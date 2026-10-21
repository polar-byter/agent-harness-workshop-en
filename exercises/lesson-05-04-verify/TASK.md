# Check the changed project

> **Where we are.** The agent proposed a change, a person approved it and the program wrote the file. The last step: make sure the code actually works after the change.
> `proposal -> diff -> approval -> write -> [tests]`

All we know so far is that the change was written. That does not mean the order total is now right: the model could have proposed code with a different bug, and the person could have missed it in the diff. What has to be checked is the code's behavior: with a price of 100 and a quantity of 3, the total must be 300.

The folder `workspace/tests` holds tests for the calculation. `check_project` runs them from our program and returns a clear report. With the original addition the tests fail; after a correct fix they pass. One detail matters: the conditions of the check were set by us in advance, not by the model after its own change.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-05-04-verify.zip), extract it and open the `lesson-05-04-verify` folder in PyCharm. The current task is `check_project` in `workspace.py`.

## Look at the data

`workspace/tests` checks three cases: 100 x 3 = 300, 100 x 0 = 0 and 12.5 x 2 = 25. The tests run as a separate Python process, and its exit code tells the outcome: `0` means everything passed, any other number means something failed. The command is already in the starter:

```python
command = [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests']
```

`sys.executable` is the same Python that runs `demo.py`. `-m unittest discover -s tests` finds and runs the tests in the `tests` folder. The command is a list rather than a string, so nothing can be slipped into it through the command shell.

## Your turn

Replace `raise NotImplementedError(...)` in `check_project` with the code below and fill in the gaps:

```python
    process = subprocess.run(
        command,
        cwd=root,
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
        timeout=5,
    )
    return {
        'passed': ...,
        'returncode': process.returncode,
        'output': ...,
    }
```

1. `'passed'` is `process.returncode == 0`.
2. `'output'` is `process.stdout + process.stderr`: tests write to both streams.

`subprocess.run` starts the process and waits for it to finish. `cwd=root` is the folder the tests run from, `capture_output=True` collects the output instead of printing it, `text=True` and `encoding` return it as strings, and `timeout=5` stops the wait after five seconds if the tests hang.

## Run it with the model

Open `demo.py` and choose **Run 'demo'**. Now the whole pass runs: the model proposes a fix, the program shows the diff, asks for approval, writes the change and calls your function. Type `yes` if you agree with the change, or press Enter to decline. The Run window shows the test result for the current `prices.py`.

**Guess before running:** what will the tests show if you decline the change?

## Check the function on its own

Open `demo_check.py` and choose **Run 'demo_check'**. It runs the tests for the current `workspace/prices.py` without a model. In a freshly extracted starter that file still adds, so we expect `passed: False`, a non-zero `returncode` and, in `output`, the test's message: 300 was expected and 103 came back. If you have already applied a correct fix through `demo.py`, the result is `passed: True`. To run the prepared checks, run `class LessonTests`.

## Try to break it

Open `workspace/prices.py` and change the calculation by hand to `return price * quantity + 1`. Run `demo_check.py`. The tests fail, and `output` shows which value was expected and which came back. This is what a change looks like when it was written but is wrong. Then change the line to `return price * quantity` and run again: now `passed: True`. To repeat the whole pass with the model, put back the original `return price + quantity`.

## What we have now

`demo.py` now performs one full pass of a coding agent: read the file, get a proposal from the model, show the diff, ask for approval, apply and test. The program tells apart three states: a change proposed, a change written and a change that passed the checks. Real coding agents add repeated repair attempts and sandboxed execution, but their control points are the same.

The practical part of the course is complete. What it means for the work of an analyst, a manager and an administrator is in the [conclusion](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/conclusion.md). Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
