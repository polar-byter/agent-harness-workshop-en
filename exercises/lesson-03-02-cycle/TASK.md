# Return tool results to the model

> **Where we are.** The program carries out the model's request to search the notes, but what it found stays with the program. Today we close the loop: the search result goes back to the model so it can answer.
> `task -> model -> search -> [result -> model again] -> answer`

This is exactly where the right paragraph could get lost in the MTS case: the search found it and it never reached the model. The model does not remember earlier requests. Send it the task "find notes about Python" again on its own, and it does not know the search already ran, so it asks for it again.

So the program keeps a history: every command from the model together with the result of carrying it out. On the next request the model gets the original task and that history. Then it can answer from the found notes or ask for one more action. Repeating this exchange is what is called the agent loop.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-03-02-cycle.zip), extract it and open the `lesson-03-02-cycle` folder in PyCharm. The current task is `run_agent` in `agent.py`; `dispatch_tool` from the previous lesson is ready.

## How the loop works

```text
Task and history -> model's decision
                       |
             +---------+---------+
             |                   |
       request a tool      final answer
             |                   |
       run the search          done
             |
       result into history
             |
       model's next decision
```

`run_agent` runs this loop. At each step it calls `decide` to get the model's decision. A final answer ends the work. A tool request is carried out by `dispatch_tool`, and the command and result are added to the list `events`. The number of steps is limited by `max_steps`: if the model never answers, the program stops on its own.

## Look at the data

`decide` receives the task `task` and the history `events` and returns the next command or a final answer. In `demo.py` this is `decide_live`, which calls the model; in `demo_check.py` it is `decide_fixture`, whose behavior is known in advance: on the first step it asks for a search, on the second it answers.

One event in the history looks like this:

```python
events.append({'command': {'tool': 'find_notes', 'query': 'python'},
               'result': {'matches': ['Python functions return values.', 'Python lists keep item order.']}})
```

The animation shows the task, the command and both found notes going into the next request, while the request counter grows from one to two. A real model may take another route, for example reading all the notes first.

## Your turn

`run_agent` already checks `max_steps` and creates the empty list `events`. Replace `raise NotImplementedError(...)` with the loop and fill in two gaps:

```python
    for step in range(max_steps):
        command = decide(task, events)
        if command.get('type') == 'answer':
            text = command.get('text')
            if not isinstance(text, str) or not text.strip():
                raise ValueError('Empty answer')
            return {'status': 'completed', 'answer': text, 'events': events}
        if command.get('type') != 'tool':
            raise ValueError('Expected an answer or a tool request')
        result = ...
        events.append({'command': ..., 'result': ...})
    return {'status': 'step_limit', 'answer': '', 'events': events}
```

1. `result` gets `dispatch_tool(command, notes_path)`.
2. The event holds the variables `command` and `result`.

`range(max_steps)` sets how many times the loop may ask the model. The `return` inside the answer branch ends the whole function at once. The last `return`, after the loop, runs only when the steps ran out without an answer: the status is then `step_limit`.

In the offline example, `events` is empty on the first step and `decide_fixture` asks for a search. Your code runs it and records the event. On the second step `decide` receives a non-empty history and returns an answer. In a real run, `decide_live` puts the history into the messages for the model, so the found notes really reach it. Without the recorded event, they would simply not be in the next request.

## Run it with the model

Open `demo.py` and choose **Run 'demo'**. Now the whole loop runs: the model chooses an action, the program carries it out, and the result returns to the model. The Run window shows the events and the final result. We expect an answer based on the found notes; the exact words and the number of steps may vary. A `step_limit` status is a result too: the events show what the model did instead of answering.

## Check the function on its own

Open `demo_check.py` and choose **Run 'demo_check'**. We expect status `completed`, the answer "Found two notes about Python." and one event: the search command and its result. To run the prepared checks, run `class LessonTests` in `tests/test_lesson.py`.

## Try to break it

Comment out the `events.append(...)` line in your code by putting `#` in front of it and run `demo_check.py`. `decide_fixture` now always receives an empty history, asks for the search every time, and the loop ends with `step_limit`. That is what an agent looks like when it cannot see the results of its own actions. Remove the `#`.

## What we have now

The assistant has an agent loop: the model decides, the program acts, the result goes back to the model. Coordinating these steps is called **orchestration**: the code decides when to call the model, when to run a tool, what to pass on and when to stop. Ours is an ordinary Python loop; larger systems use libraries such as LangGraph for the same job.

Next section: [limit the number of actions](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/04-run-control/01-budget.md). Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
