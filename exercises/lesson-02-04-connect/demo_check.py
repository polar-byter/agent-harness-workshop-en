import json
import hashlib
from pathlib import Path
from notes import find_notes, find_notes_alt, read_notes
from assistant import build_messages, extract_answer, answer_question
from transport import send_fixture

ROOT = Path(__file__).resolve().parent


def main():
    print('Exercise run without a network model call.')
    try:
        result = answer_question('How many days do I have to return an item?', ['Returns are accepted within 14 days.'], send_fixture)
    except NotImplementedError as error:
        print(error)
    else:
        print(result)


if __name__ == '__main__':
    main()
