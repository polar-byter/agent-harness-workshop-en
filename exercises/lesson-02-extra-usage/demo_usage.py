from model_stats import format_usage
from usage_client import request_sample


def main():
    question = 'What do the notes say about Python?'
    notes = ['Python lists keep item order.']
    try:
        # Check the exercise before contacting a model.
        format_usage({'input_tokens': 10, 'output_tokens': 0, 'cached_tokens': None})
        answer, stats = request_sample(question, notes)
        print('Model answer:', answer)
        for line in format_usage(stats):
            print(line)
        print(f'Request time: {stats["elapsed_seconds"]:.2f} s')
        if stats['requested_context_tokens'] is not None:
            print('Requested num_ctx:', stats['requested_context_tokens'])
        speed = stats['output_tokens_per_second']
        if speed is not None:
            print(f'Generation reported by Ollama: {speed:.1f} tokens/s')
    except (NotImplementedError, ValueError) as error:
        print(error)


if __name__ == '__main__':
    main()
