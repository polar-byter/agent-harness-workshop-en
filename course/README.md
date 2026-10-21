# Lessons and starters

Step by step we hand the program more of the work. First it finds notes, then a model answers from what was found, then the model asks the program to search on its own while the program enforces limits and keeps a log. In the last section an agent proposes a code change, and the program applies it only with your approval and runs the tests.

Each lesson answers one question from the MTS case that opens the [introduction](00-introduction.md): is the right line in the source, did the search find it, what did the model receive, who approved the action.

Every lesson has its own archive. Earlier parts are already working, and the current function is started and paused at `NotImplementedError`. You can keep working in your own project or open the lesson's archive in a new PyCharm window. If you lose track of the PyCharm windows, see [how to find a file and run an example](pycharm.md). Forgotten a term? There is a [list of terms](terms.md).

## Section 1. Searching notes

Did the program find the right line?

| Lesson | Starter |
|---|---|
| [Write a search function](01-note-search/01-search.md) | [lesson-01-01-search](../downloads/lesson-01-01-search.zip) |
| [Read notes from a file](01-note-search/02-read.md) | [lesson-01-02-read](../downloads/lesson-01-02-read.zip) |
| [Save a search result](01-note-search/03-journal.md) | [lesson-01-03-journal](../downloads/lesson-01-03-journal.zip) |
| [Connect reading, search and the journal](01-note-search/04-run.md) | [lesson-01-04-run](../downloads/lesson-01-04-run.zip) |

Optional: [let tests repeat the checks](01-note-search/extra-tests.md).

## Section 2. Answering from source notes

What did the model receive, and did it answer from the source?

| Lesson | Starter |
|---|---|
| [Send a question with its source notes](02-note-assistant/01-messages.md) | [lesson-02-01-messages](../downloads/lesson-02-01-messages.zip) |
| [Extract text from a service response](02-note-assistant/02-response.md) | [lesson-02-02-response](../downloads/lesson-02-02-response.zip) |
| [Connect the request and the answer](02-note-assistant/03-answer.md) | [lesson-02-03-answer](../downloads/lesson-02-03-answer.zip) |
| [Connect a real model](02-note-assistant/04-connect.md) | [lesson-02-04-connect](../downloads/lesson-02-04-connect.zip) |

Lesson 4 is required: from there on, the main examples use a real model through a cloud API or a local Ollama. Prepared answers stay only in `demo_check.py` files and tests, so you can check your code without a model.

After connecting a model you can optionally read [how send_live works](02-note-assistant/extra-send-live.md), [inspect request statistics](02-note-assistant/extra-usage.md) (starter [lesson-02-extra-usage](../downloads/lesson-02-extra-usage.zip)) or [run a model inside Python](02-note-assistant/extra-local.md) (starter [lesson-02-extra-local](../downloads/lesson-02-extra-local.zip)).

## Section 3. An agent chooses a tool

What did the model ask for, and what did the program allow?

| Lesson | Starter |
|---|---|
| [Execute a permitted tool request](03-tool-agent/01-tools.md) | [lesson-03-01-tools](../downloads/lesson-03-01-tools.zip) |
| [Return tool results to the model](03-tool-agent/02-cycle.md) | [lesson-03-02-cycle](../downloads/lesson-03-02-cycle.zip) |

Here the model's requests use a simple JSON format of our own. Native function calling in the big APIs follows the same idea: the model describes an action, the program performs it.

If you want to write the ready-made `decisions.py` and `transport.py` yourself, there is an [optional workbook](extra-prepared-modules/README.md) of four lessons, each with its own starter.

## Section 4. Controlling execution

When does the agent stop, what does it see at each step, and how do we check that it works?

| Lesson | Starter |
|---|---|
| [Limit the number of actions](04-run-control/01-budget.md) | [lesson-04-01-budget](../downloads/lesson-04-01-budget.zip) |
| [Choose history for the next request](04-run-control/02-context.md) | [lesson-04-02-context](../downloads/lesson-04-02-context.zip) |
| [Save the execution history](04-run-control/03-trace.md) | [lesson-04-03-trace](../downloads/lesson-04-03-trace.zip) |
| [Compare behavior across scenarios](04-run-control/04-evaluation.md) | [lesson-04-04-evaluation](../downloads/lesson-04-04-evaluation.zip) |

## Section 5. A coding agent

Which files may the agent touch, who approved the change, and does the code still work afterwards?

| Lesson | Starter |
|---|---|
| [Restrict the working folder](05-coding-harness/01-paths.md) | [lesson-05-01-paths](../downloads/lesson-05-01-paths.zip) |
| [Preview a proposed change](05-coding-harness/02-diff.md) | [lesson-05-02-diff](../downloads/lesson-05-02-diff.zip) |
| [Apply an approved proposal](05-coding-harness/03-apply.md) | [lesson-05-03-apply](../downloads/lesson-05-03-apply.zip) |
| [Check the changed project](05-coding-harness/04-verify.md) | [lesson-05-04-verify](../downloads/lesson-05-04-verify.zip) |

The agent makes one pass: proposal, review, approval, write, tests. Real coding agents add repeated repair attempts and sandboxed execution on top of the same control points.

## Optional: the prepared modules

| Lesson | Starter |
|---|---|
| [Build the decision messages](extra-prepared-modules/01-messages.md) | [lesson-extra-01-messages](../downloads/lesson-extra-01-messages.zip) |
| [Parse a command from model text](extra-prepared-modules/02-command.md) | [lesson-extra-02-command](../downloads/lesson-extra-02-command.zip) |
| [Send an HTTP request from Python](extra-prepared-modules/03-request.md) | [lesson-extra-03-request](../downloads/lesson-extra-03-request.zip) |
| [Assemble decide_live](extra-prepared-modules/04-decision.md) | [lesson-extra-04-decision](../downloads/lesson-extra-04-decision.zip) |

When you finish the main route, read [what we built and where it can help](conclusion.md).
