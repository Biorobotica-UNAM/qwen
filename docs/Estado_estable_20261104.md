# Base estable del proyecto — 4 de noviembre de 2026

Esta entrega organiza el código, la documentación y la evidencia disponibles para
retomar posteriormente el experimento final. Es una base local verificable, no
el acta de congelación experimental: falta cerrar datos y configuraciones finales.
No se ejecutaron nuevas consultas a modelos durante la estabilización.

## Puntos de entrada

- [README principal](../README.md): funcionamiento de Qwen–CLIPS y GPT directo, entrenamiento e inferencia.
- [Índice de reportes](../reports/README.md): fuente consolidada, evidencias y artículos conservados.
- [Guía experimental](experiment/Guia_del_experimento.md): piloto y decisiones de desarrollo.
- [Programas experimentales](../experiments/README.md): creación, ejecución y evaluación de campañas nuevas.
- [Protocolo final](experiment/Protocolo_experimento_final_tesis.md): diseño propuesto, métricas y criterios.

El piloto documentado tiene 900 primeros intentos. La propuesta final comprende
300 órdenes y cinco repeticiones por cada una de las tres condiciones: 4,500
intentos principales. El tamaño no está aprobado ni el conjunto acreditado como
construido; tampoco se ha ejecutado la evaluación final independiente.

## Conservación y verificaciones

Se archivaron 16 carpetas superadas de reportes, con 1,076 archivos comprobados
individualmente antes de retirarlos del árbol activo. Se conservaron las fuentes
necesarias para reproducir el informe vigente, las campañas originales y sus huellas.
El archivo histórico y su inventario están en `archives/estabilizacion_20261104/`.
Se verificaron las 91 huellas de fuentes del consolidado. Su generador se ejecutó
en una carpeta temporal y reprodujo exactamente los 900 registros y los resúmenes
de bloques, resultados técnicos y consistencia. No se reescribieron los reportes
originales. Se comprobaron los enlaces de la documentación activa y la presencia
de las figuras referenciadas por ambos artículos.

La suite de la revisión previa pasó 78 pruebas con sockets locales habilitados.
Persisten avisos nativos de liberación de memoria CLIPS al finalizar; no se
certifica ausencia de crecimiento de memoria. La organización documental no
modifica el código del instrumento. Véase el [registro de limpieza](Limpieza_repositorio.md).

Las huellas de esta base están en `estado_estable_20261104.sha256`. Desde la raíz:

```bash
sha256sum --quiet -c docs/estado_estable_20261104.sha256
```

Un cambio posterior en un archivo inventariado producirá una diferencia; eso no
significa por sí solo corrupción. Mantener este inventario como referencia de
esta entrega y producir otro al congelar la versión experimental final.

El respaldo `archives/estabilizacion_20261104/base_estable.tar.gz` incluye código,
datos, documentación, pruebas y reportes activos, incluidas las campañas ignoradas
por Git. Excluye pesos/checkpoints, cachés, entornos, credenciales, metadatos Git y
archivos históricos comprimidos. El archivo histórico se conserva por separado.
`RESPALDOS.sha256` permite comprobar ambos archivos desde la raíz del repositorio.
Para trasladar el proyecto, conservar también los adaptadores y sus modelos base;
no están incluidos en este respaldo. No basta un clon Git para recuperar las campañas.

## Al retomar el experimento final

1. Aprobar tamaño y cuotas del protocolo; construir el conjunto independiente y auditar coincidencias y cobertura respecto del desarrollo y entrenamiento.
2. Revisar y aprobar fichas, referencias y condiciones de escenario antes de observar respuestas finales.
3. Cerrar las capacidades pendientes, o registrarlas explícitamente como límites; comprobar el contrato y la equivalencia con el workspace Justina que se utilizará.
4. Verificar servidores y adaptadores 3B/7B, modelo GPT, parámetros, recursos observables, timeouts y recuperación con entradas de desarrollo.
5. Congelar datos, código, dependencias, modelos, prompt, reglas, hardware, orden y criterios en campañas nuevas. Registrar calentamiento y calendario efectivos.
6. Ejecutar, revisar semánticamente y analizar el experimento final conservando fallos, controles y reintentos separados.

Las herramientas y antecedentes quedan disponibles; estos pendientes científicos
y operativos deben resolverse antes de considerar terminada la evaluación final.
