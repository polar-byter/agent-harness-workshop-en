# What we built and where it can help

We began by finding a word in a few lines. The main route ends with programs that send explicit model requests, execute permitted operations, return tool results and preserve history. The coding project adds a preview, approval and a test report. We can follow that path instead of judging the system only by its final paragraph.

## What the exercises made concrete

We separated a file path from file contents, and retrieved evidence from the answer generated about it. We saw that mentioning a file does not put its text in a model request. We also separated a proposed action from an executed one: the model returns a description, while Python checks and performs it.

The loop made another boundary visible. A tool result reaches the model only when the next request includes it. The application controls that history and enforces a stopping condition. Later, a written file and a checked change became separate outcomes. Tests, source comparison and scenario evaluation check different kinds of correctness.

Python supplied a way to examine those distinctions directly. For someone specifying or evaluating an integration, the same distinctions become concrete requirements: input fields, permitted operations, missing-data conditions, approval points and evidence for acceptance.

## Diagnose an incorrect support answer

In a [first-hand MTS Web Services account](https://habr.com/ru/companies/ru_mts/articles/1051784/), Vladimir Drobot describes an assistant that suggested adding dummy records or requesting a feature change. The actual solution was an existing setting. The team updated its Confluence instructions and reported that similar requests were then handled correctly.

Our exercises suggest a diagnostic sequence: locate the right document, check whether retrieval selected it, inspect the text actually sent, then compare the generated advice with that evidence. A domain specialist can supply the correct resolution and build a repeatable acceptance case without implementing the entire application. The article is a specific team's experience, not a general accuracy guarantee.

## Prepare evidence for process analysis

In [Alfa-Bank's process-mining account](https://habr.com/ru/companies/alfa/articles/966570/), Andrey Shalyagin describes moving from a separate assistant for scripts to an integration that supplies process context and metrics to a model. The generated hypotheses give analysts starting points for investigation.

For our own example, suppose approval requests take several days. An analyst could prepare stage durations and the actual approval policy, then ask for hypotheses supported by those records. Missing information should lead to a qualification or follow-up request, not a confident invented cause. This example illustrates the method; it is not a reported result from that bank.

The course does not implement that corporate integration. It helps specify the sources, fields and operations needed to make one inspectable. The analyst still checks hypotheses against real cases and the people who perform the work.

## Evaluate the whole workflow

In a [Raiffeisen Bank account](https://habr.com/ru/companies/raiffeisenbank/articles/1054656/), Marat Kinyabulatov explains why faster individual tasks need not make the whole delivery process faster: work can still wait for requirements, review, testing or another team.

Apply that question to a support pilot. Faster drafting is useful, but record review time, corrections, repeat contacts and time to an actual resolution too. These are proposed measures for this example, not outcomes claimed by the banking article. Our scenario checks provide a small starting point: define the expected outcome before running and preserve the actual result.

A manager can use that evidence to decide which cases can proceed automatically and which need human review. An analyst can translate it into acceptance criteria rather than relying on an attractive demonstration.

## Choose a next experiment

Pick a familiar, checkable task: find a rule in an internal instruction, draft an answer from approved material or compare records in a permitted sample. Write down what counts as correct, what information may be missing and which action needs approval. Start with copies of data you are allowed to use.

Follow the same path: prepare the source, send explicit data, record actions and compare results across several cases. Change one substantial factor at a time. That will help distinguish an improved document, retrieval rule, instruction or model from a lucky answer.

You can continue as an analyst, process owner or member of an implementation team. The useful output is a testable description of what the system receives, does, records and hands back to a person. Return to [the lesson index](README.md) when you need to revisit a particular mechanism.
