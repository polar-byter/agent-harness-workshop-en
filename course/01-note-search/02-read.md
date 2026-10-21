# Read notes from a file

Our search accepts a list of strings, while real notes are stored in a file. The next function will connect those two forms of data. Keeping reading separate from searching lets us examine a problem at the right place: was the file read correctly, or did the search select the wrong lines?

## Open this starter

Download [this lesson starter](../../downloads/lesson-01-02-read.zip), choose **Extract All**, and open the extracted `lesson-01-02-read` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `notes.py` -> `read_notes`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder.

## Follow the data

`path` is a `Path` object identifying a file, not its contents. For example, a file containing `Python lists`, a blank line and `Agent tools` becomes the single string `'Python lists\n\nAgent tools\n'` after `read_text`. Here `\n` represents a line break. `splitlines()` turns it into `['Python lists', '', 'Agent tools']`.

We need a list of nonempty, trimmed lines. Whitespace-only lines are not notes, while repeated nonempty lines remain repeated.

<img src="../../assets/01-note-search/read-notes.gif" width="480" alt="Data flow for read notes from a file">

[Static diagram](../../assets/01-note-search/read-notes.png). This illustrates the data flow; it is not a recording of an unfinished starter running.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def read_notes(path: Path) -> list[str]:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    cleaned_notes = []
    for line in lines:
        cleaned_line = ...
        if ...:
            cleaned_notes.append(...)
    return cleaned_notes
```

Read the text with `path.read_text(encoding='utf-8')`. UTF-8 specifies how file bytes become characters. Use `text.splitlines()` for the loop. For each line, compute `cleaned = line.strip()`; append `cleaned` only if it is nonempty. Return the accumulated list after the loop.

An empty file produces `[]`. If the file does not exist, `read_text` raises `FileNotFoundError`. Let that error reach the caller for now. Returning an empty list in both cases would hide the difference between missing data and a valid empty source.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-01-02-read**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py`. It calls `read_notes` on the supplied `data/notes.txt` and prints the returned list. Compare its elements with the file itself. For an extra experiment, copy the data file, add a blank line and spaces at the ends of one line, and call the function on that copy. The visible note text should stay the same.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.

[All lessons](../../course/README.md).
