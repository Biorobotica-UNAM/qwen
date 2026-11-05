from pathlib import Path
import hashlib,json,shutil
P=Path(__file__).resolve().parent;R=P.parent/'tutor_articulos_20261029'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
trace={}
for lang,folder in [('es','Articulo Espanol'),('en','Articulo ingles')]:
 es=lang=='es';src=Path('/home/sergio')/folder;dst=P/lang;dst.mkdir(exist_ok=True)
 for f in src.iterdir():
  if f.is_file() and f.suffix in ['.tex','.bib','.cls','.sty','.bst']:shutil.copy2(f,dst/f.name)
 shutil.copytree(src/'figures',dst/'figures',dirs_exist_ok=True)
 for ext in ['tex','pdf']:shutil.copy2(src/f'articulo.{ext}',P/f'anterior_{lang}.{ext}')
 for name in ['virbot_general.pdf','virbot_ros2.pdf']:shutil.copy2(P/'imagenes'/name,dst/'figures'/name)
 trace[lang]={'source':str(src),'tex_sha256':sha(src/'articulo.tex')}
 # Source prior to our additions; reproduce the tutor's textual edits below.
 s=(R/f'original_{lang}.tex').read_text()
 a=s.index('\\author{%');b=s.index('\n}',a)+2
 aff=(r'''\sup{1}Laboratorio de Bio-Robótica, Facultad de Ingeniería, Universidad Nacional Autónoma de México, México\\
    \sup{2}Advance Intelligence and Robotics Research Center, Tamagawa University, Japón'''
 if es else r'''\sup{1}Bio-Robotics Laboratory, College of Engineering, National Autonomous University of Mexico, Mexico\\
    \sup{2}Advance Intelligence and Robotics Research Center, Tamagawa University, Japan.''')
 authors='\\author{%\n'+''.join('  \\authorname{'+n+'\\sup{'+i+'}}%\n' for n,i in [('Sergio Cano','1'),('Jesus Savage','1'),('Marco Negrete','1'),('Mauricio Matamoros','1'),('Angel Contreras','2')])+r'''  \affiliation{%
    '''+aff+r'''%
  }%
  \email{\{Sergio Cano \textless sergio081096@gmail.com\textgreater, Jesus Savage \textless robotssavage@gmail.com\textgreater\}}%
}'''
 s=s[:a]+authors+s[b:]
 if es:
  s=s.replace('Qwen--CLIPS con intérpretes Qwen2.5-3B','Presentamos Qwen--CLIPS con intérpretes Qwen2.5-3B',1)
  old='La evaluación exploratoria fuera de línea, delimitada por la cobertura GPSR implementada y sus casos de contraste, comprende 60 órdenes en inglés, 28 intenciones y cinco ejecuciones por sistema: 900 ejecuciones iniciales en total, de las cuales 690 corresponden al bloque G (46 órdenes × 5 ejecuciones × 3 sistemas).'
  new='La evaluación exploratoria fuera de línea, delimitada por la cobertura implementada de la prueba General Purpose Service Robot (GPSR) de la liga RoboCup@Home y sus casos de contraste, comprende 60 órdenes en inglés.'
  assert old in s;s=s.replace(old,new)
  s=s.replace('El coste de las 300 solicitudes GPT fue US\\$2.07. ','',1)
  s=s.replace('su conexión con CLIPS y el contrato de Justina,','su conexión con CLIPS y nuestro robot de servicio, llamado Justina,',1)
  s=s.replace('arquitectura de control ViRBot y se comunican mediante ROS~2, infraestructura de software para conectar componentes robóticos.','arquitectura de control ViRbot (Figura~\\ref{fig:virbot_general}) y se comunican mediante ROS~2, infraestructura de software para conectar componentes robóticos (Figura~\\ref{fig:virbot_ros2}).',1)
 else:
  old='The exploratory offline evaluation, bounded by the implemented GPSR coverage and contrasting cases, comprises 60 English commands, 28 intents, and five runs per system: 900 records.'
  new='The exploratory offline evaluation, bounded by the implemented coverage of the General Purpose Service Robot (GPSR) task in the RoboCup@Home league and contrasting cases, comprises 60 English commands.'
  assert old in s;s=s.replace(old,new)
  s=s.replace('The cost of the 300 GPT requests was US\\$2.07. ','',1)
  s=s.replace("its connection to CLIPS and Justina's contract,",'its connection to CLIPS and our service robot, named Justina,',1)
  s=s.replace("UNAM's Faculty of Engineering Bio-Robotics Laboratory","UNAM's college of Engineering Bio-Robotics Laboratory",1)
  s=s.replace('through the ViRBot control architecture and communicate through ROS~2, software infrastructure for connecting robotic components.','through the ViRbot control architecture, see figure~\\ref{fig:virbot_general}, and communicate through ROS~2, software infrastructure for connecting robotic components, figure~\\ref{fig:virbot_ros2}.',1)
 title='Corpus de ajuste' if es else 'Fine-Tuning Corpus'
 caption='Sistema ViRbot para operar robots de servicio.' if es else 'ViRbot system to operate service robots.'
 fig=r'''\begin{figure}[htbp]
\centering
\includegraphics[width=0.9\columnwidth]{figures/virbot_general.pdf}
\caption{'''+caption+r'''}
\label{fig:virbot_general}
\end{figure}

'''
 s=s.replace('\\subsection{'+title+'}',fig+'\\subsection{'+title+'}',1)
 opening='La implementación se integra en la arquitectura ViRBot de Justina.' if es else 'The implementation is integrated into the ViRBot architecture of Justina.'
 newopening=opening.replace('ViRBot','ViRbot')
 caption='Sistema ViRbot implementado mediante ROS-2.' if es else 'ViRbot system implemented using ROS-2.'
 fig=r'''

\begin{figure}[htbp]
\centering
\includegraphics[width=0.9\columnwidth]{figures/virbot_ros2.pdf}
\caption{'''+caption+r'''}
\label{fig:virbot_ros2}
\end{figure}

'''
 assert opening in s;s=s.replace(opening,newopening+fig,1)
 a=s.index('\\begin{figure*}');b=s.index('\\end{figure*}',a)+len('\\end{figure*}')
 block=s[a:b];assert '\\label{fig:arquitecturas}' in block;s=s[:a]+s[b:]
 a=s.index('\\label{fig:virbot_ros2}');a=s.index('\\end{figure}',a)+len('\\end{figure}')
 s=s[:a]+'\n\n'+block+s[a:]
 a=s.index('\\label{tab:resultados_g}');b=s.index('\\end{table*}',a)
 t=s[a:b].replace('lrrrrr','lrrrr').replace(' & No verificable','').replace(' & Not verifiable','')
 for x,y in [('220 & 10 & 0 & 10','220 & 10 & 10'),('215 & 15 & 0 & 10','215 & 15 & 10'),('216 & 14 & 0 & 8','216 & 14 & 8')]:assert x in t;t=t.replace(x,y)
 s=s[:a]+t+s[b:]
 old='Latencia total en G, 230 ejecuciones por sistema. Cuartiles descriptivos, sin asumir independencia.' if es else 'Total latency in G, 230 runs per system. Descriptive quartiles without assuming independence.'
 new='Latencia total en G, 230 ejecuciones por sistema. Q25--Q75 contiene el 50\\,\\% central de los tiempos. Cuartiles descriptivos, sin asumir independencia.' if es else 'Total latency in G, 230 runs per system. Q25--Q75 contains the central 50\\,\\% of response times. Descriptive quartiles without assuming independence.'
 assert old in s;s=s.replace(old,new)
 (dst/'articulo.tex').write_text(s)
(P/'trazabilidad.json').write_text(json.dumps(trace,ensure_ascii=False,indent=2)+'\n')
print('Versiones preparadas con las figuras originales del tutor y las tres correcciones acordadas.')
