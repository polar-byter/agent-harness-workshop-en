# Lessons and independent starters

Start with [the introduction](00-introduction.md) and [open the first project](01-note-search/00-setup.md). Each archive prepares previous components and leaves the current exercise unfinished.

## Searching notes

| Lesson | Starter |
|---|---|
| [Write a search function](01-note-search/01-search.md) | [lesson-01-01-search](../downloads/lesson-01-01-search.zip) |
| [Read notes from a file](01-note-search/02-read.md) | [lesson-01-02-read](../downloads/lesson-01-02-read.zip) |
| [Save a search result](01-note-search/03-journal.md) | [lesson-01-03-journal](../downloads/lesson-01-03-journal.zip) |
| [Connect reading, search and the journal](01-note-search/04-run.md) | [lesson-01-04-run](../downloads/lesson-01-04-run.zip) |

## Answering from source notes

| Lesson | Starter |
|---|---|
| [Send a question with its source notes](02-note-assistant/01-messages.md) | [lesson-02-01-messages](../downloads/lesson-02-01-messages.zip) |
| [Extract text from a service response](02-note-assistant/02-response.md) | [lesson-02-02-response](../downloads/lesson-02-02-response.zip) |
| [Connect the request and the answer](02-note-assistant/03-answer.md) | [lesson-02-03-answer](../downloads/lesson-02-03-answer.zip) |
| [Connect a real model](02-note-assistant/04-connect.md) | [lesson-02-04-connect](../downloads/lesson-02-04-connect.zip) |
| [Inspect request statistics](02-note-assistant/extra-usage.md) | [lesson-02-extra-usage](../downloads/lesson-02-extra-usage.zip) |
| [Run a model inside Python](02-note-assistant/extra-local.md) | [lesson-02-extra-local](../downloads/lesson-02-extra-local.zip) |

## An agent chooses a tool

| Lesson | Starter |
|---|---|
| [Execute a permitted tool request](03-tool-agent/01-tools.md) | [lesson-03-01-tools](../downloads/lesson-03-01-tools.zip) |
| [Return tool results to the model](03-tool-agent/02-cycle.md) | [lesson-03-02-cycle](../downloads/lesson-03-02-cycle.zip) |

## Controlling execution

| Lesson | Starter |
|---|---|
| [Limit the number of actions](04-run-control/01-budget.md) | [lesson-04-01-budget](../downloads/lesson-04-01-budget.zip) |
| [Choose history for the next request](04-run-control/02-context.md) | [lesson-04-02-context](../downloads/lesson-04-02-context.zip) |
| [Save the execution history](04-run-control/03-trace.md) | [lesson-04-03-trace](../downloads/lesson-04-03-trace.zip) |
| [Compare behavior across scenarios](04-run-control/04-evaluation.md) | [lesson-04-04-evaluation](../downloads/lesson-04-04-evaluation.zip) |

## A coding assistant

| Lesson | Starter |
|---|---|
| [Restrict the working folder](05-coding-harness/01-paths.md) | [lesson-05-01-paths](../downloads/lesson-05-01-paths.zip) |
| [Preview a proposed change](05-coding-harness/02-diff.md) | [lesson-05-02-diff](../downloads/lesson-05-02-diff.zip) |
| [Apply an approved proposal](05-coding-harness/03-apply.md) | [lesson-05-03-apply](../downloads/lesson-05-03-apply.zip) |
| [Check the changed project](05-coding-harness/04-verify.md) | [lesson-05-04-verify](../downloads/lesson-05-04-verify.zip) |

## Optional: prepared modules

| Lesson | Starter |
|---|---|
| [Build the decision messages](extra-prepared-modules/01-messages.md) | [lesson-extra-01-messages](../downloads/lesson-extra-01-messages.zip) |
| [Parse a command from model text](extra-prepared-modules/02-command.md) | [lesson-extra-02-command](../downloads/lesson-extra-02-command.zip) |
| [Send an HTTP request from Python](extra-prepared-modules/03-request.md) | [lesson-extra-03-request](../downloads/lesson-extra-03-request.zip) |
| [Assemble decide_live](extra-prepared-modules/04-decision.md) | [lesson-extra-04-decision](../downloads/lesson-extra-04-decision.zip) |

The 18 main lessons include the required real-model connection. Six additional exercises cover statistics, embedded inference and the prepared modules. Fixed responses belong to offline checks; main agent demos use the saved connection. The command protocol is educational JSON, not native API function calling. The last project performs one approved change and test pass, without autonomous retries or a sandbox.

Finish with [what we built and where it can help](conclusion.md).
