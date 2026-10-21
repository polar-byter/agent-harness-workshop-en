# Optional: follow send_live from messages to a response

Our note assistant starts with a question and one source note. `build_messages` has already put them into message dictionaries. The job of `send_live(messages)` is to send those messages through the selected connection and return a response the rest of the course understands.

## Read the connection

`read_connection()` opens the settings file written by `configure_model.py`. It obtains a provider, model ID and any required key. This file lives outside the starter, so copying a lesson does not copy credentials. The English edition uses its own settings location.

## Prepare provider messages

The supported backends receive our developer instruction as a system message. The function builds new message dictionaries with that role change; it does not mutate the caller's original list. The text of the instruction and the source notes remain the same.

For Ollama it builds a local `/api/chat` request with streaming disabled, CPU-oriented settings and bounded context and output options. For the API providers it builds a chat-completions request with the chosen model and messages. The request contains the source text we supplied; the service does not independently read `data/notes.txt` from our disk.

## Send and decode

`request_json` serializes the request dictionary, encodes it as UTF-8 bytes and describes a POST request with its headers. `urlopen` performs the exchange with a timeout. The response bytes are decoded and parsed as JSON. HTTP and connection errors are reported instead of becoming an invented answer.

## Normalize the provider response

Ollama and API providers return different fields. The adapter checks whether generation finished and extracts the provider's message content. `course_response(text)` wraps that text as a completed course response with an output message and an output_text part. `extract_answer` can then work with this shared format.

This wrapper is a course convention, not a claim that every service uses the same wire protocol. It also does not verify the factual content of the sentence. A generated answer can be complete and still be unsupported by the notes.

The optional [prepared-modules workbook](../extra-prepared-modules/README.md) lets you implement message construction, request serialization and decision parsing yourself. Return to [the live connection lesson](04-connect.md) for the actual run sequence.
