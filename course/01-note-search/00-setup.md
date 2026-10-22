# Open the first project

> **Where we are.** The course starts with the first question from the MTS case: did the program find the right clause of the instructions? Our first step is a search through a policy, and before writing it we get PyCharm and Python ready.

One example runs through the whole course: the returns policy of an online store. It has several clauses:

```text
Returns are accepted within 14 days.
Delivery within the city takes 1 day.
RETURNED money goes back to the original card.
```

When a customer asks about returns, the assistant should find the first and third clauses and skip the second one about delivery. We write the search in the first lesson; later the program will read the policy from a file and record what it found. Today the goal is modest: open the project and make sure Python runs.

## Install PyCharm and Python

PyCharm is an editor for writing and running Python code; the free edition is enough for this course. Download it from the [JetBrains site](https://www.jetbrains.com/pycharm/download/). You also need Python itself, version 3.12 or newer, from [python.org](https://www.python.org/downloads/windows/). In the first installer window, tick **Add python.exe to PATH**, then click **Install Now**. If Python is already installed, you can skip this.

## Open the starter

Download the [first starter](../../downloads/lesson-01-01-search.zip), right-click it in File Explorer and choose **Extract All**. In PyCharm choose **Open** on the welcome screen (or **File -> Open**) and select the extracted `lesson-01-01-search` folder.

Open **View -> Tool Windows -> Project** and expand the root folder. The project has a few files: `notes.py` will hold reading and searching, `app.py` will connect them, `journal.py` will save results, and the `tests` folder holds prepared checks. These checks call your function with chosen data and compare the answer with the expected one; programmers call them unit tests. You will not write all of the files at once; the first lesson is only about searching.

## Choose the Python interpreter

PyCharm needs to know which Python to use. Open **File -> Settings -> Python -> Interpreter** (in some versions **Project: lesson-01-01-search -> Python Interpreter**). If Python 3.12 or newer is already selected, you are done. If the field says **No interpreter**, click **Add Interpreter -> Add Local Interpreter**, choose **Virtualenv** and select your installed Python as the **Base interpreter**. A virtual environment is a separate folder for this project's libraries; we will not install anything into it yet. The [JetBrains guide](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html) shows the same steps with screenshots.

## First run

Open `start.py`, right-click inside the editor and choose **Run 'start'**. The Run window at the bottom should show:

```text
Project opened. Python is running.
```

PyCharm found Python and ran a file from the project. Now open `demo_search.py`: it calls the search functions with the three clauses above and the query `' Return '`. Run it the same way. For now it prints a message that the function is not finished yet - writing it is the first lesson.

If PyCharm says no interpreter is selected, go back to the previous section. If there is no **Run** item in the menu, check that you opened `start.py` from the extracted folder and not from inside the ZIP. A diagram of the PyCharm windows is in [find a file and run an example](../pycharm.md).

Next: [find policy clauses by keyword](01-search.md).
