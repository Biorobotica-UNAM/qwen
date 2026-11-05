"""Lectura de resultados históricos, sin consultas ni cambios en la campaña."""
from pathlib import Path

from .common import digest, read_json, read_jsonl


def visible(value):
    """Evita que una salida de modelo ejecute secuencias de control en terminal."""
    return ''.join(c if c.isprintable() else repr(c)[1:-1] for c in str(value))


def view_campaign(directory, case_ids=None, conditions=None, attempts='all'):
    directory = Path(directory).resolve()
    if digest(directory/'manifest.json') != (directory/'manifest.sha256').read_text().strip():
        raise ValueError('El manifiesto cambió; revisar la campaña antes de mostrarla')
    manifest = read_json(directory/'manifest.json')
    output = (directory/manifest['output_path']).resolve()
    if not output.is_relative_to(directory):
        raise ValueError('La salida debe estar dentro de la campaña')
    rows = read_jsonl(output)
    known = {r['run_id'] for r in rows}
    for event in read_jsonl(directory/'journal.jsonl'):
        if event['event'] == 'started' and event['run_id'] not in known:
            row = dict(event['record'])
            row['execution_status'] = 'sin resultado final (en curso o interrumpido)'
            rows.append(row)
            known.add(row['run_id'])
    if any(r['campaign_id'] != manifest['campaign_id'] for r in rows):
        raise ValueError('Hay registros de otra campaña')
    configs = {c['config_id']: c for c in manifest['configs']}
    def label(row):
        config = configs[row['config_id']]
        return config.get('label', config['architecture'])
    if case_ids:
        inputs = read_jsonl(directory/manifest['inputs']['path'])
        if set(case_ids)-{r['id'] for r in inputs}:
            raise ValueError('ID de caso desconocido')
        rows = [r for r in rows if r['case_id'] in case_ids]
    if conditions:
        if set(conditions)-{c.get('label', c['architecture']) for c in configs.values()}:
            raise ValueError('Condición desconocida')
        rows = [r for r in rows if label(r) in conditions]
    if attempts != 'all':
        selected = {}
        for row in rows:
            key = (row['case_id'], row['config_id'], row['repetition'])
            old = selected.get(key)
            if old is None or (row['attempt'] < old['attempt'] if attempts == 'first'
                               else row['attempt'] > old['attempt']):
                selected[key] = row
        rows = list(selected.values())
    rows.sort(key=lambda r: (r['case_id'], label(r), r['repetition'], r['attempt']))
    lines = [f"Campaña: {manifest['campaign_id']}",
             f"Vista: {attempts} | Registros: {len(rows)}",
             'Lectura histórica; no certifica reproducibilidad ni corrección semántica.']
    for row in rows:
        config = configs[row['config_id']]
        model = config.get('model') or config.get('qwen', {}).get('base_model')
        lines += ['', '='*72,
                  f"{row['case_id']} | {label(row)} | repetición {row['repetition']} | intento {row['attempt']}",
                  f"run_id: {row['run_id']}",
                  f"Orden: {row['input_original']}",
                  f"Estado: {row['execution_status']} | Respuesta: {row.get('response_kind') or 'no disponible'}"]
        if model:
            lines.append(f'Modelo: {model}')
        if row.get('message'):
            lines.append(f"Mensaje: {row['message']}")
        if row.get('error'):
            error = row['error']
            lines.append(f"Error: {error.get('type')} ({error.get('stage')}): {error.get('message')}")
        goals = row.get('goals_pred')
        title = 'Objetivos'
        if row['architecture'] == 'reference_clips':
            goals = (row.get('reference_clips') or {}).get('goals_reference_input')
            title = 'Objetivos de referencia'
        lines.append(title+':')
        lines.extend(f'  {i}. {goal}' for i, goal in enumerate(goals or [], 1))
        if not goals:
            lines.append('  (vacíos)' if goals == [] else '  (no disponibles)')
        lines.append('Plan guardado (orden original):')
        for step in row.get('plan') or []:
            lines.append(f"  {step.get('step')}: {step.get('robot')} | {step.get('action')} | {step.get('params')}")
        if not row.get('plan'):
            lines.append('  (sin plan)')
        total = (row.get('timing') or {}).get('total_ms')
        lines.append(f'Tiempo total: {total/1000:.3f} s' if total is not None else 'Tiempo total: no disponible')
        flags = {True:'válido', False:'inválido', None:'no evaluado'}
        validation = row.get('validation') or {}
        lines.append('Formato: '+', '.join(f'{name}={flags[validation.get(key)]}' for name, key in
                     [('respuesta','response_schema_valid'), ('goals','goals_schema_valid'), ('plan','plan_contract_valid')]))
        if row['architecture'] == 'gpt_direct':
            lines.append('Recursos internos GPT: no disponibles')
    if not rows:
        lines.append('Sin resultados para esta selección.')
    return '\n'.join(visible(line) for line in lines)
