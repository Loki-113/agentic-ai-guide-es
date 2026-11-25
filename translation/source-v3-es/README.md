# Traducción de trabajo v3

Traducción automática al castellano de *The Hitchhiker's Guide to
Agentic AI: From Foundations to Systems*, de Haggai Roitman, arXiv
2606.24937v3, versión 1.4. Adaptación automática de trabajo bajo
CC BY-SA 4.0. [Obra original](https://arxiv.org/abs/2606.24937v3) ·
[Licencia](https://creativecommons.org/licenses/by-sa/4.0/)

El TeX sigue la numeración de líneas de la fuente. La bibliografía y
las figuras se referencian localmente. Los bloques de código, comentarios
incluidos, se mantienen completos byte por byte. Las fórmulas y los
diagramas TikZ se conservan también íntegros. El TSV `TODO-REVIEW.tsv`
localiza los casos señalados automáticamente y `coverage.json` recoge
los recuentos sobre palabras de tramos editables del original. La
cobertura se mide sobre esos tramos y excluye código, fórmulas,
referencias y otros elementos protegidos. Los recuentos no acreditan
fidelidad semántica. Las heurísticas de nombres y terminología
requieren revisión editorial. Los comentarios de código se conservaron
con el resto del listado porque no se verificó que una modificación
fuera segura para todos los lenguajes y para pdfLaTeX.

Desde la raíz del repositorio, usa Python con `ctranslate2==4.9.1` y
`sentencepiece==0.2.3`. Extrae el modelo inglés–español Argos 1.0
fuera del repositorio. El checkpoint comprimido permite reanudar
el estado registrado en este commit. Trabaja con una copia SQLite
descomprimida fuera del repositorio.
[Modelo Argos](https://argos-net.com/v1/translate-en_es-1_0.argosmodel)

```sh
gzip -dc translation/source-v3-es/checkpoint.sqlite.gz > /ruta/checkpoint.sqlite
python scripts/translate-v3.py /ruta/en_es /ruta/checkpoint.sqlite --blocks 10
python scripts/translate-v3.py /ruta/en_es /ruta/checkpoint.sqlite
python scripts/apply-review-v3.py
make check
```

Cada lote de hasta 64 segmentos únicos se guarda en el checkpoint.
Las ejecuciones consultan la identidad del TeX, el script, el glosario,
la bibliografía y el modelo antes de reutilizar resultados. Desde este
directorio, compila con
`latexmk -norc -pdf -outdir=/ruta/salida book.tex`.

## Artefactos

- [PDF de trabajo](book-es.pdf)
- [Fuente traducida](book.tex)
- [Glosario inicial](../glossary/v3-en-es.tsv)
- [Marcas de revisión](TODO-REVIEW.tsv)
- [Informe de revisión automática](../../reports/review-report.md)
- [Informe de la primera traducción automática](BUILD.md)
- [Hashes SHA-256](SHA256SUMS)
