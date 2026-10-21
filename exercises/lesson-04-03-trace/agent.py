import json
from pathlib import Path
from notes import find_notes, read_notes


def dispatch_tool(command: dict, notes_path: Path) -> dict:
    name = command.get('tool')
    if name == 'read_notes':
        return {'notes': read_notes(notes_path)}
    if name == 'find_notes':
        query = command.get('query')
        if not isinstance(query, str):
            raise ValueError('Search requires a string query')
        return {'matches': find_notes(read_notes(notes_path), query)}
    raise ValueError('Unknown tool: ' + str(name))


def run_agent(task: str, notes_path: Path, decide, max_steps: int = 4) -> dict:
    if max_steps < 1:
        raise ValueError('At least one step is required')
    events = []
    for step in range(max_steps):
        command = decide(task, events)
        if command.get('type') == 'answer':
            text = command.get('text')
            if not isinstance(text, str) or not text.strip():
                raise ValueError('Empty answer')
            return {'status': 'completed', 'answer': text, 'events': events}
        if command.get('type') != 'tool':
            raise ValueError('Expected an answer or a tool request')
        result = dispatch_tool(command, notes_path)
        events.append({'command': command, 'result': result})
    return {'status': 'step_limit', 'answer': '', 'events': events}


def decide_fixture(task: str, events: list[dict]) -> dict:
    if not events:
        return {'type': 'tool', 'tool': 'find_notes', 'query': 'python'}
    return {'type': 'answer', 'text': 'Found two notes about Python.'}
