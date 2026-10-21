# AI agents in practice: how they get work done and how to check it

Vladimir Drobot of MTS Web Services describes a telling case in [an article about their support agent](https://habr.com/ru/companies/ru_mts/articles/1051784/) (in Russian). A customer could not upload a short list, and the agent advised adding dummy records or ordering a custom change. In fact, the limit could be switched off with an ordinary setting in the customer's account. Once the team added that to the instructions the agent relied on, similar requests were handled correctly.

The model stayed the same; only the document changed. Yet a wrong answer like that could have had other causes. The right paragraph might have been in the instructions and the search missed it. The search might have found it and the program never passed it to the model. Or the model might have received it and answered its own way anyway - what people call a hallucination. From the outside all of these look identical, and each needs a different fix. This course is about telling them apart.

## Why look inside an agent

AI agents are already being built into support desks, document work and server administration. Yet a language model, an LLM, can do exactly one thing on its own: take text in and produce text out. Reading a knowledge base, calling an API, running commands and deciding when to stop are all done by the program around the model. English-language articles call that program a harness. It decides what goes into the model's context, which actions the model may take and what ends up in the logs. So when an agent gets something wrong, the cause is usually somewhere in the harness.

**If you own a process or manage a team**, what matters most is control. An agent you only know as "it handles everything" is a black box, and trusting it means giving up control over work you are still accountable for. In 2024 a Canadian tribunal ordered Air Canada to compensate a customer whose refund question its website chatbot had answered wrongly ([The Guardian](https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit)). The airline could not shift the blame onto the bot. A manager who understands how an agent is built knows where its control points are: what data it receives, what it is allowed to do, where it must stop and ask a person, where each of its steps is recorded. When something goes wrong, you know where to step in - and a vendor can no longer get by with an impressive demo, because you know which logs, checks and limits to ask for.

**If you are a business or systems analyst**, this understanding sets you apart. Plenty of analysts can write requirements for an ordinary integration. Far fewer understand how an integration with an LLM works, and it shows as soon as a task is being specified. Such an analyst will not settle for "the bot should answer correctly". They ask which documents go into the context, what happens when the information is missing and where a person has to step in. Developers can work with them in the same language, and the client gets a specification that can be estimated and accepted. That is the analyst who gets invited into an AI project at the start.

**If you are a system administrator or DevOps engineer**, agents are already arriving as tools that read logs, restart services and run terminal commands. They are wired in through function calling or MCP servers, but the principle is the same everywhere: the model only asks for an action, and a program carries it out. Whoever understands that is the person who answers the key question for the team - may this agent touch our servers, and on what terms. Access rights and bans on dangerous commands belong in the harness code; a line in the prompt is no protection. An agent can also be tricked by prompt injection, an instruction hidden in a log file it reads. You will know what to ask before giving it access to production.

**If you work in support or testing**, you will be able to move from "the bot got it wrong again" to a precise diagnosis: at which step it failed and what needs fixing - the document, the search or the model's instructions. Someone who can build a set of control questions, called evals, and rerun them after every change becomes indispensable to the team rolling the system out.

Much of this only becomes clear in practice. An instruction to "answer only from the documents" does not guarantee the model will obey it. A search result does not reach the model by itself; the program has to put it into the next request. And a model's request for an action stays plain text until the program decides to carry it out. Reading that a model can answer beyond its sources is one thing; seeing it happen on your own data is another.

## What we will build

You may already have attached a document to a chatbot and asked it to find a passage. For one-off work that is enough. But a chat window does not show you what the application actually sent to the model or what it did with the reply. So in this course we write, step by step in Python, a small assistant that answers questions from a set of notes, and we can check every part of it ourselves.

First the program learns to find relevant lines in a text file - the simplest form of what articles call RAG, searching a knowledge base before answering. Then we pass what was found to a model together with a question and check whether it answers from the source. Next the model starts asking the program to run the search itself, while the program decides whether the action is allowed, limits the number of steps in the agent loop and records what happens. In the last section the assistant proposes a change to a small piece of code, and the program applies it only with your approval and then runs the tests. That is, in miniature, how Claude Code, Cursor and other coding agents work.

You can connect the model through a cloud API or run it on your own computer with Ollama. Registering with a cloud service or paying for requests is not required.

By the end you will have a place in the code for every question from the MTS case: where the right paragraph lived, whether the search found it, what the model received and who approved the action.

## The model and the program around it

Two words before we start. A model, or LLM, is a neural network: it receives text and returns text, but it does not open files or run anything itself. Everything else is done by the program around it: it decides what to send, receives the reply and carries out what the model asked for. In a chatbot the application does this quietly for you; in this course we write it ourselves.

Other terms - prompt, context, tools, guardrails - come up as we go, each one once there is code behind it that you have already run. If you forget one, look it up in the [list of terms](terms.md). What you need on your computer is described in [who this course is for](who-this-is-for.md), and the whole route is in the [lesson index](README.md).

## Where we begin

First we open the training project in PyCharm and make sure Python runs. Then we write the first function: a search through the notes by keyword. That is where the chain from the MTS case starts: did the program find the right line?

-> [Open the first project](01-note-search/00-setup.md)
