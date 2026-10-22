# Run a model inside Python

> **Where we are.** In the main route the program sends messages to Ollama, which runs the model. Here we load a model into our own Python program instead. This lesson is optional; the main route keeps using Ollama or a cloud service.

So far the model ran in a separate application and our code only sent it requests. Another option is to load the model file directly into the Python program. Then loading the model, calling it and freeing its memory become our code's job. This is how a model gets built into a program that must work without a network.

The question and clause stay the same, and `build_messages` and `extract_answer` do not change: we convert the model's reply into the familiar format. The only new function is `send_local`, which calls the loaded model.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-02-extra-local.zip), extract it and open the `lesson-02-extra-local` folder in PyCharm. The current task is `send_local` in `local_model.py`. Loading the model and converting its reply are ready in `local_runtime.py`.

## Look at the data

`local_runtime.load_model` creates a `Llama` object from the library llama-cpp-python, set to calculate on the processor with a limited context. Our `send_local(model, messages)` receives that object and the list of messages. The prepared `prepare_messages` changes the `developer` role to `system` and adds a short instruction for Qwen; `convert_response` checks that generation finished and wraps the text in the course format.

## Your turn

The line `prepared = prepare_messages(messages)` is already there. Replace the `raise NotImplementedError(...)` after it so the function looks like this, and fill in the gaps:

```python
def send_local(model, messages: list[dict]) -> dict:
    prepared = prepare_messages(messages)
    response = model.create_chat_completion(
        messages=..., max_tokens=256, temperature=0,
    )
    return convert_response(...)
```

1. Pass `prepared` as `messages`.
2. Pass `response` to `convert_response`.

`model.create_chat_completion(...)` hands the messages to the engine and returns a dictionary; there is no HTTP request and no Ollama here, everything happens inside our program. Keep the generation settings as given: the checks look at the roles and the length limit.

## Run it

Run `demo_check.py` first. It uses a small fake model object instead of the real one, so it needs neither the library nor the model file, and it checks that your function passed the right messages and returned the right structure.

For a real answer, follow the [installation and model-file instructions](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/local-setup.md), run `check_install.py`, put the GGUF file where that page says and then run `demo.py`. Loading needs more memory than the file size, and a small model can ignore an instruction even when the library works perfectly; compare its answer with the note.

## What we have now

We changed only how one request reaches the model: the program loads the file itself instead of calling Ollama. In the [agent loop](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/03-tool-agent/02-cycle.md) any of these ways - API, Ollama or library - fills the same place: it receives messages and returns the model's next decision. This exercise does not change the saved connection used by the other starters. Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
