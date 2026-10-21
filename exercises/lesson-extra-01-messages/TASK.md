# Build the decision messages

Return to our note assistant after a pause: a person asks it to find Python notes, the model selects a tool, and the application executes that tool. The main course already provided `decide_live`. Here we rebuild the messages it needs so the path from task to model input is explicit.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-extra-01-messages.zip), choose **Extract All**, and open the extracted `lesson-extra-01-messages` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `decisions.py` -> `build_decision_messages`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

The function receives `task='Find notes about Python'` and an `events` list. The supplied `RULES` string describes the permitted JSON decisions. We serialize the task and history into the user message; the rules occupy a separate developer message.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def build_decision_messages(task: str, events: list[dict]) -> list[dict]:
    rules = RULES
    content = ...
    return [
        {'role': 'developer', 'content': ...},
        {'role': 'user', 'content': ...},
    ]
```

Build `{'task': task, 'events': events}`, serialize it using `json.dumps(..., ensure_ascii=False)`, and return a message list with the prepared rules followed by the serialized data. Keep the original event values; do not replace them with a summary.

The JSON text is the content of a message. It is not the tool command the model will later return. This function only prepares data and can be tested without any model or network service.

## Run and inspect

Open `demo_check.py` directly under **Project -> lesson-extra-01-messages**, right-click in its editor and choose **Run 'demo_check'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo_check.py`, which prints the two messages. Repeat with one prepared event and verify that its result appears in the serialized user content. The lesson's small event example illustrates message construction; the main loop stores each real event as a command-result pair.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
