# Write a search function

> **Where we are.** We are building an assistant that answers from a set of notes. The first step is for the program to find the right notes itself, with no model yet.
> `notes -> [search] -> model -> answer`

Recall the MTS case from the introduction: the assistant gave wrong advice because the right paragraph never reached the model. The first thing to check in such an investigation is whether the program found that paragraph at all. So we start by writing the function that finds notes by keyword and watching exactly which lines it picks.

## The task

We have three notes:

```text
Python lists
Agent tools
python functions
```

We want the notes that mention "python", whether it is written in capitals or not.

**Guess before running:** how many notes should the function return, and which ones? Keep your answer in mind; we will check it at the end.

## Open the starter

Download [this lesson's starter](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/downloads/lesson-01-01-search.zip), extract it with **Extract All** and open the `lesson-01-01-search` folder in PyCharm with **File -> Open**. In the Project panel open `notes.py`. The functions `find_notes` and `find_notes_alt` are already started there; we will complete them.

## Step 1. Normalize the query

A person may type the query with extra spaces or in capitals: `' PYTHON '`. To compare reliably, strip the spaces and lower the case:

```python
query = ' PYTHON '
query = query.strip().casefold()
print(query)   # python
```

`strip()` removes spaces at both ends, and `casefold()` turns letters into lower case for comparison. Both return a new string, so we store the result back in `query`. This line is already at the start of `find_notes`.

## Step 2. Check one note

Take the first note and ask Python whether it contains the query:

```python
note = 'Python lists'
'python' in note.casefold()   # True
```

The `in` operator answers whether the string on the left occurs inside the string on the right. The note itself stays unchanged: `casefold()` makes a lowered copy only for the comparison, and the original note goes into the result.

## Step 3. Go through all notes

Now check each note in turn and collect the matching ones in a new list, `selected`. A `for` loop takes the notes one by one and runs the indented code under it for each:

```python
selected = []
for note in notes:
    if query in note.casefold():
        selected.append(note)
```

The spaces at the start of the lines matter. They tell Python that the `if` runs inside the loop and that `append` runs only when the condition is true. Use four spaces per level and keep the indentation as shown. `append` adds a note to the end of `selected`.

The animation shows `selected` growing as the loop goes:

## Your turn

In `notes.py`, `find_notes` already prepares the query and creates the empty list `selected`. Replace the line `raise NotImplementedError(...)` with the loop and fill in the two gaps:

```python
def find_notes(notes: list[str], query: str) -> list[str]:
    query = query.strip().casefold()
    if not query:
        raise ValueError('Enter a nonempty query')
    selected = []
    for note in notes:
        if ...:
            selected.append(...)
    return selected
```

1. In the condition, use the check from step 2 with the variable `query` instead of `'python'`.
2. In `append`, pass the original `note`, so the result keeps the note exactly as written.

`return selected` sits after the loop, at the same level as `for`, and hands the collected list back to whoever called the function. If you indent it into the loop, the function will stop after the first note.

Then open `find_notes_alt` in the same file. It does the same selection in one line using a list comprehension. After the prepared query lines, replace its `raise NotImplementedError(...)` with:

```python
    return [note for note in notes if query in note.casefold()]
```

Read it as "a list of each `note` from `notes` for which the query is in the lowered note". It is the same loop and condition as above, written as one expression.

## Run it

Open `demo_search.py`, right-click in the editor and choose **Run 'demo_search'**. In the Run window both functions should print:

```text
['Python lists', 'python functions']
```

Did that match your guess? "Agent tools" was skipped, and "Python lists" with a capital letter was found thanks to `casefold()`. If you see `Complete ...` instead, the file is not saved or the `raise NotImplementedError(...)` line is still in place.

## Try to break it

1. Remove `.casefold()` from the condition and run again. Which note disappears, and why?
2. In `demo_search.py`, change the query to three spaces `'   '`. The function stops with "Enter a nonempty query". That check is there on purpose: an empty string is contained in every string, so without it the search would return everything. While a person types the query, that seems unlikely; once a model or another part of the program calls the search, an empty value can arrive by mistake, and it is better to see it at once.

Put the code back the way it was before moving on.

## What we have now

We can check the first link in the MTS chain: did the program find the right note? If a note is in the source but not in this list, the problem is in the search, not in the model. In section 3 the model will ask for this same search, and your function will choose the lines.

This kind of selection is called **retrieval** in articles about AI. Ours is the simplest form: substring search. How retrieval relates to RAG is in the [list of terms](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/terms.md).

To check the search on more cases (duplicates, no matches, unusual letters), see [let tests repeat the checks](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/01-note-search/extra-tests.md). Next: [read notes from a file](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/01-note-search/02-read.md). Back to [all lessons](https://github.com/polar-byter/agent-harness-workshop-en/blob/main/course/README.md).
