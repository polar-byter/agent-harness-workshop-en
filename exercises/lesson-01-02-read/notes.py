from pathlib import Path


def find_notes(notes: list[str], query: str) -> list[str]:
    query = query.strip().casefold()
    if not query:
        raise ValueError('Enter a nonempty query')
    matches = []
    for note in notes:
        if query in note.casefold():
            matches.append(note)
    return matches


def find_notes_alt(notes: list[str], query: str) -> list[str]:
    query = query.strip().casefold()
    if not query:
        raise ValueError('Enter a nonempty query')
    return [note for note in notes if query in note.casefold()]


def read_notes(path: Path) -> list[str]:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    cleaned_notes = []
    raise NotImplementedError("Complete read_notes using the lesson hints")
