import json
from assistant import extract_answer
from transport import send_live


def propose_fixture(task, old_text):
    return 'def total_price(price, quantity):\n    return price * quantity\n'


def propose_live(task, old_text):
    response = send_live([
        {'role': 'developer', 'content': 'Return only JSON with new_text containing the complete corrected prices.py. '
         'Keep the function name and parameters. Do not add external actions.'},
        {'role': 'user', 'content': json.dumps({'task': task, 'file': old_text}, ensure_ascii=False)},
    ])
    text = extract_answer(response)
    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        raise ValueError('The model returned text instead of a JSON proposal: ' + text[:400]) from None
    if not isinstance(result, dict) or not isinstance(result.get('new_text'), str):
        raise ValueError('Missing corrected file text')
    return result['new_text']
