import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent


def send_fixture(messages: list[dict]) -> dict:
    """Read a prepared response file without calling a model."""
    return json.loads((ROOT / 'data' / 'response.json').read_text(encoding='utf-8'))


def send_live(messages: list[dict]) -> dict:
    key = os.environ.get('OPENAI_API_KEY')
    model = os.environ.get('OPENAI_MODEL')
    if not key or not model:
        raise ValueError('Set OPENAI_API_KEY and OPENAI_MODEL in the run configuration')
    payload = {'model': model, 'input': messages, 'max_output_tokens': 1200}
    request = Request('https://api.openai.com/v1/responses',
        data=json.dumps(payload).encode('utf-8'),
        headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'},
        method='POST')
    with urlopen(request, timeout=40) as response:
        return json.loads(response.read().decode('utf-8'))
