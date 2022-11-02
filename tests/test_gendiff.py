from pathlib import Path
from gendiff import generate_diff, zero_check

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

# проверка yml модуля


def test_value_gendiff_yml():  # получение положительного результата
    result = generate_diff(
        current_dir / 'fixtures' / 'filepath1.yml',
        current_dir / 'fixtures' / 'filepath2.yaml'
        )
    file = current_dir / 'fixtures' / 'result_test_gendiff.txt'
    with file.open() as f:
        expected_result = f.read()
    assert result == expected_result


def test_empty_gendiff_yml():  # тест на возврат в случае пустых файлов
    result = generate_diff(
        current_dir / 'fixtures' / 'empty_file.yml',
        current_dir / 'fixtures' / 'filepath2.yaml'
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


def test_gendiff_nest():
    result = generate_diff(
        current_dir / 'fixtures' / 'file1_1.json',
        current_dir / 'fixtures' / 'file2_2.json'
        )
    file = current_dir / 'fixtures' / 'expected_result_dict_2.txt'
    with file.open() as f:
        expected_result = f.read()
    assert result == expected_result
