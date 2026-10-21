from pathlib import Path


def find_notes(notes: list[str], query: str) -> list[str]:
    query = query.strip().casefold()
    if not query:
        raise ValueError('Enter a nonempty query')
    selected = []
    raise NotImplementedError("Complete find_notes using the lesson hints")


def find_notes_alt(notes: list[str], query: str) -> list[str]:
    query = query.strip().casefold()
    if not query:
        raise ValueError('Enter a nonempty query')
    raise NotImplementedError("Complete find_notes_alt using the lesson hints")


def read_notes(path: Path) -> list[str]:
    raise NotImplementedError("Complete read_notes using the lesson hints")
