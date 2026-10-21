# Inspect request statistics

> **Where we are.** The model now answers questions about the notes. Here we look at how much it processed and how long the request took. This lesson is optional.

How much text did the model receive? How much did it generate? What did the service actually report? These questions matter when a cloud bill is higher than expected or a local assistant has become slow, and they are better discussed with numbers than with impressions. In this lesson we display the values the service reports, without turning a missing value into an invented one.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-02-extra-usage.zip), extract it and open the `lesson-02-extra-usage` folder in PyCharm. The current task is `format_usage` in `model_stats.py`. The starter uses the connection saved in lesson 2.4.

## Look at the data

`format_usage` receives a dictionary of statistics and returns lines for printing. Before the real request, the demonstration checks it on a known example:

```python
{'input_tokens': 10, 'output_tokens': 0, 'cached_tokens': None}
```

Ten must be shown as a number, zero as zero, and `None`, meaning the service sent no value, must be explained in words. A model processes text in small pieces called tokens; the input count covers the rule, question and note, and the output count covers the generated answer.

## Your turn

In `model_stats.py` the pairs of label and key and the start of the loop are ready. For example, `('Input tokens', 'input_tokens')` means the number from `stats['input_tokens']` is printed with the label "Input tokens". Fill in the three gaps inside the loop:

```python
def format_usage(stats: dict) -> list[str]:
    lines = []
    for label, key in (
        ('Input tokens', 'input_tokens'),
        ('Output tokens', 'output_tokens'),
        ('Cached tokens', 'cached_tokens'),
    ):
        value = stats.get(key)
        if ___:
            value = ___
        lines.append(___)
    return lines
```

1. The condition is `value is None`.
2. In that case `value` becomes `'not reported'`.
3. Append the line `f'{label}: {value}'`. The `f` before the quotes lets you insert variable values inside curly braces.

`if not value` would not work here: Python treats zero as false too, and a reported zero is a real result that must not turn into "not reported".

## Run it

Run `demo_check.py` first; it needs no service. Then run `demo_usage.py`. With the function finished, it makes one real request and prints the answer, three token lines and the elapsed time; for Ollama it also prints the requested context size and the generation speed. Each run is a new request, and a cloud service counts it against your quota. Some fields may be missing for some services.

To run the prepared checks, open `tests/test_lesson.py` and run its test class. Before interpreting the numbers, read the short explanation of [tokens, context, attention and caching](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/usage-background.md).

## Try it

Add a second note to the `notes` list in `demo_usage.py`, for example `'Python functions return values.'`, and run again. Compare the number of input tokens with the first run. Then put the list back and run the same request twice in a row, comparing the cache counter and the time.

## What we have now

You can print the real counters of a request and tell a reported zero from a missing value. These numbers become useful once an agent's history starts to grow. The main route continues with [tool requests](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/03-tool-agent/01-tools.md). Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
