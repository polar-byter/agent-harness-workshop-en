import sys


def main():
    print('Python:', sys.version.split()[0])
    print('Interpreter:', sys.executable)
    try:
        import llama_cpp
    except (ImportError, OSError) as error:
        print('Library did not load:', error)
        return
    print('Library loaded:', llama_cpp.__version__)


if __name__ == '__main__':
    main()
