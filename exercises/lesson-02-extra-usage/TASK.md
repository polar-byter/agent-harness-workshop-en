# Inspect request statistics

A real answer raises practical questions: how large was the request, how much text was generated and which values did the provider actually report? This optional lesson displays the available statistics without turning missing fields into invented measurements.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-02-extra-usage.zip), choose **Extract All**, and open the extracted `lesson-02-extra-usage` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `model_stats.py` -> `format_usage`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

For the deterministic example, use `{'input_tokens': 10, 'output_tokens': 0, 'cached_tokens': None}`. Zero is a reported value; `None` means no value was supplied. `format_usage` returns a list of readable lines and does not itself measure token counts.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

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

The loop supplies `(label, key)` pairs. On its first iteration, `label` is `'Input tokens'` and `key` is `'input_tokens'`. Use `stats.get(key)` to fetch the value. Append a line containing the value when it is not `None`, and `'not reported'` otherwise. Do not use `if value`, because it would incorrectly treat zero as missing.

Return the list after the loop. The demonstration prints these lines separately. Keep collection, formatting and display as separate operations so you know where each number came from.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-02-extra-usage**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Start with `demo_check.py`, which needs no service. After completing the function, run `demo_usage.py` for the saved live connection and compare the reported fields. Provider-specific fields may be absent. Continue with the short [context and token explanation](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/usage-background.md) before interpreting these statistics.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
