# Optional workbook: implement the prepared modules

> **Where we are.** In section 3 the model asks the program to run a search, and the program decides whether that is allowed. Part of that exchange came ready-made: the modules `decisions.py` and `transport.py`. This optional workbook is for writing them yourself.

Recall the task: a customer asks about returns, and the assistant must find the right policy clauses. The model returns a request - "run a search with the query return" - but the program reads the file and searches it. For that exchange to work, the program first tells the model which actions are available and how to ask for them, and afterwards parses the text of the model's reply. On the next request it also passes on the results of actions already taken, otherwise the model never learns what was found.

In the main starters, `decide_live` in `decisions.py` and the module `transport.py`, which talks to Ollama or a cloud service, do this for you. Here we write their parts one at a time and then assemble a working `decide_live`.

| Who does what | |
|---|---|
| Receives the task, the rules and earlier results | The model |
| Returns the text of a command with a tool name and a query | The model |
| Parses the command, checks it is allowed and runs the search | The program |
| Passes the results with the task in the next request | The program |
| Answers from the found clauses | The model |

| Lesson | What you write |
|---|---|
| [Build the decision messages](01-messages.md) | `build_decision_messages` in `decisions.py` |
| [Parse a command from model text](02-command.md) | `parse_decision` in `decisions.py` |
| [Send an HTTP request from Python](03-request.md) | `request_json` in `transport.py` |
| [Assemble decide_live](04-decision.md) | `decide_live` in `decisions.py` |

Each lesson has its own starter with earlier parts ready. The first two need no model: we look at the data before sending and after receiving. The last two start with an offline check and then make a real request through the saved connection.

Start after [connecting a model](../02-note-assistant/04-connect.md), or come back here when `decide_live` first appears in [the tool lesson](../03-tool-agent/01-tools.md). If you only want to read the ready code, see [how send_live works](../02-note-assistant/extra-send-live.md). Back to [all lessons](../README.md).
