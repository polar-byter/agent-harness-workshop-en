# Limit the number of actions

A model may keep requesting work without producing a final answer. We need an explicit stopping condition even when the model does not choose to stop. This lesson separates a request to be economical from counters enforced by the application.

## Open this starter

Download [this lesson starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-04-01-budget.zip), choose **Extract All**, and open the extracted `lesson-04-01-budget` folder with **File -> Open** in PyCharm. In **View -> Tool Windows -> Project**, find `control.py` -> `check_budget`. Earlier components are prepared; the current function deliberately pauses with `NotImplementedError`. Keep your previous project in its own folder. The main run uses the connection saved in the [required connection lesson](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/02-note-assistant/04-connect.md). The offline `demo_check.py` remains a separate code check.

## Follow the data

`state = {'steps': 2, 'tool_calls': 1}` and `limits = {'steps': 4, 'tool_calls': 2}` allow another iteration. Both current counts must be strictly less than their limits. A step counts a model decision; a tool call counts an executed operation. These are not token or currency budgets.

## Complete the function

Keep the prepared function header. Fill each `...` using the hints below, then remove the `raise NotImplementedError(...)` pause in the starter. The displayed fragment explains the function body; it is not a separate script to paste elsewhere.

```python
def check_budget(state: dict, limits: dict) -> bool:
    for name in ('steps', 'tool_calls'):
        if type(state.get(name)) is not int or state[name] < 0:
            raise ValueError('Invalid counter: ' + name)
        if type(limits.get(name)) is not int or limits[name] < 1:
            raise ValueError('Invalid limit: ' + name)
    steps_available = ...
    tools_available = ...
    return steps_available and tools_available
```

Keep the prepared validation of integer counters and positive limits. Return the conjunction of `state['steps'] < limits['steps']` and `state['tool_calls'] < limits['tool_calls']`.

The caller, `run_controlled`, updates the counts. Do not increment them in `check_budget`, which should only inspect them. Equality with either limit must return `False`; negative counts and invalid types raise errors rather than granting permission.

## Run and inspect

Open `demo.py` directly under **Project -> lesson-04-01-budget**, right-click in its editor and choose **Run 'demo'**. Read the result in **View -> Tool Windows -> Run**. A `Complete ...` message means the exercise pause is still present.

Run the live demonstration and inspect its final state. In the offline checks, verify the boundary where a count equals its limit. When the budget is exhausted, the controlling function returns `'budget_limit'` and does not start another decision request. That outcome may be correct even if no final answer was produced.

After a successful demonstration, optionally open the relevant file under `tests`, right-click its test class and run it. Those checks repeat defined expectations; they do not certify every possible input or every model answer.
