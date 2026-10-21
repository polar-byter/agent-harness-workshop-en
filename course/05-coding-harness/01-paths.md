# Restrict the working folder

A coding assistant needs to read and change a file, but a model-supplied path should not select any file on the computer. We will check the path before further file operations, using a dedicated exercise workspace.

## Open this starter

Download [this lesson starter](../../downloads/lesson-05-01-paths.zip), choose **Extract All**, and open the extracted `lesson-05-01-paths` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `workspace.py` -> `workspace_path`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder. The main run uses the connection saved in the [required connection lesson](../../course/02-note-assistant/04-connect.md). The offline `demo_check.py` remains a separate code check.

## Follow the data

`root` is the exercise `workspace` folder and `relative` might be `'prices.py'`. Resolving their combination produces an absolute path. A separate experiment with `'../outside.py'` attempts to leave the root and must be rejected.

<img src="../../assets/05-coding-harness/lesson-01-paths.gif" width="480" alt="Data flow for restrict the working folder">

[Static diagram](../../assets/05-coding-harness/lesson-01-paths.png). This illustrates the data flow; it is not a recording of an unfinished starter running.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def workspace_path(root: Path, relative: str) -> Path:
    root = root.resolve()
    candidate = (root / relative).resolve()
    if Path(relative).is_absolute() or not candidate.is_relative_to(root):
        raise ValueError('The path must stay inside the exercise folder')
    if ...:
        raise ValueError('This exercise only handles Python files')
    return candidate
```

Resolve `root` and `(root / relative)`. Reject an originally absolute `relative` or a candidate that is not `is_relative_to(root)`. Also require suffix `'.py'`, then return the candidate Path.

Check the resolved relationship rather than a text prefix: similarly named folders are not necessarily parent and child. The prepared exercise focuses on this path rule; do not interpret it as a general sandbox.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-05-01-paths**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run `demo.py` and inspect the permitted relative path. In the offline checks, an outside path should raise `ValueError`. Executing a Python file remains ordinary process execution with operating-system permissions. A path check alone does not isolate unknown code, so use the supplied exercise workspace for the course.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.

[All lessons](../../course/README.md).
