# Run a model inside Python

Ollama serves a model through a local HTTP API. Another option is to load a GGUF model through a Python library in the same process as our application. This optional experiment makes that boundary visible without changing the rest of the course connection.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-02-extra-local.zip), choose **Extract All**, and open the extracted `lesson-02-extra-local` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `local_model.py` -> `send_local`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

The prepared `local_runtime.load_model` loads a `Llama` instance with CPU execution and a bounded context. Our `send_local(model, messages)` prepares the message roles, calls the model and converts its dictionary response into the normalized course format.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def send_local(model, messages: list[dict]) -> dict:
    prepared = prepare_messages(messages)
    response = model.create_chat_completion(
        messages=..., max_tokens=256, temperature=0,
    )
    return convert_response(...)
```

Pass `prepared` as the messages argument and `response` to `convert_response`. Keep the supplied generation settings; the tests inspect the message roles and limit. The conversion checks completion and selects answer text.

Use the prepared loading context manager: it closes the model in `finally`. Do not write `with Llama(...)` for this pinned exercise version. Loading a model needs RAM beyond the file size, and a small model may fail to follow instructions even when the library runs correctly.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-02-extra-local**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

First run `demo_check.py`; it uses a fake model object and does not import or load the real runtime. For the optional real run, follow the [installation and model-file instructions](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/local-setup.md). Run `check_install.py`, then `demo.py` after placing the GGUF file where that lesson specifies. This experiment is separate from the shared Ollama or API connection.

This optional branch keeps its checks in `demo_check.py` rather than a tests folder. It uses a fake model object and can run without loading the library or weights.
