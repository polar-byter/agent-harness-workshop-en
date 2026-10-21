# AI terms through the note assistant

These terms describe mechanisms we can point to in our own application. Use them after following the corresponding data flow rather than as substitutes for it.

| Term | Concrete meaning here |
|---|---|
| Model | Generates a response from the messages we supply |
| Harness | Code that prepares input, provides tools, tracks history and controls execution |
| Agent loop | Decide, execute a requested tool, record its result, decide again |
| Retrieval | Select source notes before asking for an answer |
| Grounding | Relate an answer to supplied evidence; a request to do so is not a guarantee |
| Guardrail | A particular enforced check, such as rejecting an unknown tool name |
| Orchestration | The caller coordinates model requests, tool execution and termination |
| Context engineering | Choose and arrange the information included in a request |
| Tracing | Record visible actions and results so a run can be investigated |
| Evals | Compare behavior on defined cases against suitable criteria |
| Human in the loop | A person makes a specific decision, such as approving a proposed file write |

Our line search is a simple retrieval example, not a complete production RAG system with ingestion, indexing and retrieval evaluation. Our JSONL journal is not a distributed tracing platform. Our hand-written JSON command protocol is not the API's native function-calling protocol. The path check is not process isolation.

Those distinctions help read product descriptions: ask which concrete mechanism a term refers to and what the implementation actually checks. See the [agent-loop lesson](03-tool-agent/02-cycle.md), [execution controls](04-run-control/01-budget.md) and [course conclusion](conclusion.md).
