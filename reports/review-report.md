# Revisión automática del borrador castellano v3

25 de noviembre de 2026. La base revisada es el commit
`256647da37476cea760c0de30a61faf398526386`. La fuente de comparación
es arXiv:2606.24937v3, versión 1.4, conservada en `original/source-v3/`.

## Incidencias y marcas

| Prioridad | Marcas antes | Incidencias confirmadas | Correcciones | Marcas después |
| --- | ---: | ---: | ---: | ---: |
| P0 — estructura, fórmula, código o referencia | 1 | 1 | 1 | 0 |
| P1 — riesgo técnico o terminológico | 2.862 | 63 | 63 | 2.862 |
| P2 — estilo o fluidez | 10.403 | — | 0 | 10.403 |
| Total | 13.266 | 64 | 64 | 13.265 |

Se restauraron los literales del ejemplo de tokenización en la línea
1067. Entre ellos estaban la cadena de entrada y la primera partición
en subpalabras. El borrador compilaba, pero ese ejemplo había perdido
su contenido literal. La marca que procedía de la salida Unicode
incompatible se cerró. Los 36 rechazos de salida que habían conservado
el inglés se clasificaron como P1, ya que no introdujeron daños de
LaTeX. Las marcas P1 anteriores indican casos posibles y siguen abiertas
cuando no se puede vincular la marca a un reemplazo concreto en esa
línea. [Correcciones reproducibles](../translation/source-v3-es/review-edits.tsv) ·
[Marcas priorizadas](../translation/source-v3-es/TODO-REVIEW.tsv)

## Terminología

La búsqueda emparejó las líneas del original con las del borrador.
Las correcciones se limitaron a coincidencias inequívocas y a tramos
de prosa. Se aplicaron las formas fijadas por el glosario donde
correspondía. Las variantes ambiguas se mantuvieron.

| Términos revisados | Correcciones |
| --- | ---: |
| Agent y agentic AI | 17 en agentic AI |
| harness y tool use | 10 en harness |
| memory y retrieval | 0 |
| reasoning y alignment | 19 en reasoning |
| reward y policy | 8 en reward |
| trajectory | 1 |
| embedding | 6 |
| prompt y context window | 2 en context window |
| inference y evaluation | 0 |

[Glosario](../translation/glossary/v3-en-es.tsv)

## Preservación y enlaces

| Elemento | Resultado |
| --- | --- |
| Comandos LaTeX | 34.436 tokens con secuencia idéntica |
| Referencias y citas | 2.517 comandos conservados. Incluye `\label`, `\ref`, `\eqref` y `\cite`. |
| Destinos | 121 argumentos cotejados de URL y enlaces, incluidos 93 `\hyperref`. |
| Matemáticas | 286 entornos y 4.294 tramos delimitados sin cambios |
| Código | 206 bloques idénticos, incluidos los comentarios |
| Bibliografía | 468 entradas en el mismo fichero, con claves, DOI, URL y publicaciones preservados |
| Enlaces y referencias internas sin resolver | 0 |

Se contrastaron 195 usos de referencias internas con el fichero
auxiliar de cada compilación y se resolvieron 466 claves citadas.
Se verificó la identidad de los destinos externos presentes en el
TeX. La disponibilidad remota de esos destinos queda fuera de esta
comprobación.

Se conservaron los 26 avisos por etiquetas duplicadas que ya existían
en el original. El multiconjunto de avisos coincide exactamente en
ambas compilaciones.

| Apariciones en el registro | Etiquetas |
| --- | --- |
| 3 | `motivation`, `trl-implementation` |
| 2 | `architecture.`, `evaluation`, `results.`, `results.-1` |
| 1 | `action-space-design`, `algorithm`, `architecture-overview`, `common-failure-modes`, `cost-optimization-strategies`, `design-philosophy`, `dynamic-allocation.`, `latency-optimization`, `limitations.`, `practical-implications`, `subsec:framework-comparison`, `summary` |

## Compilación y estado editorial

Se ejecutó latexmk con pdfLaTeX y BibTeX en dos directorios limpios,
con `-halt-on-error` y `-no-shell-escape`. Ambas compilaciones
terminaron con **770 páginas**, sin errores fatales ni citas
indefinidas. Los dos PDF solo difieren en el identificador interno
del documento. Persisten los avisos heredados de etiquetas y dos campos
bibliográficos vacíos, además de avisos de maquetación, en particular
tablas anchas.

El texto sigue siendo un borrador automático. Las marcas restantes
requieren revisión técnica o lingüística, y la maquetación y los
derechos por recurso requieren revisión editorial.

[PDF revisado](../translation/source-v3-es/book-es.pdf) ·
[Manifiesto SHA-256](../translation/source-v3-es/SHA256SUMS)
