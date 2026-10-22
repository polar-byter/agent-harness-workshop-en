# Optional local-library setup

This page sets up the [run a model inside Python](extra-local.md) exercise. It loads a small model into the Python process with llama-cpp-python and does not replace the Ollama or API connection used by the main lessons. Finish `send_local` and run its offline check before installing anything.

The prepared exercise targets **Windows x64 and Python 3.14**. Open the starter as its own project and create a virtual environment for it, so the libraries stay inside this project. In PyCharm's Terminal run:

```powershell
python -m pip install -r requirements.txt
```

The requirements file points to a prebuilt llama-cpp-python 0.3.36 package, so nothing has to be compiled. Look at the file before installing. Other operating systems or Python versions need a different build, which this exercise does not cover.

Run `check_install.py` from the Project panel. It prints the interpreter path and the version of the loaded library; this checks the installation without loading the model.

Download the official [Qwen3-0.6B GGUF](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF) file named `Qwen3-0.6B-Q8_0.gguf`. In the Project panel expand `models` and put the file there, next to its README. Model files are not included in the repository or the lesson archives.

Now run `demo.py`. `local_runtime.load_model` opens exactly that file, the demonstration builds the messages and your `send_local` calls the library; the model is closed when the block ends. Compare the answer with the clause: a working model can still answer wrongly or ignore the instruction.

If the file is missing, the error shows the path where the program expected it. If the library will not load, check the selected interpreter and its architecture before touching the exercise code. Installing packages into a different system Python just because its command happens to work will not help this project.
