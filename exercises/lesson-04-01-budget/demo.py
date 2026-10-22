from pathlib import Path
from agent import dispatch_tool
from control import check_budget, run_controlled, save_events, evaluate_cases
from decisions import decide_live

ROOT = Path(__file__).resolve().parent


def main():
    state = {'steps': 0, 'tool_calls': 0}
    limits = {'steps': 4, 'tool_calls': 3}
    events = []
    while check_budget(state, limits):
        command = decide_live('Find the return clauses in the policy', events)
        state['steps'] += 1
        print('Command:', command)
        if command.get('type') == 'answer':
            if not isinstance(command.get('text'), str) or not command['text'].strip():
                raise ValueError('The model returned an empty answer')
            print(command['text'])
            return
        if command.get('type') != 'tool':
            raise ValueError('Unknown command type')
        result = dispatch_tool(command, ROOT / 'data' / 'notes.txt')
        state['tool_calls'] += 1
        events.append({'command': command, 'result': result})
        print('Result:', result)
    print('Limit reached:', state)


if __name__ == "__main__":
    main()
