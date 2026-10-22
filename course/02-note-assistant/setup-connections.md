# When a real answer does not appear

Start by finding where execution stopped. An unfinished exercise, an unreachable service and an answer that contradicts its source each need a different fix. Read the first meaningful error in the Run window before changing any settings, and change one thing at a time.

## The Ollama command is not found

A program that was already open when you installed Ollama does not see the updated list of program folders (PATH). Close all PyCharm windows with **File -> Exit**, start PyCharm again, open a new Terminal and run `ollama --version`. Closing only the Terminal tab is not enough. Try a new PowerShell window from the Start menu too: if the command works there but not in PyCharm, the editor is still running with the old settings.

If neither terminal recognizes the command, check that Ollama appears in your installed apps and starts from the Start menu. The [Windows instructions](https://docs.ollama.com/windows) give its install location; you can run `ollama.exe` by its full path to confirm it exists before changing PATH.

## The model is missing or the service is unreachable

For Ollama, make sure the app is running and `ollama list` shows the exact model name. If it is missing, run `ollama pull qwen3:0.6b`. The local service normally listens at `http://127.0.0.1:11434`.

For API services, check the service, model ID and account in `configure_model.py`. Common HTTP errors point to common causes:

| Error | Check first |
|---|---|
| 401 | The key belongs to the chosen service and was copied completely |
| 402 | The account has credits or a balance |
| 403 | The model is available to your account and region |
| 404 | The model ID or service address is spelled correctly |
| 429 | A request limit was reached or the service is overloaded; try again later |

Read the service's own error text as well; it often says more than the code.

## The request works but the answer is wrong

The connection is fine; now the question is the model's behavior. Look at the question and the clause first, then at the actual messages and the extracted answer. Run `demo_check.py` to test your Python separately from the model. Do not edit the prepared response or hard-code the expected text to make the live run look right.

Keep API keys in the course settings window. Return to [the connection lesson](04-connect.md) once the failing step works.
