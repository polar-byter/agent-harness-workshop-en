# Connect reading, search and the journal

We have three operations, but a caller should not have to repeat their sequence for every search. `run_search` will read the source, normalize the request, select notes and save one result. It will also make unsuccessful searches explicit instead of treating every run as a match.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-01-04-run.zip), choose **Extract All**, and open the extracted `lesson-01-04-run` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `app.py` -> `run_search`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

The input contains `notes_path`, `query = ' Python '` and `journal_path`. Reading produces a list of notes. Search returns the original matching lines. The returned dictionary contains the cleaned query, a status and the matches. With this source, the two matching lines are `Python functions return values.` and `Python lists keep item order.`.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def run_search(notes_path: Path, query: str, journal_path: Path) -> dict:
    notes = read_notes(notes_path)
    matches = find_notes(notes, query)
    status = 'found' if matches else 'not_found'
    result = {
        'query': ...,
        'status': ...,
        'matches': ...,
    }
    write_result(..., ...)
    return result
```

Use `query.strip()` for the query stored in the result, reject an empty string, call `read_notes(notes_path)`, then `find_notes(notes, query)`. Set the status to `'found'` if the matches list is nonempty and `'not_found'` otherwise. Store `query`, `status` and `matches` in one dictionary.

Call `write_result(journal_path, result)` once and return that same dictionary. Do not catch a missing source file and turn it into `'not_found'`: the search never took place in that situation.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-01-04-run**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py` and compare the printed dictionary with the latest journal line. Run a missing-word query as well: it should save an empty matches list with `'not_found'`. This function will become useful to an agent without requiring any console interaction inside it.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
