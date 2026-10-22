"""Concrete illustrative data for the course animations, not recorded model runs."""
STORIES = []
FOLDERS = ['01-note-search', '02-note-assistant', '03-tool-agent', '04-run-control', '05-coding-harness', 'extra-prepared-modules']


def step(action, before, after, explanation, packet='data'):
    return dict(action=action, source='Before this operation', before=before,
                destination='After this operation', after=after, explanation=explanation, packet=packet)


def story(group, name, title, *scenes):
    folder = FOLDERS[group - 1] + '/' if group else ''
    STORIES.append(dict(path='assets/' + folder + name + '.gif', title=title, scenes=list(scenes)))


story(1, 'function-inputs', 'Arguments become function parameters',
      step('Call find_notes(notes, query)', 'notes: ["Returns are accepted...",\n        "Delivery within the city...", "RETURNED money..."]\nquery: " Return "',
           'First argument -> notes\nSecond argument -> query', 'The caller supplies values; the function receives them through its parameters.', 'arguments'),
      step('Normalize the query', '" Return "', '"return"', 'strip removes edge spaces; casefold supports case-insensitive comparison.', 'strip / casefold'),
      step('Return matching source lines', '["Returns are accepted...",\n "RETURNED money..."]', 'The caller receives a list.', 'Returning a value is separate from printing it.', 'return'))

search = [step('Prepare the query and result list', 'query = " Return "', 'query = "return"\nselected = []', 'Keep original source lines for the returned list.', 'prepare'),
          step('Check the first clause', '"return" in "returns are accepted..." -> True', '["Returns are accepted..."]', 'Append the original matching line.', 'append'),
          step('Check the second clause', '"return" in "delivery within the city..." -> False', '["Returns are accepted..."]', 'No match: the result list stays unchanged.', 'skip'),
          step('Check the third clause', '"return" in "returned money..." -> True', '["Returns are accepted...",\n "RETURNED money..."]', 'Append the second match, then return after the loop.', 'append / return')]
story(1, 'search-notes', 'Search builds a result list', *search)
read = [step('Read notes.txt (_ marks a space)', '__Delivery within the city...\n(empty line)\nRETURNED money...', '"__Delivery within the city...\\n\\nRETURNED money...\\n"', 'read_text returns one string; \\n represents a line break.', 'read_text'),
        step('Split the text into lines', '"__Delivery within the city...\\n\\nRETURNED money...\\n"', '["__Delivery within the city...", "",\n "RETURNED money..."]', 'The empty line becomes an empty element; leading spaces stay.', 'splitlines'),
        step('Keep nonempty trimmed lines', '["__Delivery within the city...", "",\n "RETURNED money..."]', '["Delivery within the city...",\n "RETURNED money..."]', 'Return the prepared list to the caller.', 'strip / return')]
story(1, 'read-notes', 'From a file to a list of notes', *read)
story(1, 'read-data', 'A file, a string and a list differ', *read)
story(1, 'lesson-03-journal', 'Append a search journal record',
      step('Serialize the supplied result', 'query: "return"\nmatches: ["Returns are accepted..."]', '{"query":"return",\n "matches":["Returns are accepted..."]}', 'The result dictionary becomes a JSON string.', 'json.dumps'),
      step('Append a line to runs.jsonl', 'Existing record for "refund to cash"', 'Existing record for "refund to cash"\nNew record for "return"', 'Mode a preserves earlier records; add a line break to the new one.', 'write'),
      step('Inspect the two runs', 'Two separate JSONL records', 'The query "refund to cash" found nothing.\nThe query "return" found one clause.', 'The journal preserves each supplied result.', 'read'))
story(1, 'lesson-04-run', 'Connect reading, search and a record',
      step('Read the selected source', 'notes_path: data/notes.txt', 'A list of note strings', 'A path identifies a source; search needs its contents.', 'read_notes'),
      step('Search for " return "', 'The list and query', '["Returns are accepted...",\n "RETURNED money...",\n "A receipt or order number..."]', 'Comparison ignores edge spaces and letter case.', 'find_notes'),
      step('Save and return the result', 'query, status, matches', 'write_result -> runs.jsonl\nreturn result -> caller', 'Writing the file and returning the dictionary are separate actions.', 'write / return'))
