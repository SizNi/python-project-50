from pathlib import Path
from gendiff import generate_diff, zero_check, dict_transform, sort_key

current_dir = Path(__file__).parent


def test_valid_gendiff():  # тест на правильный результат
    result = generate_diff(
        current_dir / 'fixtures' / 'file1.json',
        current_dir / 'fixtures' / 'file2.json'
        )
    file = current_dir / 'fixtures' / 'result_test_gendiff.txt'
    with file.open() as f:
        expected_result = f.read()
    assert result == expected_result


def test_empty_gendiff():  # тест на возврат в случае пустых файлов
    result = generate_diff(
        current_dir / 'fixtures' / 'empty_file.json',
        current_dir / 'fixtures' / 'file2.json'
        )
    assert result == 'nothing to diff'


def test_one_file_zero():
    result = generate_diff(
        current_dir / 'fixtures' / 'file1.json',
        current_dir / 'fixtures' / 'empty_file.json'
        )
    assert result == 'nothing to diff'


def test_zero_check():
    result = zero_check(current_dir / 'fixtures' / 'file1.json')
    assert result != 0


def test_dict_transform():
    result = dict_transform(
        {'numbers': '12345',
         'True': 'False', 'hello': 'o'}
        )
    file = current_dir / 'fixtures' / 'expected_result_dict.txt'
    with file.open() as f:
        expected_result = f.read()
    assert result == expected_result


def test_sort_key():
    e = ['true', '1234']
    result = sort_key(e)
    assert result == 'r'
