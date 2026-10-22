import json
import hashlib
from pathlib import Path
from notes import find_notes, find_notes_alt, read_notes
from journal import write_result
from app import run_search

ROOT = Path(__file__).resolve().parent


def main():
    print('Exercise run without a network model call.')
    try:
        result = [find_notes(['Returns are accepted within 14 days.', 'Delivery within the city takes 1 day.', 'RETURNED money goes back to the original card.'], ' Return '), find_notes_alt(['Returns are accepted within 14 days.', 'Delivery within the city takes 1 day.', 'RETURNED money goes back to the original card.'], ' Return ')]
    except NotImplementedError as error:
        print(error)
    else:
        print(result)


if __name__ == '__main__':
    main()
