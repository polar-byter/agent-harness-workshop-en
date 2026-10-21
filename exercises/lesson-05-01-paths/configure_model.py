"""Save one model connection for all course folders on this computer."""
import json
import tkinter as tk
from tkinter import messagebox, ttk
from transport import connection_path


def main():
    window = tk.Tk()
    window.title('Course model connection')
    window.resizable(False, False)
    frame = ttk.Frame(window, padding=18)
    frame.grid()
    ttk.Label(frame, text='Provider').grid(row=0, column=0, sticky='w', pady=5)
    provider = ttk.Combobox(frame, values=('openrouter', 'vsegpt', 'ollama'), state='readonly', width=42)
    provider.grid(row=0, column=1, pady=5)
    provider.set('openrouter')
    ttk.Label(frame, text='Model name').grid(row=1, column=0, sticky='w', pady=5)
    model = ttk.Entry(frame, width=45)
    model.grid(row=1, column=1, pady=5)
    model.insert(0, 'openrouter/free')
    ttk.Label(frame, text='API key').grid(row=2, column=0, sticky='w', pady=5)
    api_key = ttk.Entry(frame, width=45, show='*')
    api_key.grid(row=2, column=1, pady=5)
    ttk.Label(frame, text='Ollama needs no key. Settings are shared by all lessons.').grid(row=3, columnspan=2, pady=8)

    def change_provider(event=None):
        model.delete(0, tk.END)
        model.insert(0, {'openrouter': 'openrouter/free', 'ollama': 'qwen3:0.6b', 'vsegpt': ''}[provider.get()])
        api_key.delete(0, tk.END)

    provider.bind('<<ComboboxSelected>>', change_provider)
    path = connection_path()
    if path.is_file():
        try:
            previous = json.loads(path.read_text(encoding='utf-8'))
            if previous.get('provider') in provider['values']:
                provider.set(previous['provider'])
                model.delete(0, tk.END)
                model.insert(0, previous.get('model', ''))
                api_key.insert(0, previous.get('api_key', ''))
        except (OSError, ValueError):
            messagebox.showwarning('Settings', 'Saved settings could not be read. Enter them again.')

    def save():
        if not model.get().strip() or (provider.get() != 'ollama' and not api_key.get().strip()):
            messagebox.showerror('Missing information', 'Enter the model name and API key; Ollama only needs a model name.')
            return
        settings = {'provider': provider.get(), 'model': model.get().strip(),
                    'api_key': '' if provider.get() == 'ollama' else api_key.get().strip()}
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(settings, ensure_ascii=False, indent=2), encoding='utf-8')
            path.chmod(0o600)
        except OSError:
            messagebox.showerror('Could not save', 'Check access to the user settings folder.')
            return
        messagebox.showinfo('Saved', 'Open demo.py and run it using Run.')
        window.destroy()

    ttk.Button(frame, text='Save', command=save).grid(row=4, columnspan=2, pady=8)
    window.mainloop()


if __name__ == '__main__':
    main()
