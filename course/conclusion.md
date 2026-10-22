# What we built and where it can help

In the first lesson we looked for the word "return" in three lines. By the end of the main route the program sends explicit requests to a model, runs only the tools it allows, passes tool results into the next request, enforces limits and records every step. In the last section the model proposes a code change, and the program shows the diff, asks for approval and runs the tests.

Every question from the MTS case in the introduction now has a place in the code where it can be answered. Is the clause in the policy? Look at the file and `read_notes`. Did the search find it? The journal of `find_notes`. What did the model receive? The messages from `build_messages` and the history chosen by `select_context`. What did it ask for, and what did the program allow? `dispatch_tool` and the event log. Who approved the change? `apply_change`.

## What the exercises made concrete

Having a document on the computer does not mean the model has seen its contents. Between the file and the answer there are specific operations: read, search, put into the request. If one of them is missing, asking the model more firmly will not help.

The model does not perform actions; it describes them. A dictionary with a tool name does nothing until the program decides to run it. That is why the boundaries live in code: which tools exist, which files are reachable, how many steps are allowed. A tool's result does not reach the model by itself either; the program has to put it into the next request.

A completed action and a verified result are different things. A written file can contain a bug, and a complete answer from a model can contain claims that are not in the source. Each case had its own check in the course: code tests, comparing the answer with the note, the event log, the control scenarios.

Python made it possible to try all this by hand. "Connect a source", "give the agent a tool" and "keep the history" now stand for familiar operations on files, lists, dictionaries and function calls.

## Diagnose an incorrect support answer

Back to [the MTS case](https://habr.com/ru/companies/ru_mts/articles/1051784/) from the introduction: the support agent suggested a workaround when a simple setting would have solved the problem. The team added the setting to its Confluence instructions, and similar requests were then handled correctly.

The order of investigation is now clear. Find the instruction and check that it contains the right paragraph. Check whether the search returned it. Look at what the program actually sent to the model. If the paragraph was not there, the source or the search needs attention. If it was there and the answer still contradicts it, look at the messages, the answering rule and the model itself.

A support specialist or analyst does not have to build the whole system to take part in such an investigation. They know the right resolution, can improve the document and can prepare a control case: the customer's request, the right source, an acceptable answer. The event log and the scenarios from section 4 make that check repeatable after the model or the search changes.

## Use AI to investigate a business process

In [Alfa-Bank's process-mining account](https://habr.com/ru/companies/alfa/articles/966570/) (in Russian), Andrey Shalyagin describes how an AI assistant first helped analysts write SQL and Python scripts without seeing the process data, and how the model was later connected to the analytics platform and given process context and metrics to suggest hypotheses.

Imagine a similar task of your own: a manager wants to know why request approvals take several days. The model can be given an export of stage durations and the documented approval procedure; one tool returns durations, another reads the procedure. If key information is missing, a clarifying question from the model is worth more than a confident explanation invented from the process name. And a conclusion such as "the delay is in approval" still has to be checked against real requests: waiting may depend on incomplete requests, weekends or the agreed working order.

The course does not build a connection to a corporate platform, but after it you know what to put into the requirements: which sources are needed, which fields, which operations are allowed and without which information a conclusion counts as unverified.

## Check whether the rollout paid off

In [an article about AI at Raiffeisen Bank](https://habr.com/ru/companies/raiffeisenbank/articles/1054656/) (in Russian), Marat Kinyabulatov points to an important trap: individual team members may work faster while the task still waits for requirements, testing, approval or another department. More AI usage does not by itself mean the whole process got faster.

The same thinking applies to a support pilot. Suppose the assistant drafts replies faster. How long does an agent spend checking each draft? How often must it be rewritten? Did repeat contacts go down? Does the customer get a resolution sooner?

The scenarios from lesson 4.4 extend naturally here: collect typical requests, agree on the right answers with specialists and record the result together with the time spent checking and fixing it. Successful completion of the program then becomes one signal among several, next to the usefulness of the answer and the outcome of the request. A manager can use this to decide which tasks the assistant can take on, where human review stays mandatory and which cases are better left to staff for now.

## What to try next

For your next practice, pick a familiar task where you can check the answer yourself: finding a rule in an internal instruction, drafting a reply to a request or matching records in an export. Start with copies of data you are allowed to use this way. Write down in advance what counts as a correct result, when the data is insufficient and which action needs approval.

Then follow the path you already know: prepare the source, pass it to the model, record its actions and check the result on several different cases. Change one significant thing at a time, so you can tell what helped: a better document, a different selection of data, a clearer instruction or another model.

The result of such work can be a task description for an integration that both developers and the client accept: what the system receives, what it does, when it hands the decision to a person and by which criteria its work is accepted.

## Next stage

In this course the model ran separately from the program: in a cloud service or in Ollama. In [stage 2, "The model inside your application"](https://github.com/polar-byter/agent-harness-advanced-1-en), the model is loaded straight into a Python program and runs on a laptop CPU without a network. You build real applications with it: a utility that sorts an Excel journal, routing of support requests to queues with a choice probability, a photo check for a return claim, a web service, voice message transcription and a Telegram bot. The store and its returns policy come along with you.

Return to [the lesson index](README.md).
