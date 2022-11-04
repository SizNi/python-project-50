import json
import os
# from pathlib import Path
import yaml
from gendiff_stylish import stylish
from gendiff_plain import plain

# Основная функция - сравнивает если нулевые значения,
# если нет - работает с остальными функциями


def generate_diff(first_file, second_file, format='stylish'):
    first_size = zero_check(first_file)
    second_size = zero_check(second_file)
    if first_size == 0 or second_size == 0:
        return 'nothing to diff'
    else:
        f1, f2 = define_file_extension(first_file, second_file)
        lines = calculate_diff(f1, f2)
        if format.lower() == 'stylish':
            result = stylish(lines)
        elif format.lower() == 'plain':
            result = plain(lines)
        # print(result)
        return result

# сравнивает словари


def calculate_diff(f1, f2):

    def iter_(current_f1, current_f2):
        keys_list1 = set(current_f1.keys())
        keys_list2 = set(current_f2.keys())
        keys_list = keys_list1 | keys_list2
        keys_list = sorted(keys_list)
        lines = {}
        for elem in keys_list:
            # если ключ есть в обоих словарях
            if elem in keys_list1 and elem in keys_list2:
                # все словари
                if isinstance(
                    current_f1[elem], dict
                    ) and isinstance(
                        current_f2[elem], dict
                        ):
                    lines[f'  {elem}'] = iter_(
                        current_f1[elem], current_f2[elem]
                        )
                # один словарь
                elif isinstance(current_f1[elem], dict) and not isinstance(
                        current_f2[elem], dict
                        ):
                    lines[f'- {elem}'] = iter_(
                        current_f1[elem], current_f1[elem]
                        )
                    lines[f'+ {elem}'] = current_f2[elem]
                # один словарь
                elif not isinstance(
                    current_f1[elem], dict
                    ) and isinstance(
                        current_f2[elem], dict
                        ):
                    lines[f'- {elem}'] = current_f1[elem]
                    lines[f'+ {elem}'] = iter_(
                        current_f2[elem], current_f2[elem]
                        )  # первый пустой
                # все не словари
                elif not isinstance(
                    current_f1[elem], dict
                    ) and not isinstance(
                        current_f2[elem], dict
                        ):
                    if current_f1[elem] == current_f2[elem]:
                        lines[f'  {elem}'] = current_f1[elem]
                    if current_f1[elem] != current_f2[elem]:
                        lines[f'- {elem}'] = current_f1[elem]
                        lines[f'+ {elem}'] = current_f2[elem]
            if elem in keys_list1 and elem not in keys_list2:
                if isinstance(current_f1[elem], dict):
                    lines[f'- {elem}'] = iter_(
                        current_f1[elem], current_f1[elem]
                        )
                if not isinstance(current_f1[elem], dict):
                    lines[f'- {elem}'] = current_f1[elem]
            if elem not in keys_list1 and elem in keys_list2:
                if isinstance(current_f2[elem], dict):
                    lines[f'+ {elem}'] = iter_(
                        current_f2[elem], current_f2[elem]
                        )
                if not isinstance(current_f2[elem], dict):
                    lines[f'+ {elem}'] = current_f2[elem]
        return lines
    return iter_(f1, f2)

# функция определения расширения файла и возврат аргументов


def define_file_extension(first_file, second_file):
    filename1, file_extension1 = os.path.splitext(first_file)
    filename2, file_extension2 = os.path.splitext(second_file)
    if file_extension1 == '.json':
        f1 = json.load(open(first_file))
    elif file_extension1 == '.yaml' or file_extension1 == '.yml':
        f1 = yaml.safe_load(open(first_file))
    if file_extension2 == '.json':
        f2 = json.load(open(second_file))
    elif file_extension2 == '.yaml' or file_extension2 == '.yml':
        f2 = yaml.safe_load(open(second_file))
    return f1, f2

# проверка на пустоту файлов


def zero_check(file):
    res_1 = os.stat(file)
    result = res_1.st_size
    return result
