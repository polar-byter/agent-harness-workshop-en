# Send an HTTP request from Python

The model connection is not a special channel hidden inside the interpreter. Our program encodes a JSON request, sends its bytes to a service and parses the returned bytes. We will implement that small network section while keeping error handling visible.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-extra-03-request.zip), choose **Extract All**, and open the extracted `lesson-extra-03-request` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `transport.py` -> `request_json`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

`url` identifies the endpoint, `payload` is a dictionary and `api_key` is optional. JSON serialization produces a string; UTF-8 encoding produces the bytes used as the POST body. The response follows the reverse path: bytes, decoded text, parsed JSON.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def request_json(url: str, payload: dict, api_key: str = '') -> dict:
    headers = {'Content-Type': 'application/json'}
    if api_key:
        headers['Authorization'] = 'Bearer ' + api_key
    request = Request(url, data=..., headers=headers, method='POST')
    try:
        with urlopen(request, timeout=180) as response:
            return json.loads(...)
    except HTTPError:
        raise
```

For the first blank, use `json.dumps(payload, ensure_ascii=False).encode('utf-8')`. For the second, use `response.read().decode('utf-8')`. `Request` describes the operation; `urlopen` performs it, and `with` closes the response.

The compact template shows the data path. In the actual file, replace the unfinished network section and keep its existing `HTTPError`, `URLError` and timeout handling rather than replacing those branches with this abbreviated example. Do not print the authorization header or save a key in the lesson source.

## Run and inspect

Open `demo_check.py` directly under **Project -> lesson-extra-03-request**, right-click in its editor and choose **Run 'demo_check'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo_check.py` first: it substitutes an offline response and inspects the serialized request. After it passes, use `demo.py` with the saved real connection. A JSON object returned by this function is still a provider response, not yet the final answer string.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
