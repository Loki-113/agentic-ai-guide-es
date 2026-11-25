# Auditoría técnica de la fuente

Consulta del 25 de noviembre de 2026. Se revisaron fichas, cabeceras
HTTP, fragmentos acotados del HTML y metadatos Git. El inventario
interno del paquete TeX y las pruebas de compilación quedan pendientes.

## Identificación del original

Haggai Roitman, *The Hitchhiker's Guide to Agentic AI: From Foundations
to Systems*. La ficha sin sufijo apunta a **arXiv:2606.24937v3** y el
campo de comentarios indica **version 1.4**. DOI del registro
`10.48550/arXiv.2606.24937`. Para fijar la edición debe usarse el
identificador con sufijo. La página de publicaciones del autor enlaza
la ficha de arXiv.
[Ficha actual](https://arxiv.org/abs/2606.24937) ·
[Ficha v3](https://arxiv.org/abs/2606.24937v3) ·
[Publicaciones del autor](https://sites.google.com/view/haggai-roitman/home/publications)

| Revisión | Fecha de envío a arXiv (UTC) | Versión editorial |
| --- | --- | --- |
| [v1](https://arxiv.org/abs/2606.24937v1) | 2026-06-22 17:48:54 | La ficha consultada carece de número editorial. Andy Bo Wu identifica su base como 1.2.2. |
| [v2](https://arxiv.org/abs/2606.24937v2) | 2026-07-27 15:17:17 | 1.3 |
| [v3](https://arxiv.org/abs/2606.24937v3) | 2026-09-29 08:53:18 | 1.4 |

## Huellas disponibles

| Recurso | Identificador observado | Evidencia |
| --- | --- | --- |
| PDF v3 | `0f9ca81f7521871a9dc4003c60a90fd11f1cea352a6dcc933090e9c78e0a5956` | ETag con prefijo `sha256:`, 7 734 700 bytes. [Cabeceras PDF](https://arxiv.org/pdf/2606.24937v3) |
| Paquete TeX v3 | `677362882e2a178559dafa3bcdfff97bf9260a7736578e3ca587f27a6b1df34f` | ETag con prefijo `sha256:`, 5 568 123 bytes, `application/gzip`. [Cabeceras TeX](https://arxiv.org/src/2606.24937v3) |
| Código complementario | `243a9484ae94998309ecdd331dde47bc77e92001` | Commit de `main` observado, fechado el 28 de septiembre de 2026 a las 21:00 UTC. [Referencia](https://api.github.com/repos/haggair/agentic-ai-book/git/ref/heads/main) · [Commit](https://api.github.com/repos/haggair/agentic-ai-book/git/commits/243a9484ae94998309ecdd331dde47bc77e92001) |
| Árbol del código | `65aeb5c83a2bf5e42c032390886083dbff1cb060` | Identificador Git del árbol raíz, con inventario recursivo sin truncar. [Árbol fijado](https://api.github.com/repos/haggair/agentic-ai-book/git/trees/65aeb5c83a2bf5e42c032390886083dbff1cb060?recursive=1) |

Los dos valores de arXiv proceden de peticiones HEAD. Falta verificar
los bytes con un hash local en la fase de adquisición. El PDF adjunto
queda sin inspeccionar y sin asociar a ninguna revisión.

## Fuentes y componentes

La distribución oficial de la fuente editorial es **TeX Source** en
arXiv. El repositorio [haggair/agentic-ai-book](https://github.com/haggair/agentic-ai-book)
se identifica en su README como el complemento de código del libro
y enlaza el identificador exacto de arXiv. En el árbol auditado no se
encontraron `.tex`, `.sty`, `.cls`, `.bib` ni `.bbl`. Tampoco
se encontró un repositorio público independiente de la fuente
editorial en el listado público de la cuenta revisado.
[README fijado](https://github.com/haggair/agentic-ai-book/blob/243a9484ae94998309ecdd331dde47bc77e92001/README.md) ·
[Repositorios de haggair](https://api.github.com/users/haggair/repos)

| Componente | Evidencia | Posible reutilización |
| --- | --- | --- |
| LaTeX | arXiv ofrece el paquete TeX de v3. El fichero principal, el motor y los paquetes concretos están por identificar. | Edición base e índices, tras inventariar la fuente. |
| Figuras y diagramas | El HTML v3 muestra, por ejemplo, el diagrama de topología GPU en la figura 2.3. El repositorio complementario contiene 33 PNG. | Figuras y diagramas con procedencia confirmada. Comprobar formato editable, fuentes tipográficas y rótulos. |
| Tablas | El HTML v3 incluye tablas estructuradas, como 1.5, 1.6 y 19.2. | Datos, estructura y referencias, tras revisar procedencia y encabezados. |
| Bibliografía | Se observaron entradas bibliográficas en el HTML v3. Queda pendiente determinar si el paquete contiene un `.bib`, un `.bbl` o referencias integradas. | Referencias, claves de cita y DOI, tras cotejar la fuente. |
| Código | El HTML incluye listados. El árbol complementario tiene 28 notebooks de capítulo, un notebook del proyecto final, siete archivos Python y configuración. | Enlaces fijados, notebooks y utilidades bajo los términos aplicables a cada componente. |

[Muestras de la edición HTML v3](https://arxiv.org/html/2606.24937v3) ·
[Distribución TeX v3](https://arxiv.org/src/2606.24937v3)

## Licencias y riesgos

- **Obra en arXiv — CC BY-SA 4.0.** La ficha v3 enlaza esta licencia.
  Al compartir una adaptación, se debe atribuir a Roitman, enlazar la
  licencia, indicar los cambios y aplicar la licencia exigida por
  CompartirIgual. Hay que revisar créditos y posibles exclusiones de
  texto, figuras, tablas y fragmentos de terceros por separado.
  [Ficha v3](https://arxiv.org/abs/2606.24937v3) ·
  [Resumen oficial de CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
- **Repositorio complementario — MIT.** El README y el archivo LICENSE
  lo indican para el código. Conservar el aviso de copyright y el
  texto de permiso al redistribuir las partes cubiertas. Revisar por
  separado dependencias, datos, modelos, imágenes y código incrustado
  en el libro. La licencia de la documentación propia del proyecto
  español sigue pendiente.
  [LICENSE de upstream fijado](https://github.com/haggair/agentic-ai-book/blob/243a9484ae94998309ecdd331dde47bc77e92001/LICENSE) ·
  [Aviso del proyecto](../LICENSE)
- **Compatibilidad editorial.** La conversión HTML es experimental.
  Puede perder macros, relaciones de referencias, geometría de tablas
  y detalles de diagramas. Antes de elegir formato, verificar motor,
  paquetes, fuentes, caracteres españoles, bibliografía y referencias
  cruzadas con una compilación controlada. Los formatos y la
  editabilidad dentro del paquete quedan pendientes.
- **Compatibilidad de ejecución.** El README del código indica Python
  3.10–3.12, dependencias externas y, según el ejemplo, Docker, modelos
  locales, un servicio de API o GPU. Falta cotejar cuadernos y capítulos
  con v3, comprobar versiones y probar primero con respuestas
  simuladas. La proximidad de fechas del commit y de v3 no demuestra
  que constituyan una entrega sincronizada.
  [Requisitos del código](https://github.com/haggair/agentic-ai-book/blob/243a9484ae94998309ecdd331dde47bc77e92001/README.md#prerequisites)

## Traducciones y repositorios de terceros

| Proyecto | Resultado de la revisión |
| --- | --- |
| [AndyBoWu/hitchhikers-guide-agentic-ai-zh-cn](https://github.com/AndyBoWu/hitchhikers-guide-agentic-ai-zh-cn/blob/main/NOTICE.md) | Traducción al chino simplificado. El traductor declara autorización del autor y CC BY-SA 4.0. Se basa en arXiv v1 (edición 1.2.2). |
| [Chasing1020/agentic-ai-guide-zh](https://github.com/Chasing1020/agentic-ai-guide-zh) | Traducción china no oficial con fuentes LaTeX propias de esa edición y licencia declarada CC BY-SA 4.0. |
| [luckinbyte/agentic-ai-zh](https://github.com/luckinbyte/agentic-ai-zh) | Traducción china que declara la edición 1.2.2, licencia CC BY-SA 4.0 y un flujo de compilación mdBook con KaTeX. |
| [CraigKettleman](https://github.com/CraigKettleman/hitchhiker-agentic-ai-zh), [conanxin](https://github.com/conanxin/hitchhikers-guide-agentic-ai-zh), [BrandonDing](https://github.com/BrandonDing/agentic-ai-zh) y [UNPR0110](https://github.com/UNPR0110/The-Hitchhiker-s-Guide-to-Agentic-AI-Chinese-Translation) | Otros candidatos en chino identificados por metadatos de GitHub. La cobertura, la procedencia y los permisos por componente quedan sin verificar. |

Las búsquedas públicas por título, autor e identificador no
confirmaron otra traducción completa al español. La [ficha localizada
de alphaXiv](https://www.alphaxiv.org/es/abs/2606.24937) presenta
metadatos y resumen en español. La búsqueda no es exhaustiva.
[Consulta de repositorios por título](https://api.github.com/search/repositories?q=hitchhiker+agentic+ai&per_page=30) ·
[Consulta por identificador e idioma](https://api.github.com/search/repositories?q=%222606.24937%22+espa%C3%B1ol&per_page=10)

## Pendientes antes del piloto

Registrar la edición v3 y sus condiciones en la ficha de atribución
del proyecto. Cuando se autorice la adquisición, cotejar las huellas,
inventariar el paquete TeX, revisar los créditos por recurso y
documentar la correspondencia entre el código y los capítulos.
