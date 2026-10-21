# Connect a real model

So far a prepared response has helped us check how messages and answers fit together. Now we will replace it with actual generation. Complete this connection before continuing to the agent projects: their main examples expect a saved, working model connection.

The most tangible first route is a small local model. It lets you send a request from Python and receive an answer generated on your own computer. A dedicated GPU is not required for this CPU exercise, though speed and available memory still matter. If you already have an API account, the other routes use the same course functions.

## Route 1: Ollama on this computer

1. Open the [Ollama download page](https://ollama.com/download/windows). On Windows select the Windows tab. If you see a PowerShell install command, use the **Download manually** link below it for the installer route used here. Open the downloaded `OllamaSetup.exe` and complete installation.
2. Start Ollama from the Start menu if needed. It runs in the background. Close and reopen PyCharm after installation so the editor receives the updated command path.
3. Open **View -> Tool Windows -> Terminal** in PyCharm and enter `ollama --version`. Confirm the command is recognized before downloading a model.
4. Run `ollama pull qwen3:0.6b`. This downloads model files; it does not send your notes to a cloud model. Wait for the download to finish.
5. Run `ollama run qwen3:0.6b` and ask a short question. A generated reply confirms the model can run. Enter `/bye` to leave that chat; Ollama continues serving requests in the background.

If `ollama` is not recognized, follow [the short connection troubleshooting guide](setup-connections.md#the-ollama-command-is-not-found) rather than repeating the download command. The [Windows documentation](https://docs.ollama.com/windows) explains installation and changing the model storage folder. You can set `OLLAMA_MODELS` in your user environment before downloading models; restart Ollama after changing it.

## Route 2: OpenRouter

Create or use your own [OpenRouter account](https://openrouter.ai/), choose a model available to it and create an API key. Use the exact model ID shown by the provider, including its prefix. Available free options, credits and regional access can change; check the account's current conditions instead of assuming every listed model is available.

## Route 3: VseGPT

If [VseGPT](https://vsegpt.ru/) suits your account and region, obtain its API key and exact supported model ID. The course adapter already has a VseGPT option. A key from one service is not automatically valid at another service's endpoint.

## Save the selection once

Open the [connection starter](../../downloads/lesson-02-04-connect.zip) as its own PyCharm project. Run `configure_model.py`. In the small window select the provider, enter the model name, and enter an API key for an API service. Ollama needs only `qwen3:0.6b`. Click **Save**.

The English edition stores its connection outside the project under a separate English-course settings folder. Its lesson copies share that selection, so you do not need to paste a key into each starter. Do not put a key in Python source, a screenshot or a committed file.

Now run `demo.py`. It prepares the question and source note, calls `send_live` and extracts the answer. Read the actual answer in Run. It should reflect that Python lists keep item order, but its wording is not fixed. A wrong statement is a result to investigate, not a reason to overwrite the output with the expected sentence.

## Follow the instruction and source

`build_messages` places the source-only instruction in a developer message and the question with notes in a user message. `send_live` converts the instruction role for the supported backend, sends the request and normalizes its response. `extract_answer` then selects the returned text.

The supplied rule can reach the model and still be violated. Compare the answer with the original note and inspect the prepared messages before blaming the search. A tiny local model may also fail to return strict JSON in later lessons; a working connection and suitable model capability are separate checks.

For an optional walkthrough of the connection code, read [how send_live works](extra-send-live.md). For request statistics and context concepts, continue to [the optional statistics exercise](extra-usage.md). The next required project [executes tool requests](../03-tool-agent/01-tools.md).
