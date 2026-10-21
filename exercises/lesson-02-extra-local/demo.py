from pathlib import Path
from assistant import build_messages, extract_answer
from local_model import send_local
from local_runtime import load_model

ROOT = Path(__file__).resolve().parent


def main():
    question = 'What do the notes say about Python?'
    notes = ['Python lists keep item order.']
    print('Question:', question)
    print('Notes:', notes)
    try:
        # Check the exercise before loading the model or installing its library.
        from demo_check import check_exercise
        check_exercise()
        print('Loading model from file...')
        with load_model(ROOT / 'models/Qwen3-0.6B-Q8_0.gguf') as model:
            messages = build_messages(question, notes)
            response = send_local(model, messages)
            print('Model answer:', extract_answer(response))
    except (NotImplementedError, FileNotFoundError, ModuleNotFoundError, ValueError) as error:
        print(error)


if __name__ == '__main__':
    main()
