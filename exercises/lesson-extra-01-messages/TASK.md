# Build the decision messages

> **Where we are.** First lesson of the optional workbook. We write the function that assembles the messages for the model before it chooses its next action.
> `task + history -> [messages] -> model -> command`

A user asks about Python. The model has to decide what to do: search the notes, read them all or answer right away. The user's words alone are not enough for that. The program has to tell the model which actions exist, how to ask for them and what has already been done. If the result of the last search is not in the messages, the model does not know about it. If the tool names are not explained, the model may ask for something the program does not have.

`build_decision_messages` assembles these messages. You will see exactly what the model is about to receive: the rules, the task and the history. When an agent behaves oddly, this content is the first thing to check.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-extra-01-messages.zip), extract it and open the `lesson-extra-01-messages` folder in PyCharm. In `decisions.py`, `build_decision_messages` is paused at a placeholder. No model is needed in this lesson.

## Look at the data

Start with the first request, before any search:

```python
task = 'Find notes about Python'
events = []
```

`task` is the request, `events` the history of actions taken, still empty. The function returns two messages: the rules with role `'developer'` and the task with its data with role `'user'`. The rules are already in the `RULES` variable at the top of `decisions.py`, including an example of how to ask for a search:

```json
{"type":"tool","tool":"find_notes","query":"word"}
```

`type: "tool"` means a request for an action, `tool` names the search function and `query` holds the search text. This is how the program tells the model what form of command it expects; whether the model follows it shows only in its reply.

The task and history are turned into a JSON string before sending:

```python
content = json.dumps({'task': task, 'events': events}, ensure_ascii=False)
```

## Your turn

Replace the placeholder in `build_decision_messages` with the code below and fill in the three gaps:

```python
def build_decision_messages(task: str, events: list[dict]) -> list[dict]:
    rules = RULES
    content = ...
    return [
        {'role': 'developer', 'content': ...},
        {'role': 'user', 'content': ...},
    ]
```

1. `content` gets the `json.dumps` call shown above.
2. The `'developer'` message gets `rules`.
3. The `'user'` message gets `content`.

The function returns the list of two messages. Sending them comes in the last lesson, through `send_live`, where the `'developer'` role becomes `'system'` as in the main course.

## Run it

Open `demo_check.py` and choose **Run**. The Run window shows the rules and the task with an empty `events` list. To run the prepared checks, open `tests/test_lesson.py` and choose **Run**.

`demo_check.py` also makes a second call: the program has run a search and is asking the model again. The task is the same, and the history now has an entry saying which tool ran and what it returned:

```python
events = [{'tool': 'find_notes', 'result': ['Python lists keep item order.']}]
```

The program writes that entry after the search; the model does not create it. Compare the two `'user'` messages in the output: in the second, the model would receive the found note together with the task, while the rules stay the same.

Next: [parse a command from model text](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/extra-prepared-modules/02-command.md). Back to [the workbook](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/extra-prepared-modules/README.md).
