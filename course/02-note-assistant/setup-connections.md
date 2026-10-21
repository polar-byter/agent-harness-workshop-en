# When a real answer does not appear

First identify where execution stopped. An unfinished exercise, an unreachable service and a generated answer that contradicts its source require different corrections. Read the first meaningful error in Run rather than changing several settings at once.

## The Ollama command is not found

Installing an application does not update the environment of a program that was already open. Close all PyCharm windows and reopen the project, then open a new Terminal and run `ollama --version` again. Also try a new PowerShell window from the Start menu. If it works there but not in PyCharm, the editor still has an old environment.

If neither terminal recognizes the command, confirm that Ollama appears in installed applications and starts from the Start menu. The [Windows instructions](https://docs.ollama.com/windows) describe its install location. If needed, use the actual installed `ollama.exe` path to confirm the executable exists before changing PATH. Do not guess a Python interpreter command: Ollama is a separate program.

## A model is missing or the service is unreachable

For Ollama, confirm the app is running and `ollama list` contains the exact model name. Download it with `ollama pull qwen3:0.6b` if absent. The local API normally listens at `http://127.0.0.1:11434`.

For API services, check the selected provider, model ID and account conditions in `configure_model.py`. HTTP 401 commonly calls for checking credentials; 402 can indicate account balance requirements; 403 requires checking account or regional availability; 404 can mean an incorrect model or endpoint; 429 can indicate a request limit or overload. Read the provider's own error too: these are diagnostic starting points, not universal explanations.

## The request works but the answer is wrong

Inspect the question and source notes first. Then check the actual messages and the extracted answer. Do not change a fixture or hard-code the expected text to make the live run look correct. Use `demo_check.py` to test your Python separately and compare the actual model result with the source.

Keep API keys in the course settings window. The advanced `HARNESS_CONNECTION_FILE` override can select another settings file, but ordinary course work does not require it. Return to [the connection lesson](04-connect.md) after resolving the failing step.
