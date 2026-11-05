> **Actualización del 21 de octubre:** consultar el [comparativo por bloques aprobados](../comparativo_bloques_20261021/INFORME.md) y la [revisión por caso](../comparativo_bloques_20261021/REVISION_POR_CASO.md). Este documento conserva las métricas históricas; no usar su agrupación inicial como clasificación aprobada.

# Comparativo exploratorio: piloto de 60 órdenes

Fecha del informe: 17 de octubre de 2026. Tres condiciones, 60 órdenes, 28 grupos de intención y una repetición: **180 primeros intentos**. No es la evaluación final ni una evaluación física.

## Resultados observados

| Indicador | Qwen3B | Qwen7B | GPT |
|---|---:|---:|---:|
| Procesamientos completados | 58/60 | 56/60 | 60/60 |
| Planes / aclaraciones / rechazos | 58 / 0 / 0 | 56 / 0 / 0 | 53 / 3 / 4 |
| Errores técnicos | 2 | 4 | 0 |
| Planes con contrato válido | 58/58 | 56/56 | 53/53 |
| Objetivos literales iguales | 38/54 | 38/54 | 52/54 |
| Planes exactamente iguales al control | 47/54 | 47/54 | 33/54 |
| Operaciones iguales al control, normalizando espacios de say | 52/54 | 49/54 | 50/54 |
| Tiempo total medio (s) | 2.381 | 1.975 | 3.839 |
| Tiempo total mediano (s) | 2.440 | 1.930 | 3.588 |
| Tiempo total p95 (s) | 3.613 | 2.950 | 6.842 |

Los tiempos incluyen fallos. Los denominadores 54 excluyen las seis fichas sin objetivos aplicables; incluyen el diagnóstico de peso y los demás límites. Ninguna coincidencia equivale automáticamente a cumplimiento. No se puntúa null == null como acierto.

## Interpretación

GPT maneja las tres ambigüedades (DEV-055–057) mediante aclaración y los tres rechazos previstos (DEV-058–060) mediante rechazo explícito. También rechaza DEV-049 por la limitación de búsqueda con dos atributos: la ficha esperaba executable; registrar esta discrepancia sin reclasificar retrospectivamente el caso como éxito.

GPT tiene objetivos literales iguales en 52/54 fichas aplicables. Las dos diferencias son el rechazo DEV-049 y el sinónimo biggest en DEV-047. Sus 53 planes pasan el contrato estructural, pero DEV-024 cierra focus antes de acabar la interacción y DEV-052 omite instruct_follow_to_bedroom. Los límites comunes de conteo filtrado y peso también persisten. No se afirma 100 % de éxito.

Qwen3B y 7B tienen igual coincidencia literal (38/54), pero fallan en casos distintos. 3B falla en la doble entrega DEV-053; 7B resuelve esa orden y falla en DEV-001–003 y cambia orange a orange coat en DEV-029. La igualdad del indicador agregado oculta diferencias relevantes.

En esta pasada 7B presenta menor tiempo total medio que 3B. Es una observación del servicio medido, no una ley sobre el tamaño de los modelos: las condiciones se ejecutaron por bloques, sin repeticiones, y no se controlaron calentamiento y carga concurrente.

## Casos que requieren revisión

- **DEV-001:** Composición de dos desplazamientos: Qwen7B busca inspection point como objeto. Qwen3B y GPT conservan las visitas.
- **DEV-002:** Qwen7B devuelve HTTP 422 con tareas añadidas y texto tras el JSON. Composición, clasificación exploratoria posterior a observar resultados.
- **DEV-003:** Qwen7B busca inspection point como objeto. Conservar como diagnóstico de composición.
- **DEV-024:** GPT desactiva focus antes de Please follow me to entrance; la interacción aún no ha terminado. No detectado por el contrato estructural.
- **DEV-029:** Qwen7B sustituye orange por orange coat; cambia el objeto solicitado.
- **DEV-049:** Dos atributos personales: Qwen3B los mezcla, Qwen7B omite vestimenta, GPT rechaza por límite del ejecutor. La referencia aprobada espera executable; el rechazo es explícito, no cumplimiento. El control tampoco garantiza ambos atributos.
- **DEV-050:** Los objetivos conservan vestimenta (con variante singular/plural); los planes no expresan el filtro rojo y ejecutan count_person. Igualdad con control no demuestra cumplimiento.
- **DEV-051:** Los tres planes usan biggest_fruit y anuncian heaviest_category. Se conserva heaviest en objetivos, pero tamaño no demuestra peso. Caso de capacidad, no éxito automático.
- **DEV-052:** GPT omite instruct_follow_to_bedroom y solo anuncia I will follow Simone to bedroom. Aun con la clave, la ejecución física del seguimiento no queda verificada.
- **DEV-053:** Qwen3B deja la taza en bed en vez de entregarla. Qwen7B y GPT conservan las dos entregas. La causa por longitud/composición no está demostrada.
- **DEV-054:** El control convierte Water en búsqueda de persona pese a kind=object. Qwen3B/7B usan water como objeto y GPT mantiene Water como objeto. No penalizar por no copiar el defecto del control.
- **DEV-055:** Falta objeto: Qwen usa it/item; GPT pide aclaración.
- **DEV-056:** Falta destino: Qwen usa destination; GPT pide aclaración.
- **DEV-057:** Falta destinatario: 3B usa her, 7B HTTP 422; GPT pide aclaración.
- **DEV-058:** Volar/inspeccionar: Qwen sustituye por ir/buscar; GPT rechaza. Aproximación no equivale a cumplimiento.
- **DEV-059:** Termostato: ambos Qwen devuelven HTTP 422 con caracteres posteriores y set fuera del repertorio; GPT rechaza.
- **DEV-060:** Contradicción tomar/no tomar: ambos Qwen devuelven HTTP 422; GPT rechaza por contradicción.

