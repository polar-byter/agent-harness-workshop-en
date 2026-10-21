# Optional: let tests repeat the checks

After your search demonstration works, it is worth borrowing a practice from programmers: write down the expected behavior so it can be checked again after an edit. A unit test calls a small part of the program with known inputs and compares the actual result with an expected one.

For example, searching `['Python lists', 'Agent tools']` for `'python'` should return `['Python lists']`. A second case can check a word with no match, and a third can check that a whitespace-only request is rejected. These cases help preserve the function's contract while you try another implementation.

In the extracted project, expand **tests**, open the lesson test file and find the test class. Right-click its name and choose **Run**. PyCharm shows each result in its test panel; read a failed assertion as a comparison of expected and actual values. Running the correct test matters: a test for an unfinished future function may fail for the expected reason.

Tests do not prove that every possible input is handled or that a generated answer is true. They make a chosen set of expectations repeatable. In the model lessons we keep deterministic code checks separate from live generation so an unstable service or differently worded answer does not obscure a Python error.

Return to [the search lessons](../README.md#searching-notes) whenever you want to repeat those checks.
