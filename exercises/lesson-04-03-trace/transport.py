"""Connect course functions to the selected model."""
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def connection_path() -> Path:
    override = os.environ.get('HARNESS_CONNECTION_FILE')
    if override:
        return Path(override)
    folder = Path(os.environ.get('LOCALAPPDATA', Path.home() / '.config'))
    return folder / 'AgentHarnessWorkshopEnglish' / 'connection.json'


def read_connection() -> dict:
    path = connection_path()
    if not path.is_file():
        raise ValueError('No connection configured. Run configure_model.py from the connection lesson.')
    settings = json.loads(path.read_text(encoding='utf-8'))
    if settings.get('provider') not in ('openrouter', 'vsegpt', 'ollama'):
        raise ValueError('Choose OpenRouter, VseGPT or Ollama in configure_model.py')
    if not isinstance(settings.get('model'), str) or not settings['model'].strip():
        raise ValueError('Settings contain no model name')
    if settings['provider'] != 'ollama' and not settings.get('api_key'):
        raise ValueError('This provider requires an API key. Open configure_model.py')
    return settings


def send_fixture(messages: list[dict]) -> dict:
    path = Path(__file__).resolve().parent / 'data' / 'response.json'
    return json.loads(path.read_text(encoding='utf-8'))


def request_json(url: str, payload: dict, api_key: str = '') -> dict:
    headers = {'Content-Type': 'application/json'}
    if api_key:
        headers['Authorization'] = 'Bearer ' + api_key
    request = Request(url, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
                      headers=headers, method='POST')
    try:
        with urlopen(request, timeout=180) as response:
            return json.loads(response.read().decode('utf-8'))
    except HTTPError as error:
        hints = {401: 'Check the API key.', 402: 'Check the balance or trial credits.',
                 403: 'Check model availability for your account and region.',
                 404: 'Check the model name; for Ollama run ollama pull first.',
                 429: 'Rate limit or temporary overload. Try again later.'}
        raise ValueError(f'Provider returned HTTP {error.code}. ' + hints.get(error.code, 'Check the provider status.')) from None
    except (URLError, TimeoutError):
        raise ValueError('No model response. Check that Ollama is running, or check the API connection.') from None


def course_response(text: str) -> dict:
    if not isinstance(text, str) or not text.strip():
        raise ValueError('The model returned no answer text')
    return {'status': 'completed', 'output': [
        {'type': 'message', 'content': [{'type': 'output_text', 'text': text}]}
    ]}


def send_live(messages: list[dict]) -> dict:
    if not isinstance(messages, list):
        raise ValueError('send_live expects a message list, without a dictionary wrapper')
    settings = read_connection()
    # These backends receive developer instructions in a system message.
    prepared = [dict(message, role='system') if message.get('role') == 'developer'
                else dict(message) for message in messages]
    if settings['provider'] == 'ollama':
        response = request_json('http://127.0.0.1:11434/api/chat', {
            'model': settings['model'], 'messages': prepared, 'stream': False,
            'think': False, 'options': {'num_gpu': 0, 'num_ctx': 4096, 'num_predict': 1200},
        })
        if not response.get('done') or response.get('done_reason') != 'stop':
            raise ValueError('The local model did not finish; check prompt size and output limit')
        return course_response(response.get('message', {}).get('content'))
    urls = {'openrouter': 'https://openrouter.ai/api/v1/chat/completions',
            'vsegpt': 'https://api.vsegpt.ru/v1/chat/completions'}
    response = request_json(urls[settings['provider']], {
        'model': settings['model'], 'messages': prepared, 'stream': False, 'max_tokens': 1200,
    }, settings['api_key'])
    choices = response.get('choices', [])
    if not choices or choices[0].get('finish_reason') != 'stop':
        raise ValueError('The provider did not finish the text response; check the model and output limit')
    return course_response(choices[0].get('message', {}).get('content'))
