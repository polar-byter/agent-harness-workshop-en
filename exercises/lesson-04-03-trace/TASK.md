# Save the execution history

A final answer alone does not reveal which tools ran or what they returned. We will save the event list so a later reader can reconstruct the visible actions leading to that answer.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-04-03-trace.zip), choose **Extract All**, and open the extracted `lesson-04-03-trace` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `control.py` -> `save_events`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder. The main run uses the connection saved in the [required connection lesson](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/04-connect.md). The offline `demo_check.py` remains a separate code check.

## Follow the data

Each event pairs a `command` with its `result`. For example, a read command can be paired with `{'notes': ['Python lists']}`. Each event becomes a separate JSONL line in `trace.jsonl`.

Unlike the earlier search journal, this function writes a complete current history using mode `'w'`. Running it again replaces the previous file.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def save_events(path: Path, events: list[dict]) -> None:
    serialized = [json.dumps(event, ensure_ascii=False) for event in events]
    with path.open('w', encoding='utf-8') as stream:
        for text in serialized:
            stream.write(...)
```

Use `with path.open('w', encoding='utf-8') as stream`. Loop over `events`, serialize each event with `json.dumps(event, ensure_ascii=False)`, and write it with a trailing newline.

Keep the command and result in the same record. Do not reduce the record to a human summary that loses the exact values needed for diagnosis. The function returns `None`; the saved file is its effect.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-04-03-trace**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py` and open the generated history file. Check that each saved event corresponds to a visible command and result. This is a small form of action tracing, not distributed tracing and not access to the model's internal reasoning. Logs may contain source data, so decide what belongs in a working log before using the approach on real documents.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
