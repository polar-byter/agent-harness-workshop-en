# Assemble decide_live

> **Where we are.** Last lesson of the optional workbook. All the parts are ready: messages, sending, parsing. We assemble the function that the main course provided ready-made.
> `task + history -> [messages -> send_live -> text -> command]`

To learn the agent's next step, the program passes the model the rules, the task and the results of earlier actions, receives the reply and reads a command from it. Whether to carry the command out is decided by another part of the program.

We join these actions in `decide_live` in `decisions.py`: `build_decision_messages` prepares the messages, `send_live` gets the response, `extract_answer` takes out the text and `parse_decision` the command dictionary. `decide_live` itself makes one request for a decision; it does not search and does not loop. With the whole stretch in front of you, it is easy to check what went to the model, what came back and at which stage something failed.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-extra-04-decision.zip), extract it and open the `lesson-extra-04-decision` folder in PyCharm. In `decisions.py`, `decide_live` is paused; `build_decision_messages`, `parse_decision`, `extract_answer` and all of `transport.py` are ready. A real request needs the connection from [lesson 2.4](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/04-connect.md).

## Look at the data

In `demo_check.py` the task "Find notes about Python" goes in with an empty history: the first request, before any search. Instead of a model, the offline check returns a prepared response containing the command text:

```json
{"type":"tool","tool":"find_notes","query":"python"}
```

`send_live` brings every service's response into the course format; for our example it looks like this:

```python
response = {'status': 'completed', 'output': [
    {'type': 'message', 'content': [
        {'type': 'output_text',
         'text': '{"type":"tool","tool":"find_notes","query":"python"}'}
    ]}
]}
```

The outer dictionary describes the finished service response; the `text` field holds the model's command. `extract_answer` takes out that string, `parse_decision` turns it into a dictionary, and the caller gets `{'type': 'tool', 'tool': 'find_notes', 'query': 'python'}`: a command, not a description of the service response.

## Your turn

Replace the placeholder in `decide_live` with the code below and fill in four gaps:

```python
def decide_live(task: str, events: list[dict]) -> dict:
    messages = ...
    response = ...
    text = ...
    return ...
```

1. `messages` is the result of `build_decision_messages(task, events)`.
2. `response` is the result of `send_live(messages)`.
3. `text` is the result of `extract_answer(response)`.
4. Return `parse_decision(text)`.

The variable names keep the stages apart: `messages` is the list before the request, `response` the dictionary in the common format, `text` the JSON string inside it. Only the last line produces a command dictionary.

## Run it

Open `demo_check.py` and choose **Run**. The Run window shows the dictionary with the query "python". To run the prepared checks, run `tests/test_lesson.py`.

Then run `demo.py`. It prints the chosen model and the task (never the API key) and makes a real request. The model may choose `find_notes`, `read_notes` or answer straight away. If it replies with prose instead of JSON, the check in `parse_decision` fires. Valid JSON still does not mean the action was well chosen; that shows only in the command itself.

The demonstration prints the dictionary and carries nothing out. In the main course the dictionary goes on to `dispatch_tool`, which checks the tool name and runs a permitted action. The path to the notes file is set by the program; the model's command does not contain it.

## Where the agent loop continues

After a tool runs, `run_agent` adds the result to `events` and calls `decide_live` again with the same task. The function rebuilds the messages, so the model receives the extended history and decides whether it needs another tool or can answer. `decide_live` makes one request for a decision; repeating the steps is the job of `run_agent`.

Open `decisions.py` in the starter of the [main tool lesson](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/03-tool-agent/01-tools.md). There the same operations sit in one function: rules and messages, `send_live`, `extract_answer`, `json.loads` and the dictionary check. Compare them with your four lines. Back to [the workbook](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/extra-prepared-modules/README.md) or [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
