#!/usr/bin/env python3
"""Verify protected TeX structure, source alignment and linked resources."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import runpy

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--build-dir", type=Path, help="directory with a completed latexmk build")
parser.add_argument("--original-build-dir", type=Path, help="original build, for duplicate-label comparison")
args = parser.parse_args()

pipeline = runpy.run_path(str(Path(__file__).with_name("translate-v3.py")))
source = pipeline["SOURCE"]
dest = pipeline["DEST"]
source_spans = pipeline["source_spans"]
digest = pipeline["digest"]
original = source.read_bytes().decode()
translated = (dest / "book.tex").read_bytes().decode()
if original.count("\n") != translated.count("\n"):
    raise SystemExit("Cambió la correspondencia de líneas.")

def protected(text):
    return [(text[start:end], kind) for start, end, kind in source_spans(text) if kind != "text"]

if protected(original) != protected(translated):
    raise SystemExit("Cambió la estructura o el contenido de un tramo protegido.")

patterns = {
    "comandos LaTeX": r"\\(?:[A-Za-z@]+\*?|[^\n])",
    "referencias y citas": r"\\(?:label|ref|pageref|eqref|cite\w*|bibliography\w*)(?:\[[^\]]*\])*\{[^{}]*\}",
    "destinos URL, href y enlaces internos": r"\\(?:url|href|hyperlink|hypertarget)\{[^{}]*\}|\\hyperref\[[^\]]*\]",
    "bloques de código": r"\\begin\{(lstlisting|verbatim)\}[\s\S]*?\\end\{\1\}",
}
for name, pattern in patterns.items():
    originals = [m[0] for m in re.finditer(pattern, original)]
    targets = [m[0] for m in re.finditer(pattern, translated)]
    if originals != targets:
        raise SystemExit(f"Cambió la secuencia de {name}.")
    print(f"{name}: {len(targets)}")

math_names = sorted(pipeline["PROTECTED_ENV"] - {"lstlisting", "verbatim", "Verbatim", "minted", "tikzpicture"})
math_pattern = re.compile(r"\\begin\{(" + "|".join(map(re.escape, math_names)) + r")\}")
for name in math_names:
    opening = r"\begin{" + name + "}"
    closing = r"\end{" + name + "}"
    pattern = re.escape(opening) + r"[\s\S]*?" + re.escape(closing)
    if re.findall(pattern, original) != re.findall(pattern, translated):
        raise SystemExit(f"Cambió un entorno matemático: {name}.")
print(f"Entornos matemáticos: {len(math_pattern.findall(translated))}")
print(f"Tramos matemáticos delimitados: {sum(kind == 'math' for _, _, kind in source_spans(translated))}")

for resource in ("figures", "references.bib"):
    if (dest / resource).resolve() != (source.parent / resource).resolve() or not (dest / resource).exists():
        raise SystemExit(f"Recurso ausente o distinto del original: {resource}")

coverage = json.loads((dest / "coverage.json").read_text())
markers = (dest / "TODO-REVIEW.tsv").read_text().splitlines()[1:]
assert len(markers) == coverage["todo_review"]
line_count = original.count("\n") + 1
for row in markers:
    line, mark, priority, reason = row.split("\t")
    assert 1 <= int(line) <= line_count and mark == "TODO-REVIEW"
    assert priority in {"P0", "P1", "P2"} and reason

assert coverage["source_sha256"] == digest(source)
assert coverage["changed_words"] <= coverage["processed_words"] <= coverage["editable_words"]
print(f"Marcas TODO-REVIEW: {len(markers)}")


bib = (dest / "references.bib").read_text()
entries = re.findall(r"(?m)^\s*@[A-Za-z]+\s*\{", bib)
if len(entries) != 468:
    raise SystemExit(f"La bibliografía contiene {len(entries)} entradas en vez de 468.")
print(f"Entradas bibliográficas: {len(entries)}")

if args.build_dir:
    aux = (args.build_dir / "book.aux").read_text()
    log = (args.build_dir / "book.log").read_text(errors="replace")
    build_log = (args.build_dir / "build.log").read_text(errors="replace")
    if "All targets" not in build_log or re.search(r"(?im)^!|(?:LaTeX|Package [^\n]+) Error:|Fatal error", log):
        raise SystemExit("La compilación no llegó a un resultado válido.")
    prose = "".join(
        translated[a:b] if kind not in {"code", "comment"} else " " * (b - a)
        for a, b, kind in source_spans(translated)
    )
    labels = set(re.findall(r"\\newlabel\{([^{}]+)\}", aux))
    refs = re.findall(r"\\(?:ref|eqref|autoref|pageref)\*?\s*\{([^{}]+)\}|\\hyperref\[([^\]]+)\]", prose)
    missing = {key or link for key, link in refs} - labels
    cited = {key.strip() for group in re.findall(r"\\citation\{([^{}]+)\}", aux) for key in group.split(",")}
    resolved_citations = set(re.findall(r"\\bibcite\{([^{}]+)\}", aux))
    missing_citations = cited - resolved_citations - {"*"}
    if missing or missing_citations or re.search(
        r"(?im)warning:[^\n]*(?:undefined|referenced but does not exist)", log
    ):
        raise SystemExit(f"Referencias internas ausentes: {sorted(missing)}; citas ausentes: {sorted(missing_citations)}.")
    print(f"Referencias internas resueltas: {len(refs)}; claves de cita resueltas: {len(cited - {'*'})}")

    if args.original_build_dir:
        original_log = (args.original_build_dir / "book.log").read_text(errors="replace")
        duplicate_pattern = r"Label `([^']+)' multiply defined"
        duplicates = Counter(re.findall(duplicate_pattern, log))
        if duplicates != Counter(re.findall(duplicate_pattern, original_log)):
            raise SystemExit("Cambió el conjunto de avisos de etiquetas duplicadas.")
        print(f"Avisos heredados por etiquetas duplicadas: {sum(duplicates.values())}.")
