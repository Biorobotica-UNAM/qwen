# Historial del prompt experimental

Registro iniciado el 17 de octubre de 2026. Las entradas anteriores se reconstruyen
a partir del trabajo documentado y los artefactos disponibles; no se atribuyen
fechas ni huellas desconocidas. La evidencia exacta de cada ensayo es el prompt
congelado en su campaña, no este resumen.

## v1.6 — 17 de octubre de 2026

- Motivo: el piloto del 17 de octubre con v1.5 anunció `task completed` al inicio
  en diez casos; cuatro también lo duplicaron al final y seis omitieron el cierre
  final. «Habla sin focus» se podía confundir con la lista de anuncios iniciales.
- Cambio: `task completed` se añade explícitamente a `operations`, exactamente una
  vez, como último paso. Nunca se añade a `announcements`. Si falta desactivar
  focus, se hace antes del cierre. Las demás frases de estado conservan su posición.
- El validador también detecta cierres prematuros o duplicados; no repara la salida.
  Es un cambio del instrumento de evaluación, separado del cambio del prompt.
- Se incorporan `prompt_version`, historial y huellas al manifiesto de campañas
  nuevas cuando el prompt coincide con una versión registrada.
- Se mantienen modelo, esquema, entradas y política CLIPS del piloto previo para
  la nueva prueba. La eficacia del cambio se determina en los resultados, no aquí.

## v1.5 — versión conservada en pilotos del 9 y 17 de octubre

- Política general de focus: bloques contiguos de say/listen para el mismo
  interlocutor, incluso entre objetivos. Anuncios y otras acciones cierran el bloque.
- Conserva `waving person` y la distinción entre superficies de colocación.
- Defecto observado: cierre prematuro o duplicado; corregido en v1.6.

## v1.4 — revisión intermedia

- Ciclo continuo de focus para preguntar, escuchar y confirmar el nombre.

## v1.3 — revisión intermedia

- Dos ciclos separados: pregunta/escucha y confirmación, según la política
  discutida entonces. Sustituida por v1.4.

## v1.2 — revisión intermedia

- Focus antes de preguntar el nombre; evita una segunda activación tras escuchar.
- Hace explícitas `storage_rack → shelf`, `table → table` y
  `gesture='waving person'`, conservando `waving_1` para el ejecutor.

No se conservó aquí una copia independiente verificable de v1.2–v1.4. Estas
descripciones no sustituyen sus textos completos ni se usan para inventar hashes.

## v1.1 — versión conservada en el piloto del 8 de octubre

- Prompt de referencia del primer piloto, con objetivos y expansión del plan.
- Se observaron dos diferencias de superficie y una activación adicional de focus.

## Cómo rastrear un resultado

`resultados.jsonl` contiene `campaign_id`, `config_id` y la huella del manifiesto.
El manifiesto identifica modelo, parámetros y `prompt.path`/`prompt.sha256`.
Las campañas nuevas también incluyen la versión declarada y copias del historial
cuando existe una entrada con la misma huella. El historial no se envía al modelo.
Un prompt personalizado sin coincidencia conserva su copia y hash, pero no recibe
una asociación de historial inventada. Los resultados históricos no se modifican.
