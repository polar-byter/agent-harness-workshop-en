# Return tool results to the model

The previous function finds notes, but the model has not received those results yet. Sending only the original task again would omit the information just collected. We will save the command with its result and include that history in the next decision request.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-03-02-cycle.zip), choose **Extract All**, and open the extracted `lesson-03-02-cycle` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `agent.py` -> `run_agent`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder. The main run uses the connection saved in the [required connection lesson](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/04-connect.md). The offline `demo_check.py` remains a separate code check.

## Follow the data

Initially `events = []`. After a tool call, the program appends `{'command': command, 'result': result}`. The next `decide(task, events)` receives the same task and this updated list. In a real run, `decide_live` includes it in messages sent to the model.

The illustration follows one possible two-request route: search, then an answer using two found lines. A real model may choose another sequence. The offline `decide_fixture` merely checks whether history is nonempty and returns a prepared answer; it does not analyze the note contents.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def run_agent(task: str, notes_path: Path, decide, max_steps: int = 4) -> dict:
    if max_steps < 1:
        raise ValueError('At least one step is required')
    events = []
    for step in range(max_steps):
        command = decide(task, events)
        if command.get('type') == 'answer':
            text = command.get('text')
            if not isinstance(text, str) or not text.strip():
                raise ValueError('Empty answer')
            return {'status': 'completed', 'answer': text, 'events': events}
        if command.get('type') != 'tool':
            raise ValueError('Expected an answer or a tool request')
        result = ...
        events.append({'command': ..., 'result': ...})
    return {'status': 'step_limit', 'answer': '', 'events': events}
```

For a tool command, compute `result = dispatch_tool(command, notes_path)` and append the command and result to `events`. Let the loop make another decision request. For an answer command, validate the text and return the completed result immediately.

`range(max_steps)` limits decision requests. When it ends without an answer, return `'step_limit'`. A `return` inside the answer branch exits the whole function; the return after the loop handles exhaustion. Do not add a tool event for a final answer.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-03-02-cycle**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py` and inspect the events before the final result. You should be able to connect a model request, the executed search and the data sent back. Use `demo_check.py` separately to verify the call order with a prepared decision function.

This repeating exchange is the agent loop. Its orchestration is our Python code: the model chooses a requested next action, while the program decides when to call, execute, record and stop.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
