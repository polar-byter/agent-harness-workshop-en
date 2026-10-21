"""Try the completed request function with a real model."""
from assistant import answer_question
from transport import send_live


def main():
    try:
        answer = answer_question('What do the notes say about Python?',
                                 ['Python lists keep item order.'], send_live)
    except (NotImplementedError, ValueError) as error:
        print(error)
    else:
        print(answer)


if __name__ == '__main__':
    main()
