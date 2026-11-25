# Compilación y cobertura del borrador v3

| Métrica | Resultado |
| --- | --- |
| Fuente traducida | 1 archivo, `book.tex` |
| Recursos reutilizados | 1 bibliografía y 70 imágenes, enlazadas desde la fuente v3 |
| Palabras editables procesadas | 167.731 de 167.731 (100 %) |
| Palabras fuente en segmentos con cambios | 164.312 de 167.731 (97,96 %) |
| Marcas TODO-REVIEW | 13.266 en 7.400 líneas del original |
| Bloques de código preservados | 206, además de los tramos de código en línea |
| Tokens de comando LaTeX cotejados | 34.436 |
| Comandos de referencia y cita cotejados | 2.517 |
| PDF final | 770 páginas, 0 errores fatales |

Se cotejaron byte por byte los tramos protegidos, incluidas las
fórmulas y las etiquetas. Las 9.226 apariciones reconocidas de
entidades protegidas se comprobaron en el TeX de salida.
`make check` valida la fuente original, el ámbito de cambios, la
estructura de la traducción y los hashes de los artefactos.

El piloto compiló con 733 páginas. El intento intermedio detectó
U+0308 aislado y terminó con un error de pdfLaTeX. Tras aplicar NFC
y conservar las salidas incompatibles en el idioma original con
marca de revisión, el mismo corte compiló con 747 páginas.
La compilación final conservó 26 avisos de referencias duplicadas
y dos campos bibliográficos vacíos de la fuente. También hay
avisos de maquetación, especialmente en tablas anchas.

| Motivo automático | Marcas |
| --- | --- |
| Fragmento breve sin contexto | 10.403 |
| Sin cambio; comprobar término o nombre | 2.144 |
| Comprobar término del glosario | 682 |
| Salida rechazada | 36 |
| Salida Unicode incompatible con pdfLaTeX | 1 |

Se utilizó Argos inglés–español 1.0 local con CTranslate2 4.9.1.
El PDF se compiló con latexmk 4.86, pdfLaTeX de TeX Live
2025/dev/Debian, BibTeX y `-no-shell-escape`. Los hashes de
la versión entregada figuran en [SHA256SUMS](SHA256SUMS).
