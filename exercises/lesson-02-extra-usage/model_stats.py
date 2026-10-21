def format_usage(stats: dict) -> list[str]:
    lines = []
    for label, key in (
        ('Input tokens', 'input_tokens'),
        ('Output tokens', 'output_tokens'),
        ('Cached tokens', 'cached_tokens'),
    ):
        value = stats.get(key)
        # For a missing value, show "not reported". Keep zero as zero.
        raise NotImplementedError('Complete format_usage using the lesson hints and TASK.md')
    return lines
