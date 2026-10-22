"""Rebuild each starter's TASK.md and README.md from its lesson page, then repack the download archives.

TASK.md is the lesson page without the animations, with links made absolute so they work from a
local copy of the starter. Archives are written with a fixed date, so they change only with content.
"""
import json
import re
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
BLOB = 'https://github.com/polar-byter/agent-harness-workshop-en/blob/main/'
SKIP = {'__pycache__', '.pytest_cache', 'scratch'}
GENERATED = {'runs.jsonl', 'trace.jsonl'}


def absolute(link: str, page: PurePosixPath) -> str:
    if re.match(r'[a-z]+://|#', link):
        return link
    path, _, anchor = link.partition('#')
    parts = []
    for part in (page.parent / path).parts:
        if part == '..':
            parts.pop()
        elif part != '.':
            parts.append(part)
    return BLOB + '/'.join(parts) + ('#' + anchor if anchor else '')


def task_text(page: str, path: PurePosixPath) -> str:
    lines = []
    for line in page.splitlines():
        if line.startswith('<img ') or line.startswith('[Static version]'):
            continue
        lines.append(re.sub(r'\]\(([^)]+)\)', lambda m: '](' + absolute(m.group(1), path) + ')', line))
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip() + '\n'


def main():
    config = json.loads((ROOT / 'tools' / 'course-map.json').read_text(encoding='utf-8'))
    for lesson in config['lessons']:
        page_path = PurePosixPath(lesson['path'])
        page = (ROOT / page_path).read_text(encoding='utf-8')
        title = page.splitlines()[0].lstrip('# ').strip()
        lesson['title'] = title
        folder = ROOT / 'exercises' / lesson['root']
        (folder / 'TASK.md').write_text(task_text(page, page_path), encoding='utf-8', newline='\n')
        readme = (f'# {title}\n\nOpen this folder as a PyCharm project and read [TASK.md](TASK.md).\n\n'
                  f'[Full lesson]({BLOB}{page_path}) / [Course index]({BLOB}course/README.md).\n\n'
                  'The current function is unfinished on purpose. Keep model credentials outside the project.\n')
        (folder / 'README.md').write_text(readme, encoding='utf-8', newline='\n')
        archive = ROOT / 'downloads' / (lesson['root'] + '.zip')
        with ZipFile(archive, 'w', ZIP_DEFLATED) as package:
            for path in sorted(folder.rglob('*')):
                relative = path.relative_to(folder)
                if not path.is_file() or SKIP & set(relative.parts) or path.name in GENERATED:
                    continue
                info = ZipInfo(lesson['root'] + '/' + relative.as_posix(), date_time=(2026, 10, 22, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                package.writestr(info, path.read_bytes())
    (ROOT / 'tools' / 'course-map.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n',
                                                     encoding='utf-8', newline='\n')
    print('Rebuilt', len(config['lessons']), 'TASK.md files, READMEs and starter archives.')


if __name__ == '__main__':
    main()
