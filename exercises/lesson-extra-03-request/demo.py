"""Try the completed request function with a real model."""
from assistant import answer_question
from transport import send_live


def main():
    try:
        answer = answer_question('How many days do I have to return an item?',
                                 ['Returns are accepted within 14 days.'], send_live)
    except (NotImplementedError, ValueError) as error:
        print(error)
    else:
        print(answer)


if __name__ == '__main__':
    main()
