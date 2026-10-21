# Find a file and run the right example in PyCharm

A lesson archive contains a project folder, not a single script. Extract it first with **Extract All** in File Explorer. In PyCharm choose **File -> Open** and select the extracted folder named in the lesson, such as `lesson-01-01-search`, not the ZIP file and not a parent folder that holds several projects.

## Find the exercise

Open **View -> Tool Windows -> Project** and expand the project root with its small arrow. Python modules such as `notes.py` sit directly under the root; `data` holds source files and `tests` holds the optional checks. Double-click the module named in the lesson and find the target function. Functions from earlier lessons are already complete; the current one ends with `raise NotImplementedError(...)`, which you remove once your code is in place.

Write the function body using the lesson hints. The function header is already there, so you do not need a second copy of it. Use four spaces per indentation level.

## Run a particular file

Open the demonstration file named in the lesson, right-click inside the editor and choose **Run 'demo'** (or the matching file name). The green Run button at the top repeats the last configuration and may start a different file, so the right-click menu is the safer choice.

The output appears in **View -> Tool Windows -> Run**. A message beginning `Complete ...` means the current function is still unfinished. A traceback shows the chain of calls that led to an error; read its last lines first.

If no interpreter is selected, open the project's Python interpreter setting and choose your installed Python, or create a virtual environment for the project. The main lessons use only the standard library.

<img src="../assets/pycharm-run.png" width="480" alt="Find the example in Project and read its output in Run">

## Which demonstration to run

Early lessons run entirely offline. After the required connection lesson, the main `demo.py` uses your saved model connection, while `demo_check.py` checks your code on known inputs without a model. Use both: the first shows how the model behaves, the second whether your function is correct.
