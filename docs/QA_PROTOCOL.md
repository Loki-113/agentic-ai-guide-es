# Protocolo de control de calidad

## Fase de documentación

1. Ejecuta `make check` desde la raíz. Comprueba archivos obligatorios,
   errores de espacio en blanco en el diff y la ausencia de material
   nuevo en las rutas reservadas para fuente, traducción y recursos.
   El control incluye archivos Git y archivos locales sin seguimiento
   que Git no ignore.
2. Revisa el diff completo, incluidas las altas, y comprueba los
   destinos de los enlaces internos. Verifica que el cambio carezca de
   credenciales, datos privados y material ajeno al alcance.
3. Confirma que los textos coinciden en el alcance y que las
   afirmaciones sobre derechos tienen respaldo. Registra el resultado
   de las comprobaciones y las incidencias abiertas.

## Fases de traducción

1. Coteja cada unidad con su localizador en la fuente. Comprueba
   cobertura, significado y conservación de referencias.
2. Revisa legibilidad, terminología, formato y accesibilidad.
3. Verifica conceptos, código, enlaces, figuras, tablas y créditos.
   Registra cómo se comprobó cada ejemplo y qué casos quedaron
   pendientes.
4. Registra unidad, revisión de Git, fecha, responsable, resultado e
   incidencias en `reports/`. Cierra las incidencias de fidelidad,
   funcionamiento o derechos antes de aprobar la unidad. Deja
   constancia de los defectos menores que se difieran.
