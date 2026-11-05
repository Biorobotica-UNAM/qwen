from pathlib import Path
import hashlib,json,re,shutil
P=Path(__file__).resolve().parent;S=Path('/home/sergio/Articulo ingles');D=P/'fuentes'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for f in S.iterdir():
 if f.is_file() and f.suffix in ['.tex','.bib','.cls','.sty','.bst']:shutil.copy2(f,D/f.name)
shutil.copytree(S/'figures',D/'figures',dirs_exist_ok=True)
s=(S/'articulo.tex').read_text()
a=s.index('\\author{%');b=s.index('\n}',a)+2
s=s[:a]+'\\author{}'+s[b:]
s=s.replace('its connection to CLIPS and our service robot, named Justina,','its connection to CLIPS and a service-robot executor,')
old="Justina is the service robot developed at UNAM's college of Engineering Bio-Robotics Laboratory \\cite{Savage2024}."
assert old in s
s=s.replace(old,'The experimental action contract follows a service-robot platform described in prior work \\cite{Savage2024}.')
s=s.replace('Justina','the service robot')
s=s.replace('\\section*{ACKNOWLEDGEMENTS}','')
# Put a non-identifying disclosure in an appropriate section, preserving anonymous review.
# Scientific review provenance already appears in the evaluation section and is retained.
disclosure=r'''\section*{USE OF AI TOOLS}
OpenAI Codex assisted with proposing the experimental protocol and evaluating the results \cite{openai_assistance}. Figures~3--7 were generated programmatically from the implemented architecture and recorded experimental data. The tools also assisted with proposed experimental classifications and semantic reviews, as described in Section~6. ChatGPT and Codex additionally supported language revision, translation, manuscript preparation, and analysis code. The authors take responsibility for the manuscript, its analysis, and the reported results.

'''
s=s.replace('\\bibliographystyle{apalike}',disclosure+'\\bibliographystyle{apalike}')
# Make clear that citations concern writing assistance rather than scientific support.
for title in ['EXPERIMENTAL EVALUATION AND RESULTS']:
 needle='\\section{'+title+'}'
 assert needle in s
 s=s.replace(needle,needle+r'\footnote{Codex assisted with the experimental proposal and evaluation using OpenAI tools \cite{openai_assistance}; see the disclosure at the end of the paper.}',1)
(D/'articulo.tex').write_text(s)
p=D/'references.bib'
p.write_text(p.read_text()+r'''
@misc{openai_assistance,
 author = {{OpenAI}},
 title = {{ChatGPT and Codex}: tools used for manuscript and code assistance},
 year = {2026},
 howpublished = {\url{https://openai.com/}},
 note = {Accessed October 2026. Tool use is described in the manuscript disclosure}
}
''')
# Plain-text fields, exactly matching the anonymous manuscript.
title=re.search(r'\\title\{([^\n]+)\}',s).group(1).replace('--','–')
abstract=re.search(r'\\abstract\{%\s*(.*?)%\s*\}',s,re.S).group(1)
abstract=abstract.replace('--','–').replace('\\$','$')
keywords=re.search(r'\\keywords\{(.*?)\}',s).group(1)
for name,content in [('TITULO.txt',title),('RESUMEN.txt',abstract),('PALABRAS_CLAVE.txt',keywords)]:
 (P/name).write_text(content+'\n')
(P/'DECLARACION_IA.txt').write_text('OpenAI ChatGPT and Codex assisted with drafting, translation, editing, LaTeX, analysis code, programmatic figures, and proposed experimental classifications and semantic reviews. The manuscript identifies the affected sections and figures, retains the provenance of automated judgments, and distinguishes them from explicit acceptance decisions. The authors take responsibility for the manuscript and reported results.\n')
(P/'autores.csv').write_text('orden,nombre,afiliacion,pais,email\n1,Sergio Cano,"Bio-Robotics Laboratory, College of Engineering, National Autonomous University of Mexico",Mexico,sergio081096@gmail.com\n2,Jesus Savage,"Bio-Robotics Laboratory, College of Engineering, National Autonomous University of Mexico",Mexico,robotssavage@gmail.com\n3,Marco Negrete,"Bio-Robotics Laboratory, College of Engineering, National Autonomous University of Mexico",Mexico,PENDIENTE\n4,Mauricio Matamoros,"Bio-Robotics Laboratory, College of Engineering, National Autonomous University of Mexico",Mexico,PENDIENTE\n5,Angel Contreras,"Advance Intelligence and Robotics Research Center, Tamagawa University",Japan,PENDIENTE\n')
(P/'procedencia.json').write_text(json.dumps({'date':'2026-10-29','source_tex_sha256':sha(S/'articulo.tex'),'source_pdf_sha256':sha(S/'articulo.pdf'),'source_folder':str(S),'model_verified':{'requested_model':'gpt-5.6-terra','returned_model':'gpt-5.6-terra','evidence':'reports/experiments/gpt_piloto_60_01/resultados.jsonl'},'anonymization':'Removed author block, institution attribution, ownership of platform, empty acknowledgements. Prior published references retained in third person. Non-identifying AI disclosure placed separately due to conflicting conference instructions.'},ensure_ascii=False,indent=2)+'\n')
print('Fuentes anónimas y campos de formulario preparados.')
