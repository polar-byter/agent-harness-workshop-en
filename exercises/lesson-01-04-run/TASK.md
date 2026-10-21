# Connect reading, search and the journal

> **Where we are.** The assistant has three separate functions: reading notes, searching and writing the journal. We combine them into one operation that an agent can call later.
> `[file -> reading -> search -> journal]` -> result

Right now, finding notes means calling three functions in the right order. In section 3 the agent will need a single "search" command, after which the program does the rest. We also add a status to the result: `found` when there are matches and `not_found` when there are none, so the outcome is visible without reading the list.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-01-04-run.zip), extract it and open the `lesson-01-04-run` folder in PyCharm. The current task is `run_search` in `app.py`.

## Look at the data

`demo.py` passes three values: the path to `data/notes.txt`, the query `' Python '` and the path to the journal `runs.jsonl`. The function returns a dictionary with the query, the status and the found notes. The status takes one line:

```python
status = 'found' if matches else 'not_found'
```

A non-empty `matches` list gives `'found'`, an empty one gives `'not_found'`.

**Guess before running:** which of the six notes in `data/notes.txt` will the query "Python" find?

## Your turn

In `run_search`, the notes are already read and the matches found. Replace `raise NotImplementedError(...)` with the code below and fill in the gaps:

```python
def run_search(notes_path: Path, query: str, journal_path: Path) -> dict:
    notes = read_notes(notes_path)
    matches = find_notes(notes, query)
    status = 'found' if matches else 'not_found'
    result = {
        'query': ...,
        'status': ...,
        'matches': ...,
    }
    write_result(..., ...)
    return result
```

1. `'query'` gets the query without surrounding spaces: `query.strip()`.
2. `'status'` and `'matches'` get the variables `status` and `matches`.
3. `write_result` takes the journal path `journal_path` first and then `result`.

The journal is written after reading and searching on purpose: if the file is missing, the function stops earlier and the journal does not get a record of a search that never happened.

## Run it

Open `demo.py` and choose **Run 'demo'**. The Run window shows:

```text
{'query': 'Python', 'status': 'found', 'matches': ['Python functions return values.', 'Python lists keep item order.']}
```

Compare it with the last line of `runs.jsonl`: they hold the same data.

## Try to break it

1. Change the query in `demo.py` to `'database'`. The status becomes `not_found`, the list is empty, and the journal still gets a record: the search ran and found nothing.
2. Change the notes path to `ROOT / 'data' / 'missing.txt'`. The program stops with `FileNotFoundError` and nothing is written to the journal.

In `runs.jsonl` the failed search left a trace and the missing file did not. Put the original values back.

## What we have now

Section 1 is done: the assistant has a "search the notes" operation that reads the source, searches, records the result and reports a status. To run the prepared checks, open `tests/test_lesson.py` and run `class LessonTests`.

Next section: [send a question with its source notes](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/01-messages.md) to a model. Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
