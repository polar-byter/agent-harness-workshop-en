from pathlib import Path
from workspace import workspace_path, prepare_coding_task, apply_change, check_project
from coding_model import propose_live

ROOT = Path(__file__).resolve().parent


def main():
    proposal = prepare_coding_task('Fix the total price calculation', ROOT / 'workspace', propose_live)
    print(proposal['diff'] or 'The model proposed no changes')


if __name__ == "__main__":
    main()
