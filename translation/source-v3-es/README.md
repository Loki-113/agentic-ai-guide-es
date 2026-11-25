# Traducción de trabajo v3

Traducción automática al castellano de *The Hitchhiker's Guide to
Agentic AI: From Foundations to Systems*, de Haggai Roitman, arXiv
2606.24937v3, versión 1.4. Adaptación automática en curso bajo
CC BY-SA 4.0. [Obra original](https://arxiv.org/abs/2606.24937v3) ·
[Licencia](https://creativecommons.org/licenses/by-sa/4.0/)

El TeX sigue la numeración de líneas de la fuente. La bibliografía y
las figuras se referencian localmente. Los bloques de código, comentarios
incluidos, se mantienen completos byte por byte. Las fórmulas y los
diagramas TikZ se conservan también íntegros. El TSV `TODO-REVIEW.tsv`
localiza los casos señalados automáticamente y `coverage.json` recoge
los recuentos sobre palabras de tramos editables del original.

Desde la raíz del repositorio, usa Python con `ctranslate2==4.9.1` y
`sentencepiece==0.2.3`. Extrae el modelo inglés–español Argos 1.0
fuera del repositorio. Conserva el fichero SQLite entre ejecuciones.
[Modelo Argos](https://argos-net.com/v1/translate-en_es-1_0.argosmodel)

```sh
python scripts/translate-v3.py /ruta/en_es /ruta/checkpoint.sqlite --blocks 10
python scripts/translate-v3.py /ruta/en_es /ruta/checkpoint.sqlite
make check
```

Cada lote de hasta 64 segmentos únicos se guarda en el checkpoint.
Las ejecuciones consultan la identidad del TeX, el script, el glosario
y el modelo antes de reutilizar resultados. Para compilar, ejecuta
`latexmk -norc -pdf -outdir=/ruta/salida book.tex` desde este directorio.
