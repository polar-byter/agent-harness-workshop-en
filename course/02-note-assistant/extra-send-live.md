# Optional: follow send_live from messages to a response

> **Where we are.** In lesson 2.4 the program sent a question and a policy clause to a model and got an answer back. Here we read the ready code that does the sending. Nothing to write, only to follow.

Suppose the model answered beyond the policy. Before blaming the model, it is worth checking what it actually received: did the rule and the clause reach it, where did the program send the request, and what text did it read from the reply? For that you need to know the path inside `transport.py`, from the call to `send_live` back to the result. Open `transport.py` in the `lesson-02-04-connect` project and follow along.

## Read the connection

`send_live(messages)` first calls `read_connection()`, which opens the settings file written by `configure_model.py`. It returns the service, the model ID and the key, if the service needs one. The file lives outside the project folders, so copying a lesson never copies your key. If no connection has been saved, the function stops before any network request.

## Prepare the messages for the service

The supported services expect our rule as a `system` message rather than `developer`. `send_live` builds new message dictionaries with that role changed and leaves the caller's list untouched. The text of the rule and the notes stays exactly the same.

For Ollama it builds a request to the local `/api/chat` address with streaming switched off, calculation on the processor and limits on context and answer length. For the API services it builds a chat-completions request with the chosen model and messages. The request carries the note we passed in; the service never reads `data/notes.txt` from your disk.

## Send and decode

`request_json` turns the request dictionary into a JSON string and then into UTF-8 bytes, and describes a POST request with its headers in a `Request` object. Creating that object sends nothing; `urlopen` does the actual exchange, with a timeout. The reply arrives as bytes, which are decoded into text and parsed back into a dictionary. HTTP errors and connection problems are reported as errors, never turned into an empty answer.

## Bring every service to one format

Ollama and the API services return their text in different fields. `send_live` checks that generation finished normally and takes the text from the field where that service keeps it. `course_response(text)` then wraps the text in the course's format with `status` and `output`, so `extract_answer` works the same way whichever service you chose.

This step checks that the answer is complete; whether it agrees with the clause is still for you to judge.

## Check yourself

Without running the model, find three places in `transport.py`: where the role is changed, where `Request` only describes the request and where `urlopen` sends it. Then follow the answer string back to the `print` in `demo.py`. If the model ever answers beyond its notes, you will be able to confirm that the rule and the note did reach it, and the cause really is the model.

To write these parts yourself, try the optional [prepared-modules workbook](../extra-prepared-modules/README.md). Back to [the connection lesson](04-connect.md).
