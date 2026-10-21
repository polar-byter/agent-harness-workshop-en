from pathlib import Path
from assistant import answer_question
from transport import send_live

ROOT = Path(__file__).resolve().parent


def main():
    question = 'What do the notes say about Python?'
    notes = ['Python lists keep item order.']
    print('Question:', question)
    print('Notes:', notes)
    answer = answer_question(question, notes, send_live)
    print('Model answer:', answer)


if __name__ == "__main__":
    main()