story(1, 'test-result', 'Compare a result with an expectation',
      step('Define a known case', '["Returns are accepted...",\n "Delivery within the city..."]\nquery: "return"', 'Expected: ["Returns are accepted..."]', 'The expectation describes this specific input.', 'input'),
      step('Call the search function', 'find_notes(notes, query)', 'Actual: ["Returns are accepted..."]', 'This example shows a correct implementation.', 'return'),
      step('Compare both lists', 'Expected and actual lists', 'Equal: this test passes.\nReturning [] would fail.', 'A passing test checks its case, not every possible input.', 'assertEqual'))
story(2, 'lesson-01-messages', 'Separate instruction and source data',
      step('Prepare the answering rule', 'Answer only from the supplied notes.', 'developer: source-only instruction', 'The instruction is separate from the source text.', 'rule'),
      step('Serialize the question and notes', 'question: "How many days to return an item?"\nnotes: ["Returns are accepted within 14 days."]', 'user: JSON with question and notes', 'The original note is part of the model input.', 'JSON'),
      step('Return the message list', 'One rule message and one data message', '[developer message, user message]', 'The connection later adapts developer to system for these backends.', 'return'))
story(2, 'lesson-02-response', 'Extract text from a response',
      step('Check completion', 'status: "completed"\noutput: a list of items', 'Inspect message items in output.', 'The full response contains structure as well as text.', 'status'),
      step('Select output_text parts', 'message -> content -> output_text', '["You can return an item within 14 days."]', 'Ignore unrelated service elements.', 'text part'),
      step('Join and return the text', 'A list of answer fragments', '"You can return an item within 14 days."', 'The caller now receives a string, not the response dictionary.', 'join / return'))
story(2, 'lesson-03-answer', 'From a question to an answer string',
      step('Build messages', 'Question + source note', 'Instruction message + data message', 'The source note becomes explicit request content.', 'messages'),
      step('Call the supplied sending function', 'send(messages)', 'A normalized response dictionary', 'A fixture checks the code; send_live makes a real request.', 'request / response'),
      step('Extract and return the answer', 'extract_answer(response)', '"You can return an item within 14 days."', 'The sentence is illustrative; live wording may differ.', 'return'))
story(2, 'lesson-04-connect', 'Use the saved model connection',
      step('Save the chosen connection', 'Provider: Ollama\nModel: qwen3:0.6b', 'A user settings file outside the starter', 'The English course shares its own selection across lessons.', 'save'),
      step('Run demo.py', 'send_live(messages)', 'A request to the chosen local or API service', 'The settings determine the endpoint and model ID.', 'POST'),
      step('Read the generated answer', 'Provider response', 'Extracted text appears in Run.', 'A working connection does not guarantee a correct answer.', 'answer'))
story(2, 'lesson-04-instruction-flow', 'Follow the instruction to the model',
      step('Build the source-only rule', 'build_messages', 'developer: answer from notes only', 'The application supplies the rule as a separate message.', 'rule'),
      step('Adapt roles for the connection', 'developer: rule\nuser: question and notes', 'system: the same rule\nuser: the same question and notes', 'The adapter changes the role, not the instruction text.', 'roles'),
      step('Check the actual answer', 'Rule + question + source note', 'Compare generated text with the note.', 'Receiving a rule and following it are different outcomes.', 'generation'))
story(2, 'lesson-04-usage-flow', 'Reported counts reach the console',
      step('Collect available counts', 'Provider response; illustrative values', 'input_tokens: 128\noutput_tokens: 32\ncached_tokens: None', 'These are teaching values, not recorded measurements.', 'usage'),
      step('Format the values', '128, 32 and None', 'Input tokens: 128\nOutput tokens: 32\nCached tokens: not reported', 'None means unavailable, not zero.', 'format_usage'),
      step('Print the returned lines', 'A list of formatted strings', 'Input tokens: 128\nOutput tokens: 32\nCached tokens: not reported', 'Printing does not measure attention or infer missing counts.', 'print'))
