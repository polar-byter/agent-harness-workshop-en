# AI terms through the note assistant

Articles about AI often name the same action in several ways. Each term below points to a place in our own code where you can see what it actually means. There is no need to learn the list in advance; come back when a term appears in a lesson or in something you are reading.

| Term | Where it shows up in the course |
|---|---|
| LLM, language model | The model our program sends messages to, local Qwen or a cloud model |
| Prompt | The answering rule in `build_messages` and the task given to the agent |
| Context, tokens | Everything the model gets in one request: rule, question, notes |
| Retrieval | `find_notes` selects the notes that match a query |
| RAG | Found notes are sent to the model together with the question |
| Grounding | Comparing the model's answer with the note we supplied |
| Hallucination | The model states something the supplied note does not contain |
| Tools | `read_notes` and `find_notes`, which the model may ask for |
| Guardrails | `dispatch_tool` rejects an unknown tool; `workspace_path` rejects an outside file |
| Agent loop, orchestration | `run_agent` decides when to call the model, when to run a tool and when to stop |
| Context engineering | `select_context` picks the part of the history the model will see |
| Tracing | The event log with every command and its result |
| Evals | `evaluate_cases` compares the agent's behavior with expected outcomes |
| Human in the loop | `apply_change` writes a change only after a person approves it |

Our versions are deliberately small, and it helps to know where they stop. Our line search is retrieval in its simplest form; production RAG systems add document ingestion, indexing and retrieval quality checks. Our JSONL event log shows what the program did; tracing platforms such as OpenTelemetry also link operations with IDs and record how long each took. Our hand-written JSON command format plays the role of native function calling. Our path check limits which files the program opens; running untrusted code safely needs a separate sandbox.

When you meet one of these words in a product description, ask the same question as in the course: which concrete mechanism does it refer to, and what does it actually check? See the [agent-loop lesson](03-tool-agent/02-cycle.md), the [execution controls](04-run-control/01-budget.md) and the [conclusion](conclusion.md).
