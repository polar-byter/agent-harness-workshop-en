import json
import hashlib
from pathlib import Path
from notes import find_notes, find_notes_alt, read_notes
from assistant import build_messages, extract_answer, answer_question
from transport import send_fixture
from transport import send_live

ROOT = Path(__file__).resolve().parent


def main():
    print('Network model request using OPENAI_API_KEY and OPENAI_MODEL.')
    try:
        result = answer_question('What do the notes say about Python?', ['Python lists keep item order.'], send_live)
    except NotImplementedError as error:
        print(error)
    else:
        print(result)

if __name__ == "__main__":
    main()