story(2, 'lesson-extra-local-flow', 'Inference inside the Python process',
      step('Load the GGUF file', 'local_runtime + a downloaded model file', 'Model weights loaded through the library', 'This separate exercise uses CPU inference.', 'load'),
      step('Call the loaded model', 'Prepared instruction and source messages', 'create_chat_completion returns a dictionary.', 'No Ollama HTTP server is involved in this branch.', 'messages'),
      step('Normalize the answer', 'choices -> message -> content', 'status: completed\noutput: message with answer text', 'extract_answer can use the shared course response format.', 'convert'))
story(3, 'lesson-01-tools', 'The program executes a model request',
      step('Receive a proposed tool request', '{"type":"tool", "tool":"find_notes",\n "query":"return"}', 'command + application-selected notes_path', 'A tool name in a dictionary does not call a function.', 'command'),
      step('Check and dispatch the name', 'Allowed: find_notes\nUnknown names: reject', 'find_notes(read_notes(notes_path), query)', 'The program chooses which operations can run.', 'call'),
      step('Return matching source text', 'The search completed.', '{"matches": [\n "Returns are accepted...",\n "RETURNED money...",\n "A receipt or order number..."]}', 'run_agent receives this result before it can be sent to the model.', 'return'))
for folder in ('03-tool-agent/', ''):
    STORIES.append(dict(path='assets/' + folder + ('lesson-02-cycle' if folder else 'agent-cycle') + '.gif', kind='cycle'))
story(4, 'lesson-01-budget', 'A counter stops further requests',
      step('Compare state with limits', 'state: steps=2, tool_calls=1\nlimits: steps=4, tool_calls=2', '2 < 4 and 1 < 2 -> True', 'Both counts must be below their limits.', 'check'),
      step('Complete another tool action', 'steps=2, tool_calls=1', 'steps=3, tool_calls=2', 'The controller updates counts after the corresponding operations.', '+1'),
      step('Check before the next iteration', '3 < 4, but 2 < 2 is False', 'status: budget_limit\nNo further model request.', 'The program enforces the stop independently of model instructions.', 'False'))
story(4, 'lesson-02-context', 'Select history for the next request',
      step('Select recent events', 'events: [1, 2, 3]\nmax_events: 2', 'events[-2:] -> [2, 3]', 'Numbers stand for complete event records in this illustration.', 'slice'),
      step('Keep the original task', 'task + events [2, 3]', 'The next decide receives that task\nand only the selected events.', 'Earlier events are omitted from this request, not deleted.', 'context'),
      step('Inspect the full history', 'Original events: [1, 2, 3]', 'Original events: [1, 2, 3]', 'A slice creates a separate list.', 'no deletion'))
story(4, 'lesson-03-trace', 'Save the visible execution history',
      step('Pair a command with its result', 'command: find_notes\nresult: matching lines', '{"command": {...}, "result": {...}}', 'The abbreviated braces stand for the actual recorded fields.', 'JSON'),
      step('Write each event on its own line', 'Two events in memory', 'trace.jsonl: two JSONL records', 'save_events uses mode w and replaces the previous file.', 'write'),
      step('Investigate the saved actions', 'Commands and returned source text', 'Which command ran?\nWhich lines did it return?', 'This log does not expose internal model computations.', 'inspect'))
story(4, 'lesson-04-evaluation', 'Compare defined scenario outcomes',
      step('Run the normal-answer case', 'Expected: completed', 'Actual: completed\nCase passed.', 'Compare the specified answer as well as the status.', 'compare'),
      step('Run the repeat-until-limit case', 'Expected: budget_limit', 'Actual: budget_limit\nCase passed.', 'Stopping is success when the case expects a stop.', 'compare'),
      step('Return a summary', 'Two matching case outcomes', 'passed: 2\ntotal: 2', 'This evaluates the specified cases, not overall model quality.', 'return'))
story(5, 'lesson-01-paths', 'Validate the file path before use',
      step('Resolve a permitted relative path', 'root: workspace\nrelative: prices.py', 'workspace/prices.py\nInside root, with suffix .py.', 'Return a checked Path for later file operations.', 'resolve'),
      step('Try a different path deliberately', 'relative: ../outside.py', 'Outside the root -> ValueError', 'This second example tests rejection.', 'reject'),
      step('Identify the limit of the check', 'A permitted Python file path', 'Executing its code still creates\nan ordinary operating-system process.', 'Path validation does not create a sandbox.', 'boundary'))
