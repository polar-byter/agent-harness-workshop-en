"""Check the current function without a model request."""
import json
from io import BytesIO
from unittest.mock import patch
from decisions import build_decision_messages, parse_decision


def main():
    print('Offline exercise check.')
    try:
        from decisions import decide_live
        from transport import course_response
        text = '{"type":"tool","tool":"find_notes","query":"python"}'
        with patch('decisions.send_live', return_value=course_response(text)):
            print(decide_live('Find notes about Python', []))
    except NotImplementedError as error:
        print(error)


if __name__ == '__main__':
    main()
