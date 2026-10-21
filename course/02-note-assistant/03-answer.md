# Connect the request and the answer

We can now build messages and extract an answer, but the application still needs a single operation that joins those steps. `answer_question` will accept a sending function as an argument, allowing us to check our own control flow without depending on a network service.

## Open this starter

Download [this lesson starter](../../downloads/lesson-02-03-answer.zip), choose **Extract All**, and open the extracted `lesson-02-03-answer` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `assistant.py` -> `answer_question`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

`answer_question(question, notes, send)` receives a callable in `send`. It calls `build_messages`, gives the resulting list to `send`, then passes the returned response to `extract_answer`. A prepared file can stand in for the sending operation during checks; the same function can later receive `send_live`.

<img src="../../assets/02-note-assistant/lesson-03-answer.gif" width="480" alt="Data flow for connect the request and the answer">

[Static diagram](../../assets/02-note-assistant/lesson-03-answer.png). This illustrates the data flow; it is not a recording of an unfinished starter running.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def answer_question(question: str, notes: list[str], send) -> str:
    if not notes:
        return 'No matching notes.'
    messages = build_messages(question, notes)
    response = ...
    answer = ...
    return answer
```

Keep the empty-question check. If `notes` is empty, return `'No matching notes.'` before calling `send`. Otherwise build the message list, call `response = send(messages)` and return `extract_answer(response)`.

Passing a function as an argument does not call it immediately. The call happens at `send(messages)` inside `answer_question`. This is why we can change the connection without rewriting the sequence.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-02-03-answer**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py` for the assembled example. The supplied response should produce `Python lists preserve item order.`. This checks the connection between our functions, not the quality of a model: the answer comes from a file. In the next required lesson we will replace that stand-in with a real connection.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.

[All lessons](../../course/README.md).