story(5, 'lesson-02-diff', 'Preview the change before writing',
      step('Compare old and proposed code', 'Old: return price + quantity\nNew: return price * quantity', '- return price + quantity\n+ return price * quantity', 'Minus removes a line; plus adds a line.', 'diff'),
      step('Prepare the proposal record', 'Old bytes and proposed text', 'path, before_hash, new_text, diff', 'The old hash identifies the reviewed version.', 'proposal'),
      step('Inspect the actual file', 'return price + quantity', 'return price + quantity', 'Previewing has not written the proposed text.', 'no write'))
story(5, 'lesson-03-apply', 'Write only an approved proposal',
      step('Check permission first', 'approved = False', 'Return False; leave the file unchanged.', 'Declining ends this call before a write.', 'decline'),
      step('A separate run with approval', 'approved = True\nCompare current hash with before_hash.', 'Matching hash: continue.\nDifferent hash: reject without writing.', 'Check that the file still matches the reviewed version.', 'compare'),
      step('Write the proposed text', 'new_text: return price * quantity', 'File: return price * quantity\nReturn True.', 'Tests are still needed after a successful write.', 'write'))
story(5, 'lesson-04-verify', 'A written file still needs checks',
      step('Test the original addition bug', 'price=100, quantity=3\nActual 103; expected 300.', 'Nonzero exit code\npassed: False', 'The test detects a calculation error.', 'unittest'),
      step('Retest after the correct change', '100 * 3 -> 300\nExpected 300.', 'Exit code 0\npassed: True', 'check_project runs tests; it does not apply the fix.', 'unittest'),
      step('Return the process report', 'returncode, stdout, stderr', 'passed, returncode, output', 'Keep the diagnostic output as well as the success flag.', 'return'))
story(6, 'messages-flow', 'Task and history become messages',
      step('Build explicit request data', 'task: Find the return clauses in the policy\nevents: []', '{"task": "Find the return clauses\n  in the policy",\n "events": []}', 'Later requests can include recorded tool results.', 'task + events'),
      step('Serialize the data', 'A task-and-events dictionary', 'A JSON string for message content', 'Serialization changes the representation, not the task.', 'json.dumps'),
      step('Add the separate rules', 'Rules + serialized task data', 'developer: rules\nuser: task and history JSON', 'Return messages without making a network call.', 'return'))
story(6, 'command-flow', 'JSON text becomes a command dictionary',
      step('Parse model text', '\'{"type":"tool", "tool":"find_notes",\n "query":"return"}\'', '{"type":"tool", "tool":"find_notes",\n "query":"return"}', 'The input is str; the parsed object is dict.', 'json.loads'),
      step('Check the parsed object type', 'isinstance(command, dict)', 'True: return the dictionary.\nA JSON array would be rejected.', 'Valid JSON alone is not enough for this command protocol.', 'dict?'),
      step('Give the dictionary to its caller', 'tool: find_notes\nquery: return', 'dispatch_tool checks and executes\na permitted request later.', 'Parsing does not authorize or execute the tool.', 'return'))
story(6, 'request-flow', 'Follow the HTTP request bytes',
      step('Encode the request dictionary', 'payload: model and messages', 'JSON string -> UTF-8 bytes', 'The body contains bytes rather than a Python dictionary object.', 'encode'),
      step('Send and receive', 'Request: URL, POST, headers and body', 'urlopen sends the request\nand receives response bytes.', 'This illustrates a successful exchange.', 'HTTP'),
      step('Decode and parse the response', 'Response bytes -> UTF-8 text', 'json.loads -> provider response dictionary', 'Extracting answer text is a later operation.', 'parse'))
story(6, 'decision-flow', 'One decide_live call through its values',
      step('Build model messages', 'task and events', 'developer: rules\nuser: task and history JSON', 'The saved connection will receive these messages.', 'messages'),
      step('Call send_live', 'A message list', 'A normalized response dictionary', 'The sending function does not execute a search tool.', 'response'),
      step('Extract and parse the decision', 'extract_answer -> JSON string', 'parse_decision -> command dictionary', 'Return the dictionary to the controller for its next checks.', 'str -> dict'))
