# Apply an approved proposal

Approval is meaningful only if we write the proposal that was reviewed against the file version that was reviewed. Another edit between preview and application could otherwise be overwritten unnoticed. We will check both permission and the original file hash.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-05-03-apply.zip), choose **Extract All**, and open the extracted `lesson-05-03-apply` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `workspace.py` -> `apply_change`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder. The main run uses the connection saved in the [required connection lesson](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/04-connect.md). The offline `demo_check.py` remains a separate code check.

## Follow the data

The input `proposal` contains the relative path, original hash and new text from the previous function. `approved=False` means no change should be made. With approval, the current file hash must still match `proposal['before_hash']`.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def apply_change(root: Path, proposal: dict, approved: bool) -> bool:
    if not approved:
        return False
    path = workspace_path(root, proposal['path'])
    current_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if current_hash != proposal['before_hash']:
        raise ValueError('The file changed after the proposal was prepared')
    path.write_text(..., encoding='utf-8')
    return True
```

Return `False` immediately when approval is absent. Otherwise validate the path, hash its current bytes and compare the result with the stored hash. Raise `ValueError` if they differ. If they match, write `proposal['new_text']` with UTF-8 and return `True`.

Do not automatically refresh the stored hash to make the check pass. The mismatch indicates that the proposal needs a fresh review. This exercise is a simple sequential workflow, not a full concurrency-control or sandbox system.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-05-03-apply**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py`. Read the diff before typing `yes` in Run; pressing Enter declines. Confirm that declining leaves the file unchanged and approval writes the proposed text. A successful write says the change was applied, not that it passed tests. That separate check follows next.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
