"""Exporta el protocolo a HTML, DOCX y PDF; requiere markdown y LibreOffice."""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile
import markdown

base = Path(__file__).resolve().parent
source = base / 'Protocolo_experimento_final_tesis.md'
out = base / 'exportaciones'
out.mkdir(exist_ok=True)
body = markdown.markdown(source.read_text(), extensions=['tables', 'sane_lists'])
html = out / (source.stem + '.html')
html.write_text('''<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<title>Protocolo del experimento final de tesis</title>
<style>
@page { size: A4; margin: 2cm; }
body { font-family: "Liberation Sans", Arial, sans-serif; font-size: 10pt; line-height: 1.25; color: #202b35; }
h1 { font-size: 22pt; color: #174566; }
h2 { font-size: 15pt; color: #174566; margin-top: 22pt; }
h3 { font-size: 12pt; margin-top: 16pt; }
h1,h2,h3 { page-break-after: avoid; }
table { width: 100%; border-collapse: collapse; font-size: 9pt; margin: 10pt 0; }
th { background: #e5eef5; text-align: left; }
td,th { border: 1px solid #bcc9d2; padding: 5pt; vertical-align: top; }
tr { page-break-inside: avoid; }
code { font-family: "Liberation Mono", monospace; font-size: 9pt; }
p,li { orphans: 2; widows: 2; }
</style></head><body>''' + body + '</body></html>\n')
with tempfile.TemporaryDirectory(prefix='lo-protocolo-') as profile:
    for fmt in ['docx:Office Open XML Text', 'pdf:writer_pdf_Export']:
        subprocess.run(['libreoffice', '-env:UserInstallation='+Path(profile).as_uri(),
                        '--headless', '--convert-to', fmt, '--outdir', str(out), str(html)],
                       check=True, timeout=120)
files=[source,html,out/(source.stem+'.docx'),out/(source.stem+'.pdf')]
for f in files:
    assert f.is_file() and f.stat().st_size > 100, f
manifest={'version':'0.1','date':'2026-10-27','status':'propuesta pendiente de aprobación',
          'files':{str(f.relative_to(base)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
(out/'Protocolo_experimento_final_tesis_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Exportaciones verificadas:', ', '.join(f.suffix for f in files))
