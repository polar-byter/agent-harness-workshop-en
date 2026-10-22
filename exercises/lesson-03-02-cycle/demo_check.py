import json
import hashlib
from pathlib import Path
from notes import find_notes, find_notes_alt, read_notes
from assistant import build_messages, extract_answer, answer_question
from transport import send_fixture
from agent import dispatch_tool, run_agent, decide_fixture

ROOT = Path(__file__).resolve().parent


def main():
    print('Exercise run without a network model call.')
    try:
        result = run_agent('Find the return clauses in the policy', ROOT / 'data' / 'notes.txt', decide_fixture)
    except NotImplementedError as error:
        print(error)
    else:
        print(result)


if __name__ == '__main__':
    main()
