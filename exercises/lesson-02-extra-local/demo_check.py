from assistant import build_messages, extract_answer
from local_model import send_local


class ExampleModel:
    def __init__(self):
        self.calls = []

    def create_chat_completion(self, **settings):
        self.calls.append(settings)
        return {'choices': [{'finish_reason': 'stop', 'message': {
            'content': 'You can return an item within 14 days.'
        }}]}


def check_exercise():
    model = ExampleModel()
    messages = build_messages('How many days do I have to return an item?', ['Returns are accepted within 14 days.'])
    response = send_local(model, messages)
    assert len(model.calls) == 1, 'Expected one model call'
    settings = model.calls[0]
    assert settings['messages'][0]['role'] == 'system', 'Pass prepared'
    assert settings['max_tokens'] == 256, 'Keep the lesson token limit'
    assert messages[0]['role'] == 'developer', 'Leave the original messages unchanged'
    assert extract_answer(response) == 'You can return an item within 14 days.'
    return extract_answer(response)


def main():
    try:
        print('Offline exercise check:', check_exercise())
    except NotImplementedError as error:
        print(error)


if __name__ == '__main__':
    main()
