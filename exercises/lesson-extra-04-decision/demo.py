"""Make a real request using the saved course connection."""
from decisions import decide_live
from transport import read_connection


def main():
    settings = read_connection()
    print('Model:', settings['model'])
    print('Task: Find notes about Python')
    try:
        command = decide_live('Find notes about Python', [])
    except (NotImplementedError, ValueError) as error:
        print(error)
    else:
        print(command)


if __name__ == '__main__':
    main()
