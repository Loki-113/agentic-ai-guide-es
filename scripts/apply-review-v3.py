#!/usr/bin/env python3
"""Replay the reviewed edits after regenerating the automatic draft."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "translation/source-v3-es"
BASE = "0d932aa75cd528263169038a2fd82c6a3338ea446eb00a1cbbcde7303caa0f61"
PRIORITIES = {
    "salida Unicode incompatible con pdfLaTeX": "P0",
    "salida rechazada": "P1",
    "sin cambio; comprobar término o nombre": "P1",
    "comprobar término del glosario": "P1",
    "fragmento breve sin contexto": "P2",
}


def main():
    book = DEST / "book.tex"
    raw = book.read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE:
        raise SystemExit("Regenera primero el borrador automático v3 que corresponde a esta revisión.")

    lines = raw.decode().splitlines(keepends=True)
    closed_p0 = set()
    for row in (DEST / "review-edits.tsv").read_text().splitlines()[1:]:
        line, priority, old, new, reason = row.split("\t")
        index = int(line) - 1
        if lines[index].count(old) != 1:
            raise SystemExit(f"Edición ambigua en la línea {line}.")
        lines[index] = lines[index].replace(old, new, 1)
        if priority == "P0":
            closed_p0.add(line)

    markers = DEST / "TODO-REVIEW.tsv"
    rows = ["línea_fuente\tmarca\tprioridad\tmotivo"]
    for row in markers.read_text().splitlines()[1:]:
        line, mark, reason = row.split("\t")
        priority = PRIORITIES[reason]
        if priority == "P0" and line in closed_p0:
            continue
        rows.append("\t".join((line, mark, priority, reason)))

    stats = DEST / "coverage.json"
    coverage = json.loads(stats.read_text())
    coverage["todo_review"] = len(rows) - 1
    book.write_text("".join(lines))
    markers.write_text("\n".join(rows) + "\n")
    stats.write_text(json.dumps(coverage, ensure_ascii=False, sort_keys=True, indent=2) + "\n")


if __name__ == "__main__":
    main()
