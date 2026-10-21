# Parse a command from model text

> **Where we are.** Second lesson of the optional workbook. The messages for the model are ready; now we read its reply.
> `messages -> model -> [text -> command dictionary] -> dispatch_tool`

The model replied `{"type":"tool","tool":"find_notes","query":"python"}`. We can see it is a request to search. To Python, it is still one string, and the separate values have to be extracted from it.

The model could also reply "I will search now", or send a JSON list instead of an object. The program must not take such a reply for a command and carry on with missing data. So `parse_decision` parses the text, checks that it got a dictionary, and either returns it or reports an error. This is where the model's reply ends and our code's responsibility begins.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-extra-02-command.zip), extract it and open the `lesson-extra-02-command` folder in PyCharm. In `decisions.py`, `parse_decision` is paused at a placeholder; `build_decision_messages` from the previous lesson is ready. No model is needed.

## Look at the data

`demo_check.py` uses this reply:

```python
text = '{"type":"tool","tool":"find_notes","query":"python"}'
```

We see the words `tool` and `query` in the string, but a string has no fields with those names. To get at them, parse the text with `json.loads`:

```python
command = json.loads(text)
command['tool']    # 'find_notes'
command['query']   # 'python'
```

Now `command` is a dictionary. `json.loads` neither chooses nor invents anything; it only reads what is written in the text. An easy way to remember the pair: `dumps` turns data into text, `loads` turns text into data.

If the model replied with plain words, `json.loads` raises `JSONDecodeError`. The string `'[]'` is valid JSON, but it parses into a list, and a command needs a dictionary. We handle both cases.

## Your turn

Replace the placeholder in `parse_decision` with the code below and fill in the two gaps:

```python
def parse_decision(text: str) -> dict:
    try:
        command = ...
    except json.JSONDecodeError:
        raise ValueError('The model returned text instead of a JSON command: ' + text[:400]) from None
    if not isinstance(command, ...):
        raise ValueError('The command must be a JSON object')
    return command
```

1. `command` gets `json.loads(text)`.
2. The type for `isinstance` is `dict`.

`try` holds the action that may fail. On `JSONDecodeError`, Python jumps to `except`, where we replace the technical message with a clear one; `text[:400]` keeps only the first 400 characters of the reply. `isinstance(command, dict)` is `True` for a dictionary and `False` for a list.

The function returns the dictionary to its caller. In the demonstration that is `decision = parse_decision(text)`, after which `decision['tool']` gives `'find_notes'`. Nothing is searched yet: `dispatch_tool` runs the command in the main project.

## Run it

Open `demo_check.py` and choose **Run**. First you see the change from string to dictionary:

```text
Before parsing: <class 'str'>
After parsing: <class 'dict'>
Command: {'type': 'tool', 'tool': 'find_notes', 'query': 'python'}
Tool: find_notes
Query: python
```

Then the demonstration tries "I will search now" and `'[]'`, and a different check fires for each. To run the prepared checks, run `tests/test_lesson.py`.

## Try to break it

Change `return command` to `return text` in your function and run `demo_check.py` again. The parsing still happens, but the function returns the original string, and reading the `'tool'` field in the demonstration fails. Calling `json.loads` is not enough; the result has to be passed on. Put `return command` back.

The check has a limit. The dictionary `{'type': 'tool', 'tool': 'delete_file'}` passes both checks in `parse_decision`: it is valid JSON and it is a dictionary. Such an action is rejected by `dispatch_tool`, which holds the list of permitted tools. Checking the format and permitting actions are separate jobs.

Next: [send an HTTP request from Python](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/extra-prepared-modules/03-request.md). Back to [the workbook](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/extra-prepared-modules/README.md).
