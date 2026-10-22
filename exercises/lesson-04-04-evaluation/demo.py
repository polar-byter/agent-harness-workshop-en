from pathlib import Path
from agent import dispatch_tool
from control import check_budget, run_controlled, save_events, evaluate_cases
from decisions import decide_live

ROOT = Path(__file__).resolve().parent


def main():
    cases = [
        {'name': 'return', 'task': 'Find the return clauses in the policy. If they are found, reply with found only.',
         'expected_status': 'completed', 'expected_answer': 'found'},
        {'name': 'missing', 'task': 'Find policy clauses matching zzz_not_in_notes. If nothing matches, reply with missing only.',
         'expected_status': 'completed', 'expected_answer': 'missing'},
    ]
    def run(task):
        return run_controlled(task, ROOT / 'data' / 'notes.txt', decide_live, {'steps': 4, 'tool_calls': 3})
    print(evaluate_cases(cases, run))


if __name__ == "__main__":
    main()
