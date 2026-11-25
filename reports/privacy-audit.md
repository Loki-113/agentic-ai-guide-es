# Auditoría de privacidad e historial

Base auditada `58682e0502d704cf596b55b9e7beb7d1e9b20240`.
Los valores de contacto se omiten. La resolución del dominio se
comprobó sin enviar mensajes y no se verificó el buzón.

| Ubicación | Clasificación | Resultado y acción |
| --- | --- | --- |
| Ficha de arXiv y créditos del libro | Autoría pública | Se conservan los nombres necesarios para atribuir la obra y las referencias bibliográficas. |
| `original/source-v3/book.tex` y `translation/source-v3-es/book.tex`, línea 203 | Contacto ficticio o plantilla | La obra usa un marcador de sustitución. Carece de un buzón concreto en ese lugar. |
| Mismos TeX, líneas 28724, 29321 y 29323 | Contacto ficticio | Dominios reservados para ejemplos. |
| Mismos TeX, línea 27346 | Contacto real no confirmado | Dominio no reservado con resolución A/AAAA positiva. Esto no identifica el buzón ni demuestra autorización. La dirección está dentro de un bloque de código preservado. Se confirmó su presencia en las exportaciones PDF y EPUB. |
| Metadatos de autor y committer de 11 commits anteriores | Pendiente de autorización | 22 entradas de correo ajenas al formato no-reply. Confirmar si pueden hacerse públicas o aprobar una estrategia de saneamiento. |
| Commit de auditoría anterior y nuevo commit | Identidad de plataforma no-reply | Se conserva el identificador del proyecto. |
| Otros datos de contacto en texto y rutas | Dato personal no necesario | La búsqueda no identificó nuevos casos confirmados en el contenido de esta fase. Las rutas absolutas del TeX son ejemplos, sin coincidencia con rutas privadas del entorno auditado. |

## Huella histórica y tratamiento

El contacto del ejemplo está presente desde `4bea8a8` en el TeX
original y desde `563d726` en el TeX traducido. Revisar también sus
copias de lectura en `translation/source-v3-es/book-es.pdf`,
`reports/artifacts/agentic-ai-guide-es-v3-review.pdf` y
`reports/artifacts/agentic-ai-guide-es-v3-review.epub`, El cotejo del checkpoint comprimido no encontró la dirección literal.

Se preservaron los commits, el TeX original y el bloque de código.
Cambiar únicamente el dato de contacto en una exportación dejaría
el mismo dato accesible en el TeX y en el historial. Para cerrar el
P0, el propietario debe confirmar la autorización o aprobar una
referencia pública saneada que abarque todos esos formatos.
Cualquier reescritura del historial existente requiere autorización
expresa y queda fuera de esta fase.

Los commits con metadatos de correo pendientes son:
- `5d81cf16752dc966f1764ad6d1bbebfc7a8e9498`
- `6a4f7c495fb49b348fa9521310d3a8247f80d8bc`
- `256647da37476cea760c0de30a61faf398526386`
- `9d8dd37671b2c9a50d09a63c9ede71f6a6c90359`
- `7766c963bff92d1f3f159548271643e045fb599b`
- `563d7260235b41455a11280a5af7f3460a063ce2`
- `4bea8a8286bdf2279e201722dd6450d121ca39a8`
- `d08928bb3e26a055cfcef0b1eae949fcfd479c43`
- `48fd3852352d3f124ebb7550cb79e2d76aafdb40`
- `584801c57a9d524f0a9e0780648da6b93d0efd08`
- `ac731bf4c1c578f256cd52cf3128c2545883f986`
