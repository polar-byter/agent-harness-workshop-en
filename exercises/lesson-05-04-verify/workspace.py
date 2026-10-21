import difflib
import hashlib
import subprocess
import sys
from pathlib import Path


def workspace_path(root: Path, relative: str) -> Path:
    root = root.resolve()
    candidate = (root / relative).resolve()
    if Path(relative).is_absolute() or not candidate.is_relative_to(root):
        raise ValueError('The path must stay inside the exercise folder')
    if candidate.suffix != '.py':
        raise ValueError('This exercise only handles Python files')
    return candidate


def preview_change(root: Path, relative: str, new_text: str) -> dict:
    path = workspace_path(root, relative)
    old_text = path.read_text(encoding='utf-8')
    lines = difflib.unified_diff(old_text.splitlines(keepends=True),
        new_text.splitlines(keepends=True), fromfile='before/' + relative, tofile='after/' + relative)
    return {'path': relative, 'before_hash': hashlib.sha256(path.read_bytes()).hexdigest(),
            'new_text': new_text, 'diff': ''.join(lines)}


def apply_change(root: Path, proposal: dict, approved: bool) -> bool:
    if not approved:
        return False
    path = workspace_path(root, proposal['path'])
    current = hashlib.sha256(path.read_bytes()).hexdigest()
    if current != proposal['before_hash']:
        raise ValueError('The file changed after the proposal was prepared')
    path.write_text(proposal['new_text'], encoding='utf-8')
    return True


def check_project(root: Path) -> dict:
    command = [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests']
    raise NotImplementedError("Complete check_project using the lesson hints")


def prepare_coding_task(task: str, root: Path, propose) -> dict:
    path = workspace_path(root, 'prices.py')
    new_text = propose(task, path.read_text(encoding='utf-8'))
    if not isinstance(new_text, str):
        raise ValueError('The proposal must contain Python file text')
    return preview_change(root, 'prices.py', new_text)
