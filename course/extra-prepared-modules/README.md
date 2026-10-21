# Optional workbook: implement the prepared modules

In the main agent project, a person asks for Python notes. `decide_live` sends the task and previous tool results to a model; the model returns JSON describing a tool request or an answer. `dispatch_tool` and the loop then handle execution. This workbook opens up the connection and parsing code that the main path supplied ready-made.

| Lesson | What you implement |
|---|---|
| [Build decision messages](01-messages.md) | Task and history become explicit message content |
| [Parse a command](02-command.md) | JSON text becomes a checked dictionary |
| [Send an HTTP request](03-request.md) | A dictionary becomes request bytes and a parsed response |
| [Assemble decide_live](04-decision.md) | The pieces form one model-decision call |

Each lesson has an independent starter with its own current function paused. The first two work without a service. The later two include an offline check before an actual request through the saved connection. You can inspect the whole skeleton without assuming that every helper must be rewritten for the main course.

Keep the boundaries visible: building messages is not sending them; parsing JSON is not executing a tool; a complete service response is not proof of a correct answer. Return to [the main tool project](../03-tool-agent/01-tools.md) when you want to follow the full loop again.
