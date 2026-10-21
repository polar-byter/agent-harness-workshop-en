from model_stats import format_usage


def main():
    try:
        lines = format_usage({'input_tokens': 10, 'output_tokens': 0, 'cached_tokens': None})
    except NotImplementedError as error:
        print(error)
    else:
        assert lines == ['Input tokens: 10', 'Output tokens: 0', 'Cached tokens: not reported'], lines
        print('Offline format check passed.')
        for line in lines:
            print(line)


if __name__ == '__main__':
    main()
