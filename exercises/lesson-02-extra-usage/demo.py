from pathlib import Path
from assistant import answer_question
from transport import send_live

ROOT = Path(__file__).resolve().parent


def main():
    question = 'How many days do I have to return an item?'
    notes = ['Returns are accepted within 14 days.']
    print('Question:', question)
    print('Notes:', notes)
    answer = answer_question(question, notes, send_live)
    print('Model answer:', answer)


if __name__ == "__main__":
    main()
