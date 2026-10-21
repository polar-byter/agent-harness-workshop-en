# Save the execution history

> **Where we are.** The agent works in a limited loop, and the program chooses which part of the history the model sees. Now we save the full history to a file, so runs can be investigated after they finish.
> `agent loop -> history -> [file]`

The assistant stopped, and the final message does not say what happened before. Did it miss the right note? Repeat the search several times? Pick the wrong tool? To find out, you need the commands and their results in the order they happened. Without that, investigating a complaint comes down to guesswork. With it, you can show a colleague or a vendor a specific line: this is what the agent asked for, and this is what it got.

`save_events` writes the history to a file, one JSON line per event. We save the full history, even if the model saw only part of it at each step: that way you can see both what the program had and what reached the model.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-04-03-trace.zip), extract it and open the `lesson-04-03-trace` folder in PyCharm. The current task is `save_events` in `control.py`.

## Look at the data

The function receives the list of events from a finished run. Each event pairs a command with its result. Here the agent asked to read the notes and got one note back:

```python
event = {'command': {'tool': 'read_notes'},
         'result': {'notes': ['Python lists']}}
json.dumps(event, ensure_ascii=False)
```

Each event becomes a separate JSON line, as in the search journal from lesson 1.3. One difference: this file holds the history of a single run, so we open it in mode `'w'` and replace the previous contents. To keep several runs, give each its own file.

## Your turn

In `save_events` each event is already turned into a JSON string; the list is in `serialized`. Replace `raise NotImplementedError(...)` with the code below and fill in the gap:

```python
    with path.open('w', encoding='utf-8') as stream:
        for text in serialized:
            stream.write(...)
```

As in the first journal, write `text + '\n'`. If there are no events, the loop writes nothing and the file stays empty; no special case is needed.

## Run it with the model

Open `demo.py` and choose **Run 'demo'**. After the agent finishes, the program passes the history to your function, and the Run window shows the result and a message about the history file. Open the file and match each command with its result. This is the history of your own run, so the lines will be your own.

## Check the function on its own

Open `demo_check.py` and choose **Run 'demo_check'**. We expect one line:

```text
{"command": {"tool": "read_notes"}, "result": {"notes": ["Python lists"]}}
```

To run the prepared checks, run `class LessonTests` in `tests/test_lesson.py`.

## Try an investigation

Run `demo.py` again and open the fresh history file. Use it to answer three questions: which tool did the model ask for first, with which query, and how many notes came back? If the model answered, compare its answer with the notes in the log. This is the kind of investigation the MTS case called for. Keep in mind that such a log contains your source data, so decide what belongs in it before using the approach on real documents.

## What we have now

Every run leaves a record of the agent's actions. Reconstructing a run from such records is called **tracing**. Our log is its simplest form: a sequence of commands and results. Tracing platforms such as OpenTelemetry also link operations with IDs and record how long each took.

Next: [compare behavior across scenarios](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/04-run-control/04-evaluation.md). Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
