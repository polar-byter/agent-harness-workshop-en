"""Check the English edition for untranslated text and parse its Python sources."""
import ast
import json
from pathlib import Path
import re
import struct
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SUFFIXES = {'.md', '.py', '.json', '.yml', '.yaml', '.txt', '.js', '.html', '.csv'}


def check_text(name, data):
    text = data.decode('utf-8')
    assert not re.search('[\u0400-\u04ff]', text), ('Untranslated Cyrillic', name)
    if Path(name).suffix == '.py':
        ast.parse(text, filename=name)


def main():
    count = 0
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(part in ('.git', '.checks', '__pycache__', '.venv') for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix in SUFFIXES:
            check_text(str(path.relative_to(ROOT)), path.read_bytes())
            count += 1
        elif path.suffix == '.zip':
            with ZipFile(path) as archive:
                assert archive.testzip() is None, path
                for name in archive.namelist():
                    if Path(name).suffix in SUFFIXES:
                        check_text(str(path.relative_to(ROOT)) + ':' + name, archive.read(name))
        elif path.suffix in ('.gif', '.png'):
            data = path.read_bytes()
            width = struct.unpack('<H', data[6:8])[0] if path.suffix == '.gif' else struct.unpack('>I', data[16:20])[0]
            assert width <= 600, (path, width)
    config = json.loads((ROOT / 'tools/course-map.json').read_text(encoding='utf-8'))
    assert len(config['lessons']) == 24
    assert len(list((ROOT / 'assets').rglob('*.gif'))) == 29
    for gif in (ROOT / 'assets').rglob('*.gif'):
        assert gif.with_suffix('.png').is_file(), gif
    print(f'English text and Python syntax checked in {count} files and all starter archives.')


if __name__ == '__main__':
    main()
