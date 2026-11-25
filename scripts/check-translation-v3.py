#!/usr/bin/env python3
"""Verify protected TeX structure, source alignment and linked resources."""
import json
from pathlib import Path
import re
import runpy

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
    "bloques de código": r"\\begin\{(lstlisting|verbatim)\}[\s\S]*?\\end\{\1\}",
}
for name, pattern in patterns.items():
    originals = [m[0] for m in re.finditer(pattern, original)]
    targets = [m[0] for m in re.finditer(pattern, translated)]
    if originals != targets:
        raise SystemExit(f"Cambió la secuencia de {name}.")
    print(f"{name}: {len(targets)}")

for resource in ("figures", "references.bib"):
    if (dest / resource).resolve() != (source.parent / resource).resolve() or not (dest / resource).exists():
        raise SystemExit(f"Recurso ausente o distinto del original: {resource}")

coverage = json.loads((dest / "coverage.json").read_text())
markers = (dest / "TODO-REVIEW.tsv").read_text().splitlines()[1:]
assert len(markers) == coverage["todo_review"]
assert all(len(row.split("\t")) == 3 and row.split("\t")[1] == "TODO-REVIEW" for row in markers)
assert coverage["source_sha256"] == digest(source)
assert coverage["changed_words"] <= coverage["processed_words"] <= coverage["editable_words"]
print(f"Marcas TODO-REVIEW: {len(markers)}")
