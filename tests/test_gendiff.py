from pathlib import Path
from gendiff import generate_diff

current_dir = Path(__file__).parent

def test_valid_gendiff():
    result = generate_diff(current_dir / 'fixtures' / 'file1.json', current_dir / 'fixtures' / 'file2.json')
    file = current_dir / 'fixtures' / 'result_test_gendiff.txt'
    with file.open() as f:
        expected_result = f.read()
    assert result == expected_result

