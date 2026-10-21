# Write a search function

Suppose a colleague asks which of your notes mention Python. You can read three lines yourself, but an agent needs an operation that accepts a query and returns matching source text. We will write that operation before connecting a model. This keeps the first experiment observable: the same notes and query should produce the same list every time.

The function will not print, open a file or ask a model anything. Its result is a list that a caller can inspect, save or include in a later model request.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-01-01-search.zip), choose **Extract All**, and open the extracted `lesson-01-01-search` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `notes.py` -> `find_notes`, `notes.py` -> `find_notes_alt`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

The demonstration supplies `notes = ['Python lists', 'Agent tools', 'python functions']` and `query = ' PYTHON '`. The list is the first argument, so it becomes the parameter `notes`; the string becomes `query`. The expected result is `['Python lists', 'python functions']`, preserving the spelling of the source lines.

`strip()` removes whitespace at the ends of the query. `casefold()` prepares text for case-insensitive comparison. The expression `'python' in 'python lists'` is `True`: the left string occurs inside the right string. We transform a note only for comparison and return its original text.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def find_notes(notes: list[str], query: str) -> list[str]:
    query = query.strip().casefold()
    if not query:
        raise ValueError('Enter a nonempty query')
    selected = []
    for note in notes:
        if ...:
            selected.append(...)
    return selected
```

Use `query in note.casefold()` as the condition and `note` as the argument to `append`. The list starts empty; after the first line it contains `['Python lists']`, after the second it is unchanged, and after the third it contains both matching lines.

Python uses indentation to define blocks. Use four spaces per level: the condition belongs inside the loop and `append` inside the condition. Put `return selected` at the same indentation as `for`, so it runs after all notes have been checked. A return inside the loop would stop the search early.

Now implement `find_notes_alt` with the same query preparation and empty-query check, followed by `return [note for note in notes if query in note.casefold()]`. This list comprehension performs the same selection in one expression. Compare the two implementations on identical inputs; the shorter spelling should not change their behavior.

## Run and inspect

Open `demo_search.py` directly under **Project -> lesson-01-01-search**, right-click in its editor and choose **Run 'demo_search'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Open `demo_search.py` and run it. Both functions should return `['Python lists', 'python functions']`. Printing belongs to the demonstration: `print(matches)` displays the list and adds a newline by default. Multiple arguments are separated by a space; for example, `print('Matches:', matches)` adds a readable label without changing the result.

Try a query with no match, then a query containing spaces only. The first should return `[]`; the second should raise `ValueError`. An empty request and an unsuccessful search are different cases.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
