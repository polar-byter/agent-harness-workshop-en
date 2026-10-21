import difflib
import hashlib
import subprocess
import sys
from pathlib import Path


def workspace_path(root: Path, relative: str) -> Path:
    root = root.resolve()
    candidate = (root / relative).resolve()
    raise NotImplementedError("Complete workspace_path using the lesson hints")


def preview_change(root: Path, relative: str, new_text: str) -> dict:
    raise NotImplementedError("Complete preview_change using the lesson hints")


def apply_change(root: Path, proposal: dict, approved: bool) -> bool:
    raise NotImplementedError("Complete apply_change using the lesson hints")


def check_project(root: Path) -> dict:
    raise NotImplementedError("Complete check_project using the lesson hints")


def prepare_coding_task(task: str, root: Path, propose) -> dict:
    path = workspace_path(root, 'prices.py')
    new_text = propose(task, path.read_text(encoding='utf-8'))
    if not isinstance(new_text, str):
        raise ValueError('The proposal must contain Python file text')
    return preview_change(root, 'prices.py', new_text)
