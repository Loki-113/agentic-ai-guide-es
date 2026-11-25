# Preparación final para publicación pública

25 de noviembre de 2026. Base obligatoria
`58682e0502d704cf596b55b9e7beb7d1e9b20240`. Adaptación castellana v3.2
de arXiv:2606.24937v3, edición 1.4.

## Estado general — BLOQUEADO POR DERECHOS

También queda un bloqueo de privacidad. Se completó la preparación
técnica de los artefactos para revisión interna. No se autorizó la
redistribución pública de los elementos pendientes. El repositorio
sigue privado y carece de una nueva release.

## Licencia y atribución

`LICENSE` coincide con el texto oficial de CC BY-SA 4.0, con
normalización de la línea en blanco final. README, ATTRIBUTION, PDF
y EPUB identifican a Haggai Roitman, el título original, arXiv, la
edición, la fecha, el original y el Proyecto AGENTIC AI. Documentan
la traducción, los cambios y la adaptación de formato con aviso de
traducción no oficial y ausencia de aprobación o respaldo del autor.
La obra derivada usa CC BY-SA 4.0. MIT aplica al código complementario
referenciado del autor. Los artefactos carecen de DRM.
[Licencia](../LICENSE) · [Atribución](../ATTRIBUTION.md) ·
[Texto oficial](https://creativecommons.org/licenses/by-sa/4.0/legalcode)

## Derechos de terceros

Los 901 registros se clasificaron por evidencia y uso. Quedan
393 elementos NO IDENTIFICADO y uno PERMISO NECESARIO. Incluyen los
70 gráficos, con el logotipo, los cinco TikZ, las 113 tablas y los
206 bloques de código o literales. Hay indicios de procedencia para
la figura del Transformer y la visualización de LangGraph Studio,
sin permiso verificable para las copias. No se sustituyeron recursos
por materiales de origen incierto.

Se confirmó que las fuentes AMS Type 1 embebidas usan SIL OFL 1.1,
que permite la incrustación en documentos. Se conservaron las
referencias a GUST para Latin Modern. No se incorporaron notebooks
ni binarios tipográficos independientes. [Auditoría](rights-audit.md) ·
[Inventario](rights-inventory.tsv)

## Privacidad y seguridad

El dominio del contacto de ejemplo tiene resolución A/AAAA y no es
reservado. La identidad del buzón y el permiso de publicación quedan
PENDIENTES. Se comprobó que el valor aparece en los dos TeX y en
los artefactos de lectura. Figura en un bloque de código preservado
y en el original inmutable. Siguen pendientes de autorización las
entradas de correo de autoría y committer de 11 commits históricos.
Los valores se omiten y el historial se conserva.
[Ubicaciones y commits afectados](privacy-audit.md)

El escaneo por patrones cubrió 159 blobs históricos alcanzables y el
diff preparado, incluidos scripts, configuraciones, informes, texto
y metadatos de los PDF y EPUB, y checkpoints comprimidos. No detectó
secretos ni rutas privadas del entorno dentro de ese alcance.
El análisis por patrones no garantiza detectar valores de baja
entropía ni datos incluidos únicamente en imágenes.

## PDF y EPUB

- **PDF de 767 páginas.** Se inspeccionaron 12 páginas, incluida la
  hoja legal, la portada, el índice y pasajes iniciales, intermedios y
  finales con tablas, fórmulas, diagramas y pies. Se detectó un
  desbordamiento visible en la tabla de tokenización y se limitó el
  ancho de 108 tablas en una copia de compilación. La muestra revisada
  muestra la tabla dentro del ancho disponible. No se cambió el
  contenido técnico mediante esta transformación. Las referencias
  internas y las citas resuelven. Los 26 avisos de etiquetas duplicadas
  son heredados.
- **EPUB 3 con 48 secciones XHTML de lectura y 50 documentos XHTML en
  total.** Se inspeccionó visualmente una muestra con MuPDF. Se
  cambiaron un selector CSS y 196 atributos de estilo inválidos
  generados en la exportación. Las siete vistas de comprobación
  posteriores se renderizaron sin los avisos detectados. Hay 4.504
  elementos MathML, 70 imágenes y cero enlaces internos rotos.
  La equivalencia visual de todos los diagramas TikZ y tablas en
  distintos lectores queda PENDIENTE.

El PDF y el EPUB proceden del TeX corregido v3.2. Ambos incluyen
atribución visible, enlaces a la fuente y licencia, y metadatos de
título, autor y edición. El EPUB usa MathML sin fallback de TeX
notificado por el conversor.
[PDF](artifacts/agentic-ai-guide-es-v3-review.pdf) ·
[EPUB](artifacts/agentic-ai-guide-es-v3-review.epub) ·
[SHA-256](artifacts/SHA256SUMS.txt)

## Revisión de traducción

Se corrigieron siete P1 inequívocos contrastados con el original.
Se conservaron los 206 bloques de código, las fórmulas, los comandos
y las referencias. Quedan 13.265 marcas documentadas (2.862 P1 y
10.403 P2), y ninguna P0 automática abierta. Las marcas de traducción
no se confunden con los bloqueos de publicación.
[Informe de revisión](review-report.md)

## Incidencias abiertas de publicación

| Prioridad | Número | Incidencias |
| --- | ---: | --- |
| P0 | 2 | Derechos de redistribución de recursos individuales. Autorización de los datos de contacto del historial y del ejemplo reproducido. |
| P1 | 2 | Completar evidencia y créditos por recurso. Comprobar equivalencia en lectores EPUB, en especial de diagramas y tablas. |
| P2 | 2 | Revisar redacción y fluidez del borrador. Revisar maquetación restante en casos no cubiertos por la muestra. |

## Acciones antes de abrir el repositorio

1. Confirmar licencias, atribuciones y permisos de los 394 elementos
   pendientes. Si un recurso no se puede distribuir, el propietario
   debe aprobar su sustitución, su exclusión de un paquete público
   separado o la conservación del proyecto en privado.
2. Obtener confirmación verificable sobre la publicación de los
   contactos históricos y del ejemplo. Si no hay autorización,
   el propietario debe aprobar una referencia pública saneada.
   Cualquier cambio del original o reescritura del historial requiere
   autorización expresa adicional.
3. Repetir el escaneo de la referencia que vaya a abrirse y comprobar
   las tablas y los diagramas en los lectores EPUB previstos. Mantener
   identificada la versión como traducción de trabajo.

## Validaciones y alcance

Se comprobó `make check`, `git diff --check`, los archivos
obligatorios, los enlaces internos y los manifiestos de integridad.
La fuente original conserva sus bytes. El cambio de TeX se limita
a siete correcciones contrastadas. Las reglas de `.gitignore`
cubren los auxiliares, y no se añadieron archivos temporales.

## Archivos modificados o añadidos

- `ATTRIBUTION.md`
- `CHANGELOG.md`
- `README.md`
- `docs/STATUS.md`
- `reports/artifacts/SHA256SUMS.txt`
- `reports/artifacts/agentic-ai-guide-es-v3-review.epub`
- `reports/artifacts/agentic-ai-guide-es-v3-review.pdf`
- `reports/privacy-audit.md`
- `reports/publication-readiness.md`
- `reports/review-report.md`
- `reports/rights-audit.md`
- `reports/rights-inventory.tsv`
- `scripts/prepare-pdf-layout-v3.py`
- `translation/source-v3-es/SHA256SUMS`
- `translation/source-v3-es/book-es.pdf`
- `translation/source-v3-es/book.tex`
- `translation/source-v3-es/review-edits.tsv`
