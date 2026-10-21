import json
from pathlib import Path


def build_messages(question: str, notes: list[str]) -> list[dict]:
    if not question.strip():
        raise ValueError('The question must not be empty')
    data = {'question': question, 'notes': notes}
    content = json.dumps(data, ensure_ascii=False)
    raise NotImplementedError("Complete build_messages using the lesson hints")


def extract_answer(response: dict) -> str:
    raise NotImplementedError("Complete extract_answer using the lesson hints")


def answer_question(question: str, notes: list[str], send) -> str:
    raise NotImplementedError("Complete answer_question using the lesson hints")
