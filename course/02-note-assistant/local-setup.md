# Optional local-library setup

This branch loads a small model in the Python process using llama-cpp-python. It does not replace the shared Ollama or API connection used by later main lessons. Complete [send_local](extra-local.md) and run its offline check before installing or downloading the runtime.

The supplied pinned exercise targets **Windows x64 and Python 3.14**. Open this starter as its own project and select a project virtual environment. In PyCharm's Terminal run:

```powershell
python -m pip install -r requirements.txt
```

The requirement points to a prepared llama-cpp-python 0.3.36 wheel rather than asking a beginner to set up a compiler. Read the actual requirements file before installation. Other operating systems or Python versions may need a different supported build; that adaptation is outside this particular pinned branch.

Run `check_install.py` from the Project panel. Its output should identify the interpreter and loaded library version. This checks the runtime installation without loading model weights.

Download the official [Qwen3-0.6B GGUF model](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF) file named `Qwen3-0.6B-Q8_0.gguf`. In Project expand `models` and place the downloaded file there, next to its README. Do not rename another file format to GGUF. Model weights are intentionally excluded from the repository and lesson archives.

Now run `demo.py`. `local_runtime.load_model` opens that exact file, the demonstration builds messages, and your `send_local` calls the library. Its context manager closes the loaded model afterward. A running model can still give an incorrect answer or ignore an instruction; compare the result with the source note.

If the file is absent, read the reported expected path. If the library cannot load, check the selected interpreter and architecture before changing exercise code. Avoid installing packages into a different system Python merely because its command happens to be available.
