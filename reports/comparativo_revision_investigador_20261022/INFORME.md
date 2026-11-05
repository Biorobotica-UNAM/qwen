# Revisión con decisiones del investigador — 22 de octubre de 2026

Se aplican las aclaraciones del investigador a los 180 primeros intentos guardados.
Las campañas, objetivos, planes y referencias originales permanecen intactos.
La clasificación por bloques sigue aprobada. Se conserva por fila el dictamen anterior,
la decisión, su fundamento y la identificación del resultado original.

## Supuestos aceptados y alcance

- DEV-019–024, 028–030, 034–036 y 043–045: la única persona presente en la habitación
  representa al destinatario nombrado. Es una condición declarada de estos escenarios,
  no una afirmación general sobre toda prueba GPSR. No se aplica al conteo de personas.
- DEV-025–027: el investigador confirma compatibilidad con el supervisor; se acepta el
  protocolo de seguimiento. No se afirma éxito físico ni se inventa una huella histórica.
- DEV-037–039: se acepta el protocolo de memoria/reporte por declaración del investigador.
  La cadena ejecutora completa no ha sido probada por este análisis.
- DEV-040–042 y 046–048: se ratifica el cumplimiento simbólico ya propuesto.
- GPT/DEV-024 conserva el fallo de focus y Qwen7B/DEV-029 conserva orange coat en lugar de
  orange: el supuesto sobre identidad no corrige esos errores independientes.
- DEV-052 no fue incluido en esta aprobación: Qwen mantiene no verificable por identidad
  y contrato histórico; GPT mantiene la omisión del disparador de seguimiento.

## Dos lecturas para evitar confundir aceptación con equivalencia

**Criterio estricto:** preserva las restricciones originales (peso distinto de tamaño;
conteo filtrado distinto de conteo total), aplicando los supuestos de identidad/protocolo
que el investigador acaba de declarar.

**Aceptación en el escenario:** añade DEV-050 y DEV-051 como excepciones expresamente
aceptadas por el investigador. No se denominan correcciones exitosas del plan histórico.
DEV-051 usa tamaño como proxy aceptado de peso; DEV-050 conserva un filtro omitido.
Ambas excepciones son retrospectivas y deben aparecer como tales en tesis/artículo.
Una futura regla o prompt no modifica lo que devolvieron estas campañas.

## Bloque G: 46 órdenes por sistema

| Modelo | Cumple bajo supuestos | Incumple estricto | No verificable | Excepciones aceptadas (incluidas en incumple) | Aceptados en escenario |
|---|---:|---:|---:|---:|---:|
| Qwen3B | 43 | 2 | 1 | 2 | 45/46 |
| Qwen7B | 42 | 3 | 1 | 2 | 44/46 |
| GPT | 42 | 4 | 0 | 2 | 44/46 |

Las excepciones no son una quinta categoría que se sume a las anteriores: son un subconjunto
de incumplimientos estrictos. La columna final corresponde únicamente al criterio relajado
del escenario. No sumar ni comparar tasas de criterios diferentes sin identificarlo.

## Corrección pendiente de DEV-050

La regla histórica emite analyze_objects count_person. El investigador propone analyze_person
red_shirt. Al inspeccionar AnalyzePerson.cpp actual, red_shirt no es un argumento admitido:
la forma reconocida es color_red_shirt, que localiza una persona por atributo. El componente
no implementa un conteo filtrado ni guarda el resultado que reportaría say count_category.
Cambiar solamente el nombre de acción/argumento no completa la tarea solicitada.
El investigador decidió expresamente documentar la capacidad pendiente y mantener la
aceptación excepcional en el reporte. La implementación del conteo filtrado queda aplazada;
no hay una decisión pendiente sobre implementar ahora. Ejecutor, CLIPS y prompt permanecen
sin cambios. La aceptación excepcional no convierte el plan histórico en conteo filtrado correcto.

## Todos los bloques

| Bloque | Modelo | n | Cumple bajo supuestos | Incumple estricto | No verificable | No aplicable | Excepciones |
|---|---|---:|---:|---:|---:|---:|---:|
| G | Qwen3B | 46 | 43 | 2 | 1 | 0 | 2 |
| G | Qwen7B | 46 | 42 | 3 | 1 | 0 | 2 |
| G | GPT | 46 | 42 | 4 | 0 | 0 | 2 |
| L | Qwen3B | 3 | 3 | 0 | 0 | 0 | 0 |
| L | Qwen7B | 3 | 3 | 0 | 0 | 0 | 0 |
| L | GPT | 3 | 3 | 0 | 0 | 0 | 0 |
| C | Qwen3B | 4 | 3 | 1 | 0 | 0 | 0 |
| C | Qwen7B | 4 | 1 | 3 | 0 | 0 | 0 |
| C | GPT | 4 | 4 | 0 | 0 | 0 | 0 |
| M | Qwen3B | 1 | 0 | 1 | 0 | 0 | 0 |
| M | Qwen7B | 1 | 0 | 1 | 0 | 0 | 0 |
| M | GPT | 1 | 0 | 1 | 0 | 0 | 0 |
| A | Qwen3B | 3 | 0 | 0 | 0 | 3 | 0 |
| A | Qwen7B | 3 | 0 | 0 | 0 | 3 | 0 |
| A | GPT | 3 | 0 | 0 | 0 | 3 | 0 |
| F | Qwen3B | 2 | 0 | 0 | 0 | 2 | 0 |
| F | Qwen7B | 2 | 0 | 0 | 0 | 2 | 0 |
| F | GPT | 2 | 0 | 0 | 0 | 2 | 0 |
| X | Qwen3B | 1 | 0 | 0 | 0 | 1 | 0 |
| X | Qwen7B | 1 | 0 | 0 | 0 | 1 | 0 |
| X | GPT | 1 | 0 | 0 | 0 | 1 | 0 |

A/F/X conservan su evaluación separada de aclaración/rechazo: GPT responde adecuadamente
6/6; los Qwen 0/6. Los fallos HTTP no son rechazos deliberados. En M, GPT reconoce limitación
sin cumplir la tarea; los Qwen pierden una condición. Latencia y recursos no cambian:
consultar el reporte previo, donde los recursos internos GPT son no disponibles.

Los resultados son exploratorios sobre desarrollo y una repetición; no establecen éxito
físico ni sustituyen el conjunto independiente final. Las decisiones registradas no aprueban
automáticamente otros dictámenes que el investigador no mencionó.

## Reproducción

Desde la raíz: `MPLCONFIGDIR=/tmp/matplotlib-piloto python3 reports/comparativo_revision_investigador_20261022/generar_reporte.py`.
El programa verifica las huellas de las campañas antes y después. Guardar una copia del CSV
antes de editar observaciones porque la regeneración sobrescribe las salidas derivadas.
