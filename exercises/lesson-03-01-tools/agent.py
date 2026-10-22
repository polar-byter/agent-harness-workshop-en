import json
from pathlib import Path
from notes import find_notes, read_notes


def dispatch_tool(command: dict, notes_path: Path) -> dict:
    name = command.get('tool')
    raise NotImplementedError("Complete dispatch_tool using the lesson hints")


def run_agent(task: str, notes_path: Path, decide, max_steps: int = 4) -> dict:
    raise NotImplementedError("Complete run_agent using the lesson hints")


def decide_fixture(task: str, events: list[dict]) -> dict:
    if not events:
        return {'type': 'tool', 'tool': 'find_notes', 'query': 'return'}
    return {'type': 'answer', 'text': 'Found three clauses about returns.'}
