import json
from pathlib import Path


def write_result(path: Path, result: dict) -> None:
    text = json.dumps(result, ensure_ascii=False)
    raise NotImplementedError("Complete write_result using the lesson hints")
