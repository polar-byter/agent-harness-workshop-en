from notes import find_notes, find_notes_alt


def main() -> None:
    notes = ['Returns are accepted within 14 days.', 'Delivery within the city takes 1 day.', 'RETURNED money goes back to the original card.']
    query = ' Return '
    for search in (find_notes, find_notes_alt):
        print(search.__name__)
        try:
            matches = search(notes, query)
        except NotImplementedError as error:
            print(error)
        else:
            print(matches)


if __name__ == '__main__':
    main()
