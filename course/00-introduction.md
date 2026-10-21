# AI agents in practice: how they act and how to check their work

Imagine a hiring team finds suitable applicants among the resumes its new AI assistant rejected. The first useful question is which information and criteria produced those rejections. We need to inspect the source documents, the instructions and the actual decisions before deciding what to change.

The same problem appears with less consequential tasks: a support answer contradicts a manual, a report omits a record, or a coding assistant changes more than expected. A convincing final paragraph gives us little evidence about the path that produced it. This workshop builds that path in small, observable steps.

## Why build a small assistant when a chat application already exists?

You can attach a file to a ready-made assistant and ask a question. The application already handles uploading, extracting text, building requests and displaying results. Those are useful capabilities, but they do not reveal their implementation.

We will build a simpler version so that you can follow the data yourself. A search function will select source lines; a connection will send them to a model; a loop will execute permitted tool requests and return their results. The exercise gives you a way to distinguish missing evidence, a code error and an unsupported generated answer.

## Model, harness and agent

A language model generates tokens conditioned on its input. Training gives it broad capabilities, but it does not automatically gain access to a file, database or application merely because we mention one. The surrounding program must provide the data or a permitted operation.

The **harness** is that surrounding application: it prepares messages, provides tools, handles responses, stores history and enforces stopping conditions. In our small agent, the model chooses a requested next action and Python coordinates its execution. Different systems use the word agent more broadly; the concrete exchange matters more than the label.

Two strong models can behave differently, and neither can be assumed to solve every task. The surrounding system also changes the outcome: whether it includes the correct source, makes an operation available, validates a request and returns its result. We will be able to change and inspect those parts independently.

## A request is not the whole instruction system

In a chat application you might type, "Find notes about Python." That is the current request, or prompt. The application can also supply persistent rules, such as answering from attached sources and distinguishing missing information from a negative result. Roles such as system, developer and user identify how a message is supplied; a project file is not automatically a system message merely because its name is AGENTS.md.

An agent application may read an **AGENTS.md** file and include its project instructions in the model context. A **skill** packages reusable guidance in a SKILL.md file and may include examples, scripts and other resources. The application discovers the skill, the model or application loads relevant instructions, and tools execute scripts when needed. A file sitting on disk has no effect unless the application reads or uses it.

That explains why Python is useful here beyond software development. It can turn a domain operation into something repeatable: read records, filter a list, compare values or prepare a report. A skill can explain when such a script should be used; the script can implement the calculation rather than asking a model to invent it anew.

## Our route

We start with file reading, search and a journal. Next we construct messages, extract an answer and connect a real model. The following projects add tool selection, an agent loop, limits, history selection and scenario checks. The last project previews a code change, asks permission to write it and runs tests.

You will complete one function at a time. Each lesson has a separate starter with earlier components prepared, concrete examples, a partial implementation and a hint for each missing part. Python explanations stay close to the operation you are writing. You can inspect the entire skeleton without having to implement everything at once.

The workshop does not reproduce a production platform. It gives you a working foundation for asking more precise questions about one: what it receives, what it is allowed to do, how it stops and what evidence supports acceptance. Those questions are useful when you own a process, specify an integration or evaluate a proposed automation.

Start with [the project setup](01-note-search/00-setup.md), or inspect [all lessons and starters](README.md). At the end, [the conclusion](conclusion.md) connects the exercises to published workplace examples.
