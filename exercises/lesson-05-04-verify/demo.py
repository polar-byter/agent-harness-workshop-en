from pathlib import Path
from workspace import workspace_path, prepare_coding_task, apply_change, check_project
from coding_model import propose_live

ROOT = Path(__file__).resolve().parent


def main():
    proposal = prepare_coding_task('Fix the total price calculation', ROOT / 'workspace', propose_live)
    print(proposal['diff'] or 'The model proposed no changes')

    approved = input('Apply this change to the exercise prices.py? Type yes: ').strip().lower() == 'yes'
    applied = apply_change(ROOT / 'workspace', proposal, approved)
    print('Change applied:', applied)

    print('Project check:', check_project(ROOT / 'workspace'))


if __name__ == "__main__":
    main()
