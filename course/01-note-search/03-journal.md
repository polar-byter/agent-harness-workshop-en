# Save a search result

A console message disappears among later runs. A journal lets us check which query produced which result. We will save one JSON object per line, keeping earlier runs instead of replacing them. This simple record will later help us separate what the program actually found from what a model says it found.

## Open this starter

Download [this lesson starter](../../downloads/lesson-01-03-journal.zip), choose **Extract All**, and open the extracted `lesson-01-03-journal` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `journal.py` -> `write_result`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

`result = {'query': 'python', 'matches': ['Python lists']}` is a dictionary: keys identify the query and matching lines. `json.dumps(result, ensure_ascii=False)` returns a JSON string. Writing that string followed by `"\n"` creates one record in `runs.jsonl`. JSONL is a convention: each line is a separate valid JSON value.

<img src="../../assets/01-note-search/lesson-03-journal.gif" width="480" alt="Data flow for save a search result">

[Static diagram](../../assets/01-note-search/lesson-03-journal.png). This illustrates the data flow; it is not a recording of an unfinished starter running.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def write_result(path: Path, result: dict) -> None:
    text = json.dumps(result, ensure_ascii=False)
    with path.open('a', encoding='utf-8') as stream:
        stream.write(...)
```

Open `path` with `path.open('a', encoding='utf-8')`: mode `'a'` appends. Use the stream inside `with`, which closes it when the block ends. Serialize `result` with `json.dumps(..., ensure_ascii=False)` and pass the resulting string plus `'\n'` to `stream.write`.

The function writes the supplied dictionary; it should not perform a new search. Its return value is `None`, because the useful effect here is a new line in the file. A missing parent folder is still a file-system error, not a successful record.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-01-03-journal**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py` twice and open `runs.jsonl` in the Project panel. There should be a record for each run. Do not compare JSON key order or spacing as though they were the meaning of the result: parse a line with `json.loads` when you want its dictionary values.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.

[All lessons](../../course/README.md).
