# Reportes vigentes

Estado documental estable: **4 de noviembre de 2026**. El piloto está consolidado;
el experimento final sigue pendiente. Esta carpeta reúne resultados vigentes,
evidencia original y antecedentes necesarios para reproducir los dictámenes.

## Lectura principal

| Material | Uso |
|---|---|
| [Piloto consolidado](comparativo_escenario_20261024/INFORME.md) · [reporte visual](comparativo_escenario_20261024/index.html) | Fuente principal: 60 órdenes, 28 intenciones, cinco repeticiones y tres sistemas, 900 primeros intentos |
| [Análisis de consistencia](comparativo_escenario_20261024/ANALISIS_CONSISTENCIA.md) | Interpretación de variaciones, argumentos y redundancias |
| [Decisión DEV-052](comparativo_escenario_20261024/decision_DEV052.json) | Condición de identidad y protocolo acordada para el escenario |
| [Auditoría de cobertura](auditoria_cobertura_20261018/PROCEDENCIA.md) | Ámbito del generador, clasificación y aprobación |
| [Auditoría de coincidencias v02](evaluation/auditoria_desarrollo_v02.json) | Comparación de las entradas de desarrollo con el corpus |
| [Protocolo final](../docs/experiment/Protocolo_experimento_final_tesis.md) | Propuesta independiente, pendiente de aprobación y congelación |

## Evidencia y reproducción

- `experiments/`: campañas originales, manifiestos, respuestas y diarios. Se conservan intactos, incluso los intentos preliminares. No reanudar campañas históricas con fuentes nuevas.
- `evaluation/`, `training/`, `figures/`: auditorías, resultados de entrenamiento y figuras utilizadas en la documentación.
- `comparativo_revision_investigador_20261022/`: sus dictámenes y decisiones son entradas directas del generador del informe consolidado.
- `comparativo_bloques_20261021/` y `revision_cumplimiento_20261018/`: antecedentes de esos dictámenes y de su reproducción. No sustituyen al informe consolidado.
- `comparativo_piloto60_20261017/`: primera pasada R1, citada por la guía histórica; sus 180 intentos están incluidos en los 900.
- `repeticiones_20261023/`: vínculo entre R1 y R2–R5 y política GPT de las campañas adicionales.
- `diagnostics/`: evidencia de diagnóstico de CLIPS. Los avisos de memoria siguen siendo una limitación documentada.

Para reproducir el informe sin alterar la evidencia publicada, copiar primero el
repositorio a una carpeta de trabajo. Los scripts `generar_reporte.py` y
`completar_analisis.py` escriben en su propia carpeta. El segundo inspecciona
además fuentes del workspace Justina externo. La reproducción de resultados
históricos no consiste en volver a consultar modelos con el código actual.

## Artículos y documentos conservados

| Carpeta | Contenido |
|---|---|
| [alinear_tutor_20261029](alinear_tutor_20261029/README.md) | Últimas copias locales identificadas de artículos en español e inglés, fuentes, figuras y PDF |
| [envio_icaart_2027_20261029](envio_icaart_2027_20261029/LEEME_ENVIO.md) | Paquete preparado de revisión anónima y su procedencia; no acredita envío ni vigencia de plazos |
| `tdp_qwen_clips_20261029/` | Sección descriptiva de Qwen–CLIPS y procedencia |

Los scripts editoriales `preparar.py` y `publicar.py` son registros de operaciones
históricas sobre carpetas externas; no son comandos del experimento final.
El paquete estable permite consultar los documentos sin ejecutar esos scripts.

## Archivo histórico

Se archivaron **16 carpetas**, **1,076 archivos** (418,259,297 bytes sin comprimir),
conservando rutas relativas y contenido verificado por SHA-256:

- Archivo local: [reportes_historicos.tar.gz](../archives/estabilizacion_20261104/reportes_historicos.tar.gz).
- [Inventario completo](../archives/estabilizacion_20261104/inventario_reportes.json).
- [Resumen y huella del archivo](../archives/estabilizacion_20261104/resumen_reportes.json).

Incluye etapas editoriales de artículos y los comparativos
`comparativo_5_repeticiones_20261023` y `comparativo_criterios_20261023`, sustituidos
por el consolidado del 24 de octubre. Archivar no cambia su condición histórica.

Para recuperar una carpeta, desde la raíz del repositorio y comprobando antes que
no exista el destino:

```bash
tar -xzf archives/estabilizacion_20261104/reportes_historicos.tar.gz \
  reports/comparativo_criterios_20261023
```

`archives/` y las campañas de `reports/experiments/` están excluidos de Git.
Conservar el respaldo local al trasladar el proyecto; un clon de Git por sí solo
no contiene toda la evidencia. La [base estable](../docs/Estado_estable_20261104.md)
describe el respaldo de esta entrega y los pendientes para retomar el experimento.
