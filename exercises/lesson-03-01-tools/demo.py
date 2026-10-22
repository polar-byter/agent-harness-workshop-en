from pathlib import Path
from agent import dispatch_tool
from decisions import decide_live

ROOT = Path(__file__).resolve().parent


def main():
    task = 'Find the return clauses in the policy. First request the find_notes tool with query return.'
    command = decide_live(task, [])
    print('Model command:', command)
    if command.get('type') != 'tool':
        raise ValueError('The model requested no tool. Compare its command with the task; do not silently substitute one.')
    result = dispatch_tool(command, ROOT / 'data' / 'notes.txt')
    print('Tool result:', result)


if __name__ == "__main__":
    main()
