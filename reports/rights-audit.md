# Auditoría de derechos de los recursos

El inventario identifica 901 registros por ruta, localizador, tipo,
procedencia, licencia, distribución, atribución, riesgo y acción.
Los localizadores del TeX y las claves bibliográficas identifican cada
elemento sin duplicar su contenido. [Inventario TSV](rights-inventory.tsv)

## Obra y traducción

La ficha de arXiv v3 identifica la licencia CC BY-SA 4.0 de la obra.
La traducción derivada aplica la misma licencia. El TeX original, el
TeX traducido, la bibliografía y los recursos de origen se conservan
para trazabilidad. Las figuras y otros componentes que puedan
pertenecer a terceros requieren un cotejo independiente.
[Ficha de arXiv](https://arxiv.org/abs/2606.24937v3) ·
[Licencia CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) ·
[Atribución](../ATTRIBUTION.md)

## Resultados por tipo de recurso

| Recurso | Distribución y resultado |
| --- | --- |
| 69 PNG y 1 JPG | Empaquetados en la fuente y el EPUB, y usados por el PDF. Autoría, licencia y crédito individual PENDIENTES. Incluye diagramas rasterizados y el logotipo. |
| 5 diagramas TikZ y 113 tablas | Presentes en el TeX y usados en el PDF. Procedencia y derechos por elemento PENDIENTES. La exportación EPUB puede simplificar diagramas y tablas LaTeX. |
| 204 listados y 2 bloques literales | Redistribuidos en el TeX. Los créditos, la procedencia y las licencias de fragmentos de terceros dentro de esos bloques están PENDIENTES. |
| 468 entradas bibliográficas | Metadatos conservados, con las obras citadas como referencias. La licencia de una obra citada requiere verificación si se incorpora contenido suyo. |
| Tipografías del PDF | Latin Modern con licencia GUST según el paquete instalado. Los binarios AMS y los avisos concretos de los subconjuntos embebidos quedan PENDIENTES. La hoja legal usa referencias a fuentes base PDF. El EPUB carece de archivos tipográficos. |
| Iconos e imágenes externas | Sin archivos de iconos separados en el paquete. Los elementos gráficos dentro de imágenes y las posibles figuras derivadas de fuentes externas se incluyen en el cotejo individual de los 70 archivos. |
| Notebooks y código complementario | Solo referenciados. MIT confirmado en el commit auditado para el código de ese repositorio. Datos, modelos, dependencias y contenido de terceros requieren revisión propia si se incorporan. |

[Inventario de la fuente v3](../original/source-v3/INVENTORY.md) ·
[LICENSE MIT del repositorio complementario fijado](https://github.com/haggair/agentic-ai-book/blob/243a9484ae94998309ecdd331dde47bc77e92001/LICENSE) ·
[Latin Modern de GUST](https://www.gust.org.pl/projects/e-foundry/latin-modern)

## Acción antes de abrir el repositorio

Cotejar por elemento las figuras, el logotipo, los diagramas, las
tablas y los listados con sus créditos y condiciones de origen.
Documentar la evidencia de cada permiso y los avisos de las fuentes
embebidas. Si alguno requiere autorización adicional, obtenerla o
acordar el tratamiento de ese recurso antes de la apertura.
