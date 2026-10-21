from contextlib import contextmanager
import re
from pathlib import Path


@contextmanager
def load_model(path: Path):
    if not path.is_file():
        raise FileNotFoundError(f'Place the model file here: {path}')
    from llama_cpp import Llama
    model = Llama(
        model_path=str(path), n_ctx=2048, n_gpu_layers=0,
        seed=42, verbose=False,
    )
    try:
        yield model
    finally:
        model.close()


def prepare_messages(messages: list[dict]) -> list[dict]:
    prepared = []
    for message in messages:
        item = dict(message)
        if item['role'] == 'developer':
            item['role'] = 'system'
            # Request a short Qwen answer while preserving the source-only instruction.
            item['content'] += ' Answer briefly in English. /no_think'
        prepared.append(item)
    return prepared


def convert_response(response: dict) -> dict:
    choice = response['choices'][0]
    if choice.get('finish_reason') != 'stop':
        raise ValueError('Generation did not finish: check max_tokens')
    text = choice['message'].get('content')
    if not isinstance(text, str):
        raise ValueError('The model returned no text')
    # Qwen may include a reasoning block before its final answer.
    text = re.sub(r'\A\s*<think>.*?</think>\s*', '', text, flags=re.S).strip()
    if not text:
        raise ValueError('The model returned no final answer')
    return {'status': 'completed', 'output': [
        {'type': 'message', 'content': [{'type': 'output_text', 'text': text}]}
    ]}
