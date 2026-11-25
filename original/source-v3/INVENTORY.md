# Inventario de la fuente TeX v3

| Componente | Cantidad y ubicación |
| --- | --- |
| Archivos regulares | 73, incluidos el manifiesto `00README.json`, el TeX, el BibTeX y 70 imágenes |
| LaTeX | 1, `book.tex` |
| Bibliografía | 1, `references.bib`, con 468 entradas. El documento selecciona `plainnat` con `natbib`. |
| Recursos gráficos | 70 en `figures/`, 69 PNG y 1 JPG. Las 70 rutas distintas de `includegraphics` existen localmente. |
| Figuras y diagramas | 77 entornos `figure` y 5 bloques TikZ en las líneas 678, 1033, 11155, 14052 y 20317. El conjunto PNG incluye diagramas rasterizados, como `fig_049_agentic-stack.png` y `fig_076_deployment-arch.png`. |
| Tablas | 113 entornos `table`, 182 `tabular` y 2 `tabularx`. Los entornos pueden anidarse. |
| Listados | 204 entornos `lstlisting` y 2 `verbatim`. El paquete contiene los listados en el TeX y carece de cuadernos o scripts independientes. |
| Tipografía y recursos externos | 0 archivos de fuente tipográfica. Usa Latin Modern vía `lmodern`, codificación T1 y entrada UTF-8. Los 26 destinos HTTP(S) distintos de `href` y `url` son enlaces en el texto. La bibliografía contiene referencias externas adicionales. |

Los recuentos de entornos se obtuvieron del TeX y no son aditivos.
El código de los notebooks MIT quedó sin descargar. La declaración
CC BY-SA 4.0 aparece también en el TeX. Sigue pendiente revisar los
créditos y derechos por recurso antes de redistribuir la fuente.

El [manifiesto SHA-256](SHA256SUMS) enumera los 73 archivos del paquete.
Se calculó a partir del archivo descargado.
