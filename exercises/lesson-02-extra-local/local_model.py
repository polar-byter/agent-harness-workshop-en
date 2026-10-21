from local_runtime import prepare_messages, convert_response


def send_local(model, messages: list[dict]) -> dict:
    prepared = prepare_messages(messages)
    # Pass messages to the loaded model and return the course response format.
    raise NotImplementedError('Complete send_local using the lesson hints')
