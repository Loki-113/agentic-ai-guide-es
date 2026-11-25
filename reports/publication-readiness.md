# Preparación para publicación pública

25 de noviembre de 2026. Auditoría de la base
`5d81cf16752dc966f1764ad6d1bbebfc7a8e9498` y de los archivos
preparados para la adaptación castellana v3.1.

## Estado general — NO APTO

La licencia y la atribución están documentadas. La apertura sigue
bloqueada por los derechos de recursos redistribuidos pendientes de
verificación y por datos de autoría del historial cuya publicación
requiere decisión expresa. El repositorio conserva su visibilidad
privada y carece de una nueva release.

## Licencia principal

`LICENSE` contiene el texto íntegro oficial de Creative Commons
Attribution-ShareAlike 4.0 International. Se normalizó únicamente la
línea en blanco final del archivo descargado.
[Texto en el repositorio](../LICENSE) ·
[Texto oficial](https://creativecommons.org/licenses/by-sa/4.0/legalcode) ·
[Licencia en castellano](https://creativecommons.org/licenses/by-sa/4.0/deed.es)

## Atribución

README, atribución y formatos de lectura identifican a Haggai Roitman,
el título de la obra, la edición 1.4 del 29 de septiembre de 2026,
arXiv:2606.24937v3, el Proyecto AGENTIC AI y el repositorio castellano.
La adaptación registra los cambios de idioma, revisión y formato,
con un aviso expreso de traducción no oficial y ausencia de revisión,
aprobación o respaldo del autor. [Atribución](../ATTRIBUTION.md) ·
[Ficha oficial](https://arxiv.org/abs/2606.24937v3)

## ShareAlike

La obra derivada se identifica como CC BY-SA 4.0 en la documentación
y en los formatos de lectura. El PDF carece de cifrado y el paquete
EPUB carece de archivos de cifrado o DRM. Los derechos de terceros se
mantienen por separado. La licencia MIT del código complementario
se documenta exclusivamente para ese código.

## Recursos de terceros

El inventario registra 70 archivos gráficos, 5 diagramas TikZ,
113 tablas, 206 bloques de código o literales, 468 fichas
bibliográficas, 37 nombres tipográficos y dos grupos de recursos
complementarios referenciados. Las obras citadas solo se referencian.
Los notebooks del autor siguen sin incorporarse.

Los derechos individuales de las figuras, el logotipo, los diagramas,
las tablas y los fragmentos de código quedan PENDIENTES. Latin Modern
se identificó bajo GUST Font License en el paquete instalado. Queda
PENDIENTE la comprobación específica de los subconjuntos AMS embebidos
y de los avisos de redistribución. [Auditoría](rights-audit.md) ·
[Inventario por recurso](rights-inventory.tsv)

## PDF y EPUB

El PDF tiene 771 páginas. Se añadió una hoja legal inicial y se
actualizaron los metadatos a partir del PDF compilado del TeX revisado.
El texto extraído con la opción de maquetación de las otras 770
páginas coincide exactamente con el PDF compilado anterior.

El EPUB 3 se regeneró a partir del mismo TeX, con información legal,
metadatos y preparación de anclas de exportación. Se sustituyó la
sintaxis de dimensionado de delimitadores de una copia temporal por
la equivalente admitida por el conversor. El EPUB pasó los controles
de estructura ZIP, XML, manifiesto, navegación, imágenes y enlaces
internos. Contiene 4.504 elementos MathML, 70 imágenes y 0 enlaces
internos rotos. El conversor terminó sin advertencias matemáticas.
La equivalencia visual de tablas y diagramas en lectores concretos
queda PENDIENTE. [PDF](artifacts/agentic-ai-guide-es-v3-review.pdf) ·
[EPUB](artifacts/agentic-ai-guide-es-v3-review.epub)

## Seguridad y privacidad

El análisis por patrones examinó los archivos actuales, el contenido
textual extraíble de PDF y EPUB, los checkpoints SQLite comprimidos y
145 blobs de los 11 commits alcanzables desde la base auditada. Se
buscaron formatos comunes de tokens, claves de proveedor, secretos
asignados, credenciales en URLs, claves privadas, certificados y rutas
del entorno de trabajo. No se detectaron secretos ni rutas privadas
del entorno en el alcance y con los patrones aplicados. Este resultado
no sustituye una comprobación exhaustiva de datos de baja entropía,
imágenes o metadatos de terceros.

Los metadatos de autor y committer contienen 22 entradas de correo
ajenas al formato no-reply repartidas entre los 11 commits previos,
con valores omitidos. Su autorización para exposición pública queda
PENDIENTE. En el TeX, el contacto de la línea 203 es una plantilla y
el de la línea 27346 aparece en un ejemplo con dominio no reservado.
La condición ficticia o la autorización del segundo se debe confirmar
antes de abrir. Los otros ejemplos de correo usan dominios reservados.
Las rutas absolutas de ejemplos del original se distinguieron de las
rutas de ejecución del proyecto.

Se añadió `.gitignore` para auxiliares, cachés y archivos de entorno.
Los artefactos versionados incluyen el checkpoint reproducible y
las copias finales destinadas a revisión. El nuevo commit usa una
identidad no-reply y preserva el historial.

## Integridad de archivos

El árbol de la fuente original y el TeX traducido conservan sus
bytes. Se verificaron los manifiestos de origen y traducción, los
hashes de los artefactos y los enlaces internos de la documentación.
Los dos PDF del repositorio contienen los mismos bytes.
[Hashes de distribución](artifacts/SHA256SUMS.txt) ·
[Hashes de traducción](../translation/source-v3-es/SHA256SUMS)

## Incidencias pendientes

| Prioridad | Número | Incidencias |
| --- | ---: | --- |
| P0 | 2 | Confirmación de derechos de redistribución de terceros. Autorización de exposición de correos del historial y del contacto de ejemplo sin dominio reservado. |
| P1 | 2 | Evidencia individual de créditos y licencias del inventario. Evidencia de licencia y avisos de los subconjuntos AMS embebidos. |
| P2 | 2 | Pruebas visuales de tablas y diagramas del EPUB. Revisión editorial y de maquetación del borrador. |

Los grupos P1 de derechos aportan evidencia para cerrar el primer P0.
Las incidencias de traducción y los informes de la fase anterior
conservan su registro.

## Acciones necesarias antes de hacerlo público

1. Confirmar autoría, licencia, crédito y autorización de cada
   figura, logotipo, diagrama, tabla y fragmento redistribuido.
   Registrar pruebas o acordar el tratamiento de cualquier recurso
   que no tenga permiso suficiente.
2. Verificar las licencias y avisos de las fuentes AMS y los
   subconjuntos tipográficos embebidos. Incorporar los avisos
   exigidos antes de redistribuir.
3. Confirmar si puede exponerse el historial con los correos existentes
   y comprobar el carácter ficticio o autorizado del contacto de
   ejemplo. Si hiciera falta sanear esos datos, acordar el alcance
   antes de modificar la fuente o reescribir el historial.
4. Repetir el escaneo de privacidad y secretos sobre la referencia
   que vaya a hacerse pública y comprobar la visualización del EPUB
   en lectores objetivo. Mantener los artefactos identificados como
   borrador mientras siga pendiente la revisión editorial.

## Archivos modificados o añadidos

- `.gitattributes`
- `.gitignore`
- `ATTRIBUTION.md`
- `CHANGELOG.md`
- `LICENSE`
- `README.md`
- `docs/STATUS.md`
- `reports/artifacts/SHA256SUMS.txt`
- `reports/artifacts/agentic-ai-guide-es-v3-review.epub`
- `reports/artifacts/agentic-ai-guide-es-v3-review.pdf`
- `reports/publication-readiness.md`
- `reports/rights-audit.md`
- `reports/rights-inventory.tsv`
- `translation/source-v3-es/SHA256SUMS`
- `translation/source-v3-es/book-es.pdf`
