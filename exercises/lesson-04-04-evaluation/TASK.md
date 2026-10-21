# Compare behavior across scenarios

> **Where we are.** The agent runs in a limited loop and its actions are logged. The last step of this section: checking whether a change made the agent better.
> `set of tasks -> agent -> [compare with expectations] -> report`

Say you adjusted the instructions and the assistant now answers the question about Python lists better. Is it better overall? It may have stopped saying "no information" when the notes have none, or started hitting the step limit more often. One good answer is easy to notice; a regression on other questions slips by without a repeatable check.

So we prepare a set of scenarios and agree, before running anything, on the right outcome for each. `evaluate_cases` runs the tasks, compares the results with the expectations and builds a report. This is what analysts call acceptance criteria: a list of cases by which an agent is accepted or sent back for more work.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-04-04-evaluation.zip), extract it and open the `lesson-04-04-evaluation` folder in PyCharm. The current task is `evaluate_cases` in `control.py`.

## Look at the data

A scenario is a dictionary with a name, a task and the expected result:

```python
case = {'name': 'Answer', 'task': 'Find Python',
        'expected_status': 'completed', 'expected_answer': 'Done'}
```

A list of these goes into the `cases` parameter. With it the function receives `run`, a function that performs a task and returns the actual result with a status and an answer. Those two fields are compared with the expectation.

Exact comparison works only for short answers agreed in advance. That is why `demo.py` asks the model to reply with a single word: `found` if notes were found and `missing` if not. Free-form answers need other criteria.

## Your turn

`evaluate_cases` already has the empty list `results`. Replace `raise NotImplementedError(...)` with the code below and fill in the gap:

```python
    for case in cases:
        actual = run(case['task'])
        passed = ...
        results.append({'name': case['name'], 'passed': passed})
    passed_count = sum(item['passed'] for item in results)
    return {'passed': passed_count, 'total': len(results), 'results': results}
```

For `passed`, join two comparisons with `and`: `actual['status'] == case['expected_status']` and `actual['answer'] == case['expected_answer']`. A scenario passes only when both fields match. Double `==` compares values; single `=` assigns.

`run(case['task'])` calls the passed-in function just as `send(messages)` did in section 2. `sum(...)` adds up boolean values: `True` counts as one and `False` as zero, which gives the number of passed scenarios.

## Run it with the model

Open `demo.py` and choose **Run 'demo'**. It has two scenarios for the real model: find notes about Python and reply `found`, and search for `zzz_not_in_notes` and reply `missing`. Your function compares the actual results with the expectations.

**Guess before running:** will the model pass both scenarios?

`passed` may come out lower than `total`. That is not a bug in your function but the result of testing the model: it may have answered with a full sentence instead of one word. A scenario can take several requests to the model, so keep your service quota in mind.

## Check the function on its own

Open `demo_check.py` and choose **Run 'demo_check'**. Its behavior is fixed in advance, so we expect:

```text
{'passed': 2, 'total': 2, 'results': [{'name': 'Answer', 'passed': True}, {'name': 'Stop', 'passed': True}]}
```

The second scenario checks stopping at the limit: the agent keeps asking to read the notes, and the correct result there is the status `budget_limit`. To run the prepared checks, run `class LessonTests` in `tests/test_lesson.py`.

## Try to break it

In `demo_check.py`, change the expected answer of the first scenario from `'Done'` to `'Done.'` with a full stop and run again. That scenario fails: for exact comparison, an extra full stop makes a different answer. That is why free-form answers need other criteria. Put the original value back.

## What we have now

The assistant has a set of control scenarios to check any change against: a new instruction, another model, an edited note. Evaluating AI behavior against criteria set in advance is called **evaluation**, or evals. Keep the two kinds of check apart: the tests in `tests` check that your code counts results correctly, and running `demo.py` checks whether the model handled the scenarios.

Next section: an agent that changes code. [Restrict the working folder](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/05-coding-harness/01-paths.md). Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
