# Execute a permitted tool request

So far we chose source notes ourselves. Now the model can request an operation. That also gives us a reason to draw a boundary: a model may invent a tool name, but the program should execute only operations we deliberately provide. `dispatch_tool` makes that decision in ordinary Python.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-03-01-tools.zip), choose **Extract All**, and open the extracted `lesson-03-01-tools` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `agent.py` -> `dispatch_tool`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder. The main run uses the connection saved in the [required connection lesson](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/04-connect.md). The offline `demo_check.py` remains a separate code check.

## Follow the data

A possible command is `{'type': 'tool', 'tool': 'find_notes', 'query': 'python'}`. The `tool` field names the requested operation and `query` supplies its search text. The application supplies `notes_path` separately, so the model cannot use this command to choose an arbitrary file.

`decide_live` prepares the request and parses the model text into this dictionary. Parsing JSON does not execute a function. We will implement the next step.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def dispatch_tool(command: dict, notes_path: Path) -> dict:
    name = command.get('tool')
    if name == 'read_notes':
        return {'notes': ...}
    if name == 'find_notes':
        query = command.get('query')
        if not isinstance(query, str):
            raise ValueError('Search requires a string query')
        notes = read_notes(notes_path)
        return {'matches': ...}
    raise ValueError('Unknown tool: ' + str(name))
```

Read `command.get('tool')`. For `'read_notes'`, return `{'notes': read_notes(notes_path)}`. For `'find_notes'`, check that `query` is a string, then call `find_notes(read_notes(notes_path), query)` and return its matches under the key `'matches'`. Raise `ValueError` for any other name.

`dict.get` returns `None` when the key is absent, so an omitted name also reaches the rejection branch. Keep checks before the call rather than accepting any Python name found in model text.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-03-01-tools**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py` with the saved model connection, then use `demo_check.py` for a known command. The search should return the two Python lines from the source. In a separate offline experiment, change the test command tool name to `'delete_notes'`: it must be rejected without deleting anything.

This allowlist is one narrow guardrail: it constrains a particular action. It does not isolate the Python process or make all possible model behavior safe.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
