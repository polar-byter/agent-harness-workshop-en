# Extract text from a service response

A model service returns a structured response, not just a sentence. We need to select the answer text while ignoring unrelated elements. Keeping this conversion in a function allows the rest of the application to work with a string rather than a provider response.

## Open this starter

Download [this lesson starter](../../downloads/lesson-02-02-response.zip), choose **Extract All**, and open the extracted `lesson-02-02-response` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `assistant.py` -> `extract_answer`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

The course response has `status='completed'` and an `output` list. A message item has a `content` list, whose text part has `type='output_text'` and a `text` value. The supplied fixture contains `Python lists preserve item order.`.

This is the normalized course format. `transport.py` converts each supported provider response into it; the services do not all return this exact structure.

<img src="../../assets/02-note-assistant/lesson-02-response.gif" width="480" alt="Data flow for extract text from a service response">

[Static diagram](../../assets/02-note-assistant/lesson-02-response.png). This illustrates the data flow; it is not a recording of an unfinished starter running.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def extract_answer(response: dict) -> str:
    if response.get('status') != 'completed':
        raise ValueError('Model response is incomplete')
    parts = []
    for item in response.get('output', []):
        if item.get('type') == 'message':
            for part in item.get('content', []):
                if part.get('type') == 'output_text':
                    parts.append(...)
    answer = '\n'.join(parts).strip()
    if not answer:
        raise ValueError('The response contains no text')
    return ...
```

Keep the prepared status check. Loop over `response.get('output', [])`, select items with `type == 'message'`, then loop over their `content`. Select `type == 'output_text'` and append each text value to `parts`. Join the collected strings with `'\n'` and trim the result.

Reject an empty final string. An incomplete response or a structure without answer text should not silently become a successful empty answer. `return` passes the string to the caller; it does not print it.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-02-02-response**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py`. The result should be the sentence from the fixture, without the surrounding response dictionary. For a small experiment, inspect the fixture and distinguish service fields from source text; do not change it just to make a failing function appear successful.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.

[All lessons](../../course/README.md).