## Recursos y tokens

RAM del servidor y GPU asignada por PyTorch son ámbitos distintos del cliente. Los valores de las gráficas son medianas de picos muestreados, no consumo total de la GPU ni energía. El muestreo puede omitir picos breves. CPU/RAM/GPU internos de GPT: **no disponibles**, nunca cero.

GPT informó estos tokens agregados: `{"input_tokens": 328469, "output_tokens": 28036, "total_tokens": 356505, "cached_input_tokens": 321845}`. No se calcula coste monetario sin una tarifa verificada.

## Matrices

- Matriz de respuestas: filas = respuesta prevista; columnas = plan/aclaración/rechazo/error/timeout. El caso domain_capability_review conserva su fila propia.
- Confusión de objetivos: doce tareas binarias de presencia. TP = presente en referencia y predicción; FP = predicho sin referencia; FN = omitido; TN = ausente en ambos. Se excluyen respuestas fallidas, indicando el denominador por modelo. La negativa de GPT en DEV-049 se representa como ausencia de objetivos, no como dictamen semántico.
- Estas matrices no detectan por sí solas argumentos erróneos, multiplicidad, dependencias u orden. Por ejemplo, conservar go pero perder una segunda visita puede pasar inadvertido.
- La matriz por caso describe evidencia, no una tasa de cumplimiento humano.

## Trazabilidad y limitaciones

Los tres conjuntos de entradas y referencias tienen las mismas huellas; las referencias están aprobadas y el inventario de fuentes de los tres clientes coincide. Las reglas CLIPS de ambos Qwen también coinciden. Se verificó la integridad de las campañas antes de analizar. El modelo GPT solicitado fue gpt-5.6-terra, prompt v1.6; los modelos devueltos y parámetros completos constan en resumen_comparativo.json.

Qwen usa do_sample=false, max_new_tokens=128 y repetition_penalty=1.05. GPT usa Structured Outputs, max_output_tokens=8192 y store=false. Son sistemas configurados de manera diferente; no se atribuyen diferencias solamente al tamaño ni a CLIPS.

Este conjunto se usó para desarrollo y cambios de prompt. Existen coincidencias conocidas con el corpus de Qwen; no se auditó aquí de nuevo la procedencia exacta de ambos entrenamientos. Los 60 textos no son 60 intenciones independientes. No se hicieron pruebas de significación ni intervalos que traten paráfrasis como independientes.

La expansión local de las 54 referencias usa las reglas congeladas; queda guardada como control_diagnostico.json. No se inventan registros oficiales ni tiempos de control. Ese control puede contener defectos (Water) y limitaciones, por lo que no sustituye la rúbrica.

La revisión humana final de cumplimiento queda pendiente. Las notas de este informe son diagnósticos exploratorios posteriores a observar las respuestas, no cambios de referencias o categorías oficiales.

## Siguiente paso

Revisar los hallazgos por intención, completar los dictámenes humanos y decidir ajustes como una nueva versión de desarrollo. Después congelar la configuración y preparar un conjunto final independiente, con referencias aprobadas antes de observar resultados. Conservar intactas estas tres campañas.

## Archivos

- index.html: reporte visual local con filtro por ID y comparación de planes.
- 01–06 en PNG/SVG: figuras exportables.
- comparacion_por_caso.csv / .json: 180 registros de comparación.
- resumen_comparativo.json: métricas, matrices, modelos, parámetros y huellas.
- control_diagnostico.json: evidencia de expansión de referencias.
- generar_reporte.py: reproducción local; no consulta modelos.
