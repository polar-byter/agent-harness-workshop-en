# Who this course is for

The course is for analysts, process owners and managers, system administrators, support and QA specialists - anyone who introduces AI assistants, accepts their work or is responsible for an area where they appear. Why understanding an agent's internals matters for each of these roles is covered in the [introduction](00-introduction.md).

You do not need to be a programmer. It is enough to be comfortable with a computer and willing to read short pieces of code. We learn Python along the way, only as much as each step needs: strings, lists, dictionaries, loops, functions and reading files. The same skills come in handy outside the course, when you need to compare two exports or assemble a report from several files.

## What you need

- A Windows computer. The lessons show the route for Windows and PyCharm.
- PyCharm and Python 3.12 or newer. Installing them and opening the first project is covered in the [setup lesson](01-note-search/00-setup.md).
- From lesson 2.4 on, a connection to a model: a cloud service through its API or a small Qwen model running on your laptop through Ollama, with no registration or payment.

## How each lesson works

Every lesson has its own archive with a ready project. Everything written in earlier lessons already works, and the current function is started and stopped at the line `raise NotImplementedError(...)`. The lesson shows the data the function works with and a template with `...` gaps, with a hint for each gap. You complete the function, run the example and compare the result with what you expected. Prepared tests in the `tests` folder let you check your solution further.

The archives are independent: if one lesson does not work out, you can open the next archive and carry on from there.

Start with the [introduction](00-introduction.md) or go straight to [opening the first project](01-note-search/00-setup.md). The whole route is in the [lesson index](README.md).
