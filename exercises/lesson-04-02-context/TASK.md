# Choose history for the next request

> **Where we are.** The agent loop has a step limit. Now we look at what the model receives at each step: the whole history so far, or only part of it.
> `history -> [choose a part] -> model -> action -> history ...`

After several actions the assistant has a history of tool requests and their results. If every request carries all of it, requests keep growing, and with them time and cost. If a request carries too little, the model loses information it needs, such as a clause it found three steps ago, and asks for the same search again.

Let us try a simple rule: always send the original task, and from the history only the latest events. `select_context` prepares that selection without touching the full history the program keeps. When an agent repeats itself or forgets what it has already done, this is often where the cause lies: in what it was given.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-04-02-context.zip), extract it and open the `lesson-04-02-context` folder in PyCharm. The current task is `select_context` in `control.py`.

## Look at the data

Take a history of three events and keep the last two. To make the selection visible, the events are just numbered:

```python
events = [{'step': 1}, {'step': 2}, {'step': 3}]
events[-2:]   # [{'step': 2}, {'step': 3}]
```

In a real history each element is a dictionary with a command and a result, and it is kept or dropped as a whole. How many events to keep is set by `max_events`; the task `task` is always included. Whatever is left out, the model does not see in this request.

## Your turn

`select_context` already checks `max_events` and creates `context` with the task and an empty list of events. Replace `raise NotImplementedError(...)` with the code below and fill in the gap:

```python
    if max_events > 0:
        context['events'] = ...
    return context
```

Use the slice `events[-max_events:]`. Square brackets with a colon create a new list from part of the old one: `-2:` means "the last two". `events` itself does not change.

The `max_events > 0` condition is needed because of a Python quirk: `events[-0:]` is the same as `events[0:]`, the whole list. Without the check, a limit of zero would send the model everything.

## Run it with the model

Open `demo.py` and choose **Run 'demo'**. Before each request to the model, the program calls your function. The Run window shows the status, the answer and the history. Look at which events the chosen `max_events` keeps: the ones left out were not visible to the model in that request.

## Check the function on its own

Open `demo_check.py` and choose **Run 'demo_check'**. We expect the task unchanged and the last two events, steps 2 and 3. To run the prepared checks, run `class LessonTests` in `tests/test_lesson.py`.

## Try to break it

In `demo_check.py` change the last argument of the call from `2` to `0`. We expect an empty list of events. Now temporarily remove the `if max_events > 0:` line from your function (leaving the assignment unindented) and run again: the whole history comes back. Restore the condition.

## What we have now

The program decides what the model sees at the next step. This is part of what is called **context engineering**: choosing which instructions, sources and history go into each request. "Latest events" is the simplest possible rule and does not weigh how important each piece is, but it shows exactly where the decision is made.

Next: [save the execution history](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/04-run-control/03-trace.md). Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
