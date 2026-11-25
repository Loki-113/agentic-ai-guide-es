#!/usr/bin/env python3
"""Prepare a temporary TeX copy with width-limited floating tables."""
import argparse
from pathlib import Path
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("source", type=Path)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
if args.source.resolve() == args.destination.resolve():
    parser.error("use a separate output file")

text = args.source.read_text(encoding="utf-8")
marker = r"\begin{document}"
if text.count(marker) != 1:
    parser.error("expected one document environment")
text = text.replace(marker, r"\usepackage{adjustbox}" + marker, 1)
table = re.compile(r"\\begin\{table\}.*?\\end\{table\}", re.S)
tabular = re.compile(r"\\begin\{tabular\}.*?\\end\{tabular\}", re.S)
wrapped = 0


def fit_table(match):
    global wrapped
    block = match.group()
    if r"\resizebox" in block or r"\begin{adjustbox}" in block:
        return block
    fitted, count = tabular.subn(
        lambda inner: r"\begin{adjustbox}{max width=\linewidth}"
        + inner.group()
        + r"\end{adjustbox}",
        block,
    )
    wrapped += count
    return fitted


args.destination.write_text(table.sub(fit_table, text), encoding="utf-8")
print(f"Tablas con ajuste al ancho disponible: {wrapped}")
