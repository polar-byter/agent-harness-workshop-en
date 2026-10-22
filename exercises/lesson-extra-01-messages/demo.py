"""Check the current function without a model request."""
import json
from io import BytesIO
from unittest.mock import patch
from decisions import build_decision_messages, parse_decision


def main():
    print('Offline exercise check.')
    try:
        for events in ([], [{'tool': 'find_notes', 'result': ['Returns are accepted within 14 days.']}]):
            messages = build_decision_messages('Find the return clauses in the policy', events)
            for message in messages:
                print(message['role'] + ': ' + message['content'])
    except NotImplementedError as error:
        print(error)


if __name__ == '__main__':
    main()
