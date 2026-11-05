# Auditoría inicial de procedencia y cobertura

18 de octubre de 2026. Revisión del README y evidencia local. No se entrenaron
modelos, generaron nuevos comandos ni modificaron campañas o referencias.

## Comprobado

- Generador local: qwen_gpsr/generation/gpsr_commands.py, command_utils.py y
  command_goals.py; superficies y vocabularios en domain/command_constants.py.
- 29 familias y 87 variantes de plantilla, presentes también en los metadatos
  del corpus. Las variantes pueden contener subórdenes (follow-ups), por lo que
  no representan solo 87 frases ni 87 firmas completas.
- Catálogos en CompetitionTemplate: nombres, ubicaciones, habitaciones y objetos.
- Dataset actual: 40 000 filas, 20 000 people y 20 000 objects, SHA-256
  0695f400370b93abbe97fc403a2acaa9f2d6bc8241667788bd466c6ad7c1c406.
  Coincide con la huella registrada en la auditoría de coincidencias del piloto.
- Scripts train.py y train_3b.py: misma ruta de datos, TEST_SIZE=0.1,
  RANDOM_SEED=42, train_test_split. Los logs de ambos muestran 36 000/4 000 filas.
- Configuraciones de adaptador identifican las bases 3B y 7B. Los estados finales
  de Trainer señalan checkpoint-7000 para 3B y checkpoint-5000 para 7B como mejores.
  Esto no identifica por sí solo el archivo exacto ni la partición usados.

## Hallazgos que afectan la clasificación

- countClothPrsInRoom contempla conteo filtrado por vestimenta. El corpus tiene
  1 163 filas con count y wearing; ejemplo: línea 13. DEV-050 no puede descartarse
  como capacidad ausente del generador. Su expansión debe evaluarse separadamente.
- heaviest pertenece a OBJECT_COMP_LIST y a familias de propiedades. Hay 167
  filas con property=heaviest; ejemplo: línea 98. DEV-051 permite estudiar una
  discrepancia entre el dominio lingüístico y la capacidad simbólica/ejecutora.
- El corpus tiene cero secuencias con dos go consecutivos y cero goals con gesto
  y vestimenta simultáneos. Las plantillas actuales apoyan esta ausencia estructural,
  pero falta completar el análisis de sus subórdenes para cerrar la cobertura.
  Cero ocurrencias por sí solo no certifica que una gramática lo prohíba.
- Color + prenda sí aparece como atributo de vestimenta; no confundirlo con la
  conjunción de un gesto y una prenda como dos condiciones independientes.

## Procedencia confirmada por el investigador — 18 de octubre de 2026

El investigador confirmó que ambos modelos utilizaron el mismo dataset_gpsr.jsonl
sin cambios entre entrenamientos. Identificó como origen
https://github.com/RoboCupAtHome/CommandGenerator y declaró que el repositorio
no había cambiado desde que lo utilizó. La versión local fue modificada para
agregar plantillas y distintas formulaciones de un mismo conjunto de acciones.
La declaración completa queda registrada en declaracion_investigador.json.

Se consultó la página pública del repositorio de origen. Identifica la rama master
y src/robocupathome_generator/gpsr_commands.py. No se consiguió identificar en
esta consulta el commit exacto utilizado históricamente; no se atribuye al origen
la huella del código local ni se afirma haber certificado ausencia de cambios.

## Distinción necesaria para la auditoría

- Origen: CommandGenerator de RoboCupAtHome, según la procedencia declarada.
- Sistema evaluado: generador local ampliado, cuyos archivos y huellas están en
  inventario.json; este define la distribución operacional de entrenamiento.
- Corpus: mismo archivo para 3B y 7B, confirmado por el investigador, compatible
  con scripts y logs. La huella disponible fue medida sobre el archivo actual.
- División histórica: no se encontraron índices archivados de train/validación.
  No volver a pedir confirmación del archivo compartido; documentar aparte esta
  limitación de trazabilidad.

El propósito declarado es aumentar variabilidad lingüística. El código local
además identifica findNameInRoom, findObjectInRoomSimple y greetNameInRoomSimple
como nuevas coberturas semánticas respecto de un dataset anterior. Por ello, la
comparación posterior debe separar cambios de redacción de cambios en las
firmas completas admitidas; no se afirma todavía su diferencia exacta respecto
de un commit del generador externo.

Para evaluar robustez lingüística, el conjunto final no debe consistir solamente
en frases nuevas producidas por las mismas variantes ya usadas para entrenar:
separar nuevas instancias de plantillas conocidas de paráfrasis adicionales
revisadas para conservar la intención.

No se requieren ahora más documentos del investigador para continuar con el
inventario local y la clasificación. Si aparece un respaldo del generador original,
su commit o los índices de partición, podrá añadirse como evidencia adicional.

## Siguiente paso

Enumerar las firmas semánticas y rutas de follow-up alcanzables, contrastarlas
con adaptador/reglas, y clasificar las 60 órdenes con evidencia por fila. A/B
(estructura canónica frente a paráfrasis) no debe confundirse con pertenencia
literal al corpus ni con presencia en train. Mantener aparte capacidad admitida
por el generador y capacidad conservada por el plan.

La aprobación de dictámenes sigue pendiente. Conviene cerrar esta clasificación
antes de aprobar los casos de límites. Las propuestas y campañas anteriores se
conservan. El inventario es actual y exploratorio, no un registro retrospectivo
fabricado del entrenamiento.
