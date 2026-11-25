# Arquitectura editorial

| Ruta | Función |
| --- | --- |
| `docs/` | Documentación operativa del proyecto |
| `original/` | Espacio reservado para la fuente cuando proceda |
| `translation/chapters/` | Unidades de traducción en Markdown |
| `translation/glossary/` | Terminología aprobada y variantes |
| `translation/metadata/` | Identificadores, versión fuente y estado de las unidades |
| `assets/diagrams/`, `assets/figures/`, `assets/tables/` | Recursos editoriales por tipo |
| `scripts/` y `tests/` | Automatización y pruebas futuras |
| `reports/` | Resultados e incidencias de revisión |

En las fases de producción, asigna a cada unidad un identificador
estable, por ejemplo `cap-01`. Registra la relación entre ese
identificador, la edición de origen y el rango de secciones o páginas.
Usa la misma referencia en los recursos, el glosario y los informes
cuando corresponda.

El flujo previsto parte de una fuente identificada, continúa con el
inventario y la traducción, y pasa por revisión antes de preparar la
entrega. El formato de publicación se decidirá tras el piloto.
