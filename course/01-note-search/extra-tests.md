# Optional: let tests repeat the checks

In the [search lesson](01-search.md) the function found two notes out of three, as expected. But what happens with an empty query? With a duplicate note? With a word that is nowhere in the notes? Checking all that by hand after every edit gets tedious, and sooner or later a case gets forgotten.

Programmers solve this with unit tests: small checks that call a function with chosen inputs and compare the result with the expected one. You write the condition once and rerun it whenever you like.

For example, a test gives the function `['Python lists', 'Agent tools']` and the query `'python'` and expects `['Python lists']`. If the function returns anything else, the test shows what was expected and what came back.

<img src="../../assets/01-note-search/test-result.gif" width="480" alt="A test compares the expected list with the actual one">

[Static version](../../assets/01-note-search/test-result.png).

## Run the prepared tests

In the `lesson-01-01-search` project, open `tests/test_lesson.py`. Right-click the line `class LessonTests` and choose **Run**. PyCharm [can run a single test class](https://www.jetbrains.com/help/pycharm/performing-tests.html), so there is no need to run the whole `tests` folder.

The result appears at the bottom. The tests check both `find_notes` and `find_notes_alt`: letter case, spaces in the query, a duplicate note, no matches and an empty query. If a test fails, open its result: it shows the expected value and what the function returned, or the error that occurred. Find the cause in the function and run the tests again. Changing the expected value just to make a test pass would leave the test checking nothing.

## What tests can and cannot tell you

Tests check exactly the cases written into them. A passing run means the search works on those cases. If tomorrow a note contains "Pyhton" with a typo, the test will not notice; that case has to be added to it.

In later lessons, `tests/test_lesson.py` checks that lesson's own function: reading the file, writing the journal or the combined run. Check which project is open in the Project panel before running.

Back to [the search lesson](01-search.md) or on to [reading notes from a file](02-read.md).
