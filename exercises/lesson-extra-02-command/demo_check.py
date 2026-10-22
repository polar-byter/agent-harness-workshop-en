"""Check the current function without a model request."""
import json
from io import BytesIO
from unittest.mock import patch
from decisions import build_decision_messages, parse_decision


def main():
    print('Offline exercise check.')
    try:
        text = '{"type":"tool","tool":"find_notes","query":"return"}'
        print('Before parsing:', type(text))
        decision = parse_decision(text)
        print('After parsing:', type(decision))
        print('Command:', decision)
        print('Tool:', decision['tool'])
        print('Query:', decision['query'])
        for text in ('I will search now', '[]'):
            try:
                parse_decision(text)
            except ValueError as error:
                print(error)
    except NotImplementedError as error:
        print(error)


if __name__ == '__main__':
    main()
