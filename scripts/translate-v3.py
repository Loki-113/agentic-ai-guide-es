#!/usr/bin/env python3
"""Translate editable TeX spans with local Argos weights and resumable SQLite."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "original/source-v3/book.tex"
DEST = ROOT / "translation/source-v3-es"
GLOSSARY = ROOT / "translation/glossary/v3-en-es.tsv"
BIBLIOGRAPHY = SOURCE.with_name("references.bib")
COMMAND = re.compile(r"\\(?:[A-Za-z@]+\*?|[^\n])")
SPECIAL = re.compile(r"[\\$%{}\[\]&~_^#\n]")
LETTER = re.compile(r"[A-Za-z]")
NAME = re.compile(
    r"\b(?:Haggai Roitman|Dafna Sheinwald|Guardian Angel System|Guardian Angel|"
    r"Creative Commons Attribution-ShareAlike|Model Context Protocol|Agent-to-Agent|"
    r"California SB 942|EU AI Act|Hugging Face|Google DeepMind|DeepMind|FrontierMath|"
    r"Peter Szolovits|John Doyle|William Long|Isaac Kohane|Stephen Pauker|Tobi Lütke|"
    r"OpenRouter|Perplexity|Shopify|Databricks|Cohere|Salesforce|Cloudflare|"
    r"PyTorch|TensorFlow|GitHub|OpenAI|Anthropic|DeepSeek|Microsoft|NVIDIA|"
    r"Google|Meta|Amazon|Qwen|Llama|Gemini|Claude|Mistral|LangChain|LangGraph|"
    r"Qdrant|Redis|Docker|Ollama|Python|BibTeX|LaTeX|Transformer|"
    r"GPT(?:-[\w.]+)?|[A-Z]{2,}(?:[-/][A-Za-z0-9.]+)*s?|"
    r"[A-Za-z]+[A-Z][A-Za-z0-9]*|[A-Za-z][A-Za-z0-9]*[_/][\w./-]+|"
    r"[A-Z][a-z]+\d+[\w.-]*|[A-Z][a-z]+(?= et al\.)|"
    r"(?:https?|ftp)://[^\s]+)\b"
)
TEXT_COMMANDS = set(
    "title chapter part section subsection subsubsection paragraph subparagraph caption "
    "textbf textit textsc textsl textnormal textrm emph footnote underline mbox".split()
)
TEXT_OPTIONS = TEXT_COMMANDS | {"item"}
PROTECTED_ENV = set(
    "equation equation* align align* aligned gather gather* multline multline* "
    "displaymath math split cases bmatrix pmatrix lstlisting verbatim Verbatim minted "
    "tikzpicture".split()
)
BOXES = set("keybox intuitionbox questionbox examplebox warningbox".split())
ARITY = {
    "href": (False, True),
    "hyperref": (True,),
    "addcontentsline": (False, False, True),
    "resizebox": (False, False, True),
    "parbox": (False, True),
    "raisebox": (False, True),
    "colorbox": (False, True),
    "textcolor": (False, True),
    "fcolorbox": (False, False, True),
}
UNSAFE_OUTPUT = re.compile(r"[\\{}\[\]%$&#^_~\x00-\x1f]")
TITLE_OVERRIDES = {
    "The Hitchhiker's Guide to Agentic": "Guía del autoestopista sobre sistemas agénticos de",
    "From Foundations to Systems": "De los fundamentos a los sistemas",
    "Disclaimer": "Aviso legal",
}
SUPPORTED_PUNCTUATION = frozenset("‘’“”–—…¿¡§«»")
WORD = re.compile(r"[^\W\d_]+", re.UNICODE)


def group_end(text, pos, limit):
    opening = text[pos]
    closing = {"{": "}", "[": "]"}[opening]
    depth = 1
    braces = 0
    i = pos + 1
    while i < limit:
        char = text[i]
        if char == "\\":
            i += 2
            continue
        if opening == "[":
            if char == "{":
                braces += 1
            elif char == "}":
                braces -= 1
        if not braces:
            if char == opening:
                depth += 1
            elif char == closing:
                depth -= 1
                if not depth:
                    return i + 1
        i += 1
    return pos + 1


def source_spans(text):
    """Yield disjoint protected and editable spans, retaining original bytes."""
    def parse(start, end):
        i = start
        while i < end:
            hit = SPECIAL.search(text, i, end)
            stop = hit.start() if hit else end
            if stop > i:
                yield (i, stop, "text")
                i = stop
                continue
            ch = text[i]
            if ch == "%":
                newline = text.find("\n", i, end)
                j = end if newline < 0 else newline
                yield (i, j, "comment")
                i = j
                continue
            if ch == "$" or text[i:i + 2] in (r"\(", r"\["):
                marker = "$$" if text.startswith("$$", i) else ch
                if ch == "\\":
                    marker = text[i:i + 2]
                close = {r"\(": r"\)", r"\[": r"\]"}.get(marker, marker)
                ending = re.search(r"(?<!\\)" + re.escape(close), text[i + len(marker):end])
                if ending:
                    j = i + len(marker) + ending.end()
                    yield (i, j, "math")
                    i = j
                    continue
            if ch != "\\":
                yield (i, i + 1, "syntax")
                i += 1
                continue
            match = COMMAND.match(text, i, end)
            if not match:
                yield (i, i + 1, "syntax")
                i += 1
                continue
            cmd = match[0][1:].rstrip("*")
            j = match.end()
            if cmd in {"verb", "lstinline"} and j < end:
                if text[j] == "[":
                    j = group_end(text, j, end)
                if j < end and not text[j].isspace():
                    ending = text.find(text[j], j + 1, end)
                    if ending >= 0:
                        j = ending + 1
                yield (i, j, "code")
                i = j
                continue
            env = ""
            if cmd in {"begin", "end"} and j < end and text[j] == "{":
                k = group_end(text, j, end)
                env = text[j + 1:k - 1]
                j = k
                if cmd == "begin" and env in PROTECTED_ENV:
                    delimiter = r"\end{" + env + "}"
                    ending = text.find(delimiter, j, end)
                    if ending >= 0:
                        j = ending + len(delimiter)
                        yield (i, j, "code" if env in {"lstlisting", "verbatim", "Verbatim", "minted"} else "protected")
                        i = j
                        continue
            yield (i, j, "syntax")
            i = j
            args = ARITY.get(cmd, (True,) if cmd in TEXT_COMMANDS else ())
            arg_index = 0
            while i < end:
                # Whitespace between a command and consumed arguments is literal.
                cursor = i
                while cursor < end and text[cursor] in " \t":
                    cursor += 1
                if cursor >= end or text[cursor] not in "{[":
                    break
                opening = text[cursor]
                if env and (cmd == "end" or opening == "{" and env not in {"tabular", "tabularx", "multicols"}):
                    break
                if opening == "{" and arg_index >= len(args) and (
                    cmd in TEXT_COMMANDS or cmd in ARITY or cmd in {"item", "centering", "small", "large", "Large", "Huge", "bfseries", "itshape", "mdseries", "par"}
                ):
                    break
                k = group_end(text, cursor, end)
                if k == cursor + 1:
                    break
                editable = (
                    (cmd in TEXT_OPTIONS or env in BOXES) if opening == "[" else
                    arg_index < len(args) and args[arg_index]
                )
                if editable:
                    yield (i, cursor + 1, "syntax")
                    yield from parse(cursor + 1, k - 1)
                    yield (k - 1, k, "syntax")
                else:
                    kind = "code" if cmd == "texttt" else "protected"
                    yield (i, k, kind)
                if opening == "{":
                    arg_index += 1
                i = k
    start = text.index(r"\title{")
    yield (0, start, "preamble")
    yield from parse(start, len(text))


def terms():
    return dict(line.split("\t") for line in GLOSSARY.read_text().splitlines()[1:])


def named_entities():
    authors = set()
    for entry in re.findall(r"(?m)^\s*author\s*=\s*\{([^{}]+)\}", BIBLIOGRAPHY.read_text()):
        for author in entry.split(" and "):
            family, comma, given = author.partition(", ")
            if comma and all(part and all(c.isalpha() or c in " -.’'" for c in part) for part in (given, family)):
                authors.add(re.escape(f"{given} {family}"))
    if not authors:
        return NAME
    return re.compile(r"\b(?:" + "|".join(sorted(authors, key=lambda name: (-len(name), name))) + r")\b|" + NAME.pattern)


def units(text):
    """Split editable spans at preserved names and technical identifiers."""
    entities = named_entities()
    for start, end, kind in source_spans(text):
        if kind != "text":
            yield start, end, kind
            continue
        pos = start
        for match in entities.finditer(text, start, end):
            if pos < match.start():
                yield pos, match.start(), "text"
            yield match.start(), match.end(), "name"
            pos = match.end()
        if pos < end:
            yield pos, end, "text"


def editable(text):
    match = re.fullmatch(r"([\s\W\d]*?)([A-Za-z].*?[A-Za-z0-9]|[A-Za-z])([\s\W\d]*)", text)
    return match.groups() if match else ("", "", "")


def render_candidate(original, candidate, issue):
    if original in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[original], ""
    candidate = unicodedata.normalize("NFC", candidate)
    for char in candidate:
        if char.isascii() or char in original or char in SUPPORTED_PUNCTUATION:
            continue
        if not unicodedata.name(char, "").startswith("LATIN"):
            return original, "salida Unicode incompatible con pdfLaTeX"
    return candidate, issue


def digest(path):
    return hashlib.file_digest(path.open("rb"), "sha256").hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("checkpoint", type=Path)
    parser.add_argument("--blocks", type=int, default=None, help="maximum new batches for a pilot")
    args = parser.parse_args()
    import ctranslate2
    import sentencepiece

    text = SOURCE.read_bytes().decode()
    pieces = list(units(text))
    assert "".join(text[a:b] for a, b, _ in pieces) == text
    glossary = terms()
    db = sqlite3.connect(args.checkpoint)
    db.execute("CREATE TABLE IF NOT EXISTS translations (source TEXT PRIMARY KEY, target TEXT, issue TEXT)")
    db.execute("CREATE TABLE IF NOT EXISTS metadata (id INTEGER PRIMARY KEY, signature TEXT NOT NULL)")
    identity = ":".join(digest(p) for p in (SOURCE, GLOSSARY, Path(__file__), args.model / "model/model.bin", args.model / "sentencepiece.model", BIBLIOGRAPHY))
    previous = db.execute("SELECT signature FROM metadata WHERE id=1").fetchone()
    if previous and previous[0] != identity:
        raise SystemExit("El checkpoint corresponde a otra versión de la fuente, modelo o configuración.")
    db.execute("INSERT OR IGNORE INTO metadata VALUES (1, ?)", (identity,))
    db.commit()
    saved = {s: (t, i) for s, t, i in db.execute("SELECT source, target, issue FROM translations")}
    cores = [editable(text[a:b])[1] for a, b, kind in pieces if kind == "text"]
    pending = [s for s in dict.fromkeys(cores) if s and s not in saved]
    tokenizer = sentencepiece.SentencePieceProcessor(model_file=str(args.model / "sentencepiece.model"))
    engine = ctranslate2.Translator(str(args.model / "model"), device="cpu", inter_threads=1, intra_threads=3)
    glossary_re = re.compile(r"(?<!\w)(?:" + "|".join(map(re.escape, sorted(glossary, key=len, reverse=True))) + r")(?!\w)", re.I)
    for batch_no, offset in enumerate(range(0, len(pending), 64), 1):
        if args.blocks is not None and batch_no > args.blocks:
            break
        batch = pending[offset:offset + 64]
        encoded = [tokenizer.encode(s, out_type=str) for s in batch]
        predictions = engine.translate_batch(encoded, beam_size=1, max_batch_size=1024, batch_type="tokens", max_decoding_length=512)
        rows = []
        for original, prediction in zip(batch, predictions, strict=True):
            target = tokenizer.decode(prediction.hypotheses[0]).strip()
            preferred = glossary.get(original.lower())
            if preferred:
                target = preferred.capitalize() if original[:1].isupper() else preferred
            issue = ""
            if not target or UNSAFE_OUTPUT.search(target) or len(target) > 3 * len(original) + 30:
                target, issue = original, "salida rechazada"
            elif target.casefold() == original.casefold():
                issue = "sin cambio; comprobar término o nombre"
            elif glossary_re.search(original) and not any(v.casefold() in target.casefold() for v in glossary.values()):
                issue = "comprobar término del glosario"
            elif len(WORD.findall(original)) <= 2:
                issue = "fragmento breve sin contexto"
            rows.append((original, target, issue))
            saved[original] = target, issue
        with db:
            db.executemany("INSERT INTO translations VALUES (?, ?, ?)", rows)
        if batch_no == 1 or batch_no % 10 == 0:
            print(f"Checkpoint {len(saved)}/{len(set(cores) - {''})} segmentos únicos", flush=True)

    chunks = []
    reviews = []
    counts = Counter()
    offset = line = 0
    for a, b, kind in pieces:
        assert a == offset
        offset = b
        original = text[a:b]
        result = original
        if kind == "text":
            left, core, right = editable(original)
            if core:
                words = len(WORD.findall(core))
                counts["editable_words"] += words
                if core in saved:
                    candidate, issue = render_candidate(core, *saved[core])
                    result = left + candidate + right
                    counts["processed_words"] += words
                    if candidate.casefold() != core.casefold():
                        counts["changed_words"] += words
                    if issue:
                        reviews.append((line + 1, issue))
                else:
                    reviews.append((line + 1, "pendiente de traducción"))
        if kind == "code" and original.startswith((r"\begin{lstlisting}", r"\begin{verbatim}")):
            counts["code_blocks"] += 1
        if kind in {"math", "protected", "code", "syntax", "name"}:
            assert original == result
            counts[kind] += 1
        chunks.append(result)
        line += original.count("\n")
    translated = "".join(chunks).replace(
        r"{\normalsize Versión 1.4\par}",
        r"{\normalsize Versión 1.4 (traducción automática de trabajo)\par}",
        1,
    )
    assert translated.count("\n") == text.count("\n")
    assert [(text[a:b], k) for a, b, k in source_spans(text) if k != "text"] == [
        (translated[a:b], k) for a, b, k in source_spans(translated) if k != "text"
    ], "Cambió la estructura o un tramo protegido"
    counts["todo_review"] = len(reviews)
    counts["checkpoint_segments"] = len(saved)
    counts["source_sha256"] = digest(SOURCE)
    counts["model_sha256"] = digest(args.model / "model/model.bin")
    DEST.mkdir(exist_ok=True, parents=True)
    for name, data in {
        "book.tex": translated,
        "coverage.json": json.dumps(dict(counts), ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        "TODO-REVIEW.tsv": "línea_fuente\tmarca\tmotivo\n" + "".join(f"{line}\tTODO-REVIEW\t{issue}\n" for line, issue in reviews),
    }.items():
        path = DEST / name
        scratch = path.with_suffix(path.suffix + ".tmp")
        scratch.write_text(data, encoding="utf-8")
        scratch.replace(path)
    print(json.dumps(dict(counts), ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
