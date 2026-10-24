# Agent Harness Workshop

A course on how AI agents work and how to check their work. Step by step you write in Python a small assistant that answers customers from an online store's returns policy: a search tool, a connection to a real model, tool requests the program checks before running, an agent loop with limits and a log, and finally a coding agent whose change is applied only with your approval and then tested.

The course is for analysts, process owners and managers, system administrators, support and QA specialists, and programmers new to Python. Each lesson works on concrete data, gives you a started function and a hint for every gap.

**[Start here](course/00-introduction.md)** / **[All lessons](course/README.md)** / **[Who it is for](course/who-this-is-for.md)** / **[Results and applications](course/conclusion.md)**

## Learn directly from GitHub

Read the lessons in the browser. For practice, download a lesson's ZIP from the link in the lesson, or browse the matching folder under [exercises](exercises/README.md), then open that single project in PyCharm.

There are 18 main lessons, six optional exercises and 24 independent starters. In each starter the earlier parts already work, so you can take any lesson on its own.

## What you need

The main route uses Python 3.12 or newer, PyCharm and the standard library. The required connection lesson supports local Ollama, OpenRouter and VseGPT. A separate optional Windows x64 / Python 3.14 branch loads a pinned model library in the Python process.

English instructions, prompts, data, diagrams and starter archives are maintained here. The Russian edition remains separate. Provider choices and free offerings may change; follow the linked official instructions when connecting a service.

The repository checks cover links, packaging and the starters' unfinished state without calling a model. Your own solution is checked by the tests inside each exercise.

## Next stage

[Stage 2: the model inside your application](https://github.com/polar-byter/agent-harness-advanced-1-en) continues this course. The model is loaded straight into a Python program and runs on a laptop CPU without a network, and you build real applications with it: an Excel utility, routing of support requests to queues, a photo check, a web service, voice message transcription and a Telegram bot.

## License

Code is released under the [MIT License](LICENSE). Lesson texts and images are released under [CC BY-NC-SA 4.0](LICENSE-CONTENT.md): you may use and adapt them with credit, for non-commercial purposes, under the same license.
