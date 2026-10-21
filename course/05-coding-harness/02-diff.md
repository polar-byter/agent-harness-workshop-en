# Preview a proposed change

The exercise file adds price and quantity even though total price requires multiplication. We can ask a model to propose a correction, but we should see the proposed difference before writing it. `preview_change` builds that inspectable proposal.

## Open this starter

Download [this lesson starter](../../downloads/lesson-05-02-diff.zip), choose **Extract All**, and open the extracted `lesson-05-02-diff` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `workspace.py` -> `preview_change`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder. The main run uses the connection saved in the [required connection lesson](../../course/02-note-assistant/04-connect.md). The offline `demo_check.py` remains a separate code check.

## Follow the data

The old line is `return price + quantity`; the proposed line is `return price * quantity`. A unified diff marks removed lines with `-` and added lines with `+`. The proposal also stores the original file hash and the complete proposed text.

<img src="../../assets/05-coding-harness/lesson-02-diff.gif" width="480" alt="Data flow for preview a proposed change">

[Static diagram](../../assets/05-coding-harness/lesson-02-diff.png). This illustrates the data flow; it is not a recording of an unfinished starter running.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def preview_change(root: Path, relative: str, new_text: str) -> dict:
    path = workspace_path(root, relative)
    old_text = path.read_text(encoding='utf-8')
    lines = difflib.unified_diff(
        old_text.splitlines(keepends=True),
        new_text.splitlines(keepends=True),
        fromfile='before/' + relative,
        tofile='after/' + relative,
    )
    before_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        'path': relative,
        'before_hash': before_hash,
        'new_text': ...,
        'diff': ...,
    }
```

Get the checked path using `workspace_path` and read its UTF-8 text. Use `difflib.unified_diff` on old and new `splitlines(keepends=True)` lists, then join its output. Compute `hashlib.sha256(path.read_bytes()).hexdigest()` for `before_hash`.

Return `path`, `before_hash`, `new_text` and `diff`. Do not write `new_text` here. A hash is a comparison value for the next lesson, not an encryption of the source or proof that the proposed change is correct.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-05-02-diff**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run the live example to inspect what the model proposes, or `demo_check.py` for the prepared multiplication change. Open `workspace/prices.py` afterward: previewing should leave its old text intact. The exact model proposal is not predetermined, so a missing or incorrect change must be reviewed as an outcome.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.

[All lessons](../../course/README.md).
