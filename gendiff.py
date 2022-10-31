import json
import os
# from pathlib import Path
import yaml


def generate_diff(first_file, second_file):
    first_size = zero_check(first_file)
    second_size = zero_check(second_file)
    if first_size == 0 or second_size == 0:
        return 'nothing to diff'
    # определение расширения файла и возврат списка ключей и path файлов ф1 ф2
    keys_list, f1, f2 = define_file_extension(first_file, second_file)
    # вызов функции, работающей со словарями
    return generate_diff_second_step(keys_list, f1, f2)


def generate_diff_second_step(keys_list, f1, f2):
    summ_dict = {}
    # print(keys_list)
    # общий список всех ключей из двух файлов
    for elem in keys_list:
        if elem in f1 and elem in f2:  # случай 1. Ключ есть в обоих словарях:
            if f1[elem] == f2[elem]:  # случай 1.1. значения ключей равны
                # добавили в результирующий словарь ключ и значение
                summ_dict[f'  {elem}'] = f1[elem]
            # если значения не равны записываем из
            # первого словая с - из второго с +
            elif f1[elem] != f2[elem]:
                summ_dict[f'- {elem}'] = f1[elem]
                summ_dict[f'+ {elem}'] = f2[elem]
        # если элемент есть в списке ф1 и его нет в списке ф2 и наоборот
        elif elem in f1 and elem not in f2:
            summ_dict[f'- {elem}'] = f1[elem]
        elif elem in f2 and elem not in f1:
            summ_dict[f'+ {elem}'] = f2[elem]
    # приведение булевых объектов к строке и в нижний регистр
    for elem in summ_dict:
        if type(summ_dict[elem]) == bool:
            summ_dict[elem] = str(summ_dict[elem]).lower()
    result = dict_transform(summ_dict)
    print(result)
    return result

# проверяет файлы на пустоту


def zero_check(file):
    res_1 = os.stat(file)
    result = res_1.st_size
    return result

# сортирует и трансформирует словарь в нужный вид


def dict_transform(summ_dict):
    lines = []
    lines.append('{')
    keys_dict = []
    keys_dict = summ_dict.keys()
    keys_dict = sorted(keys_dict, key=sort_key)
    for elem in keys_dict:
        lines.append(f'  {elem}: {summ_dict[elem]}')
    lines.append('}')
    summ_str = '\n'.join(lines)
    return (summ_str)

# функция сортировки по алфавиту без учета минусов и плюсов


def sort_key(key):
    return key[2:]

# функция определения расширения файла и возврат аргументов


def define_file_extension(first_file, second_file):
    filename1, file_extension1 = os.path.splitext(first_file)
    filename2, file_extension2 = os.path.splitext(second_file)
    if file_extension1 == '.json':
        f1 = json.load(open(first_file))
        keys_list1 = set(f1.keys())
    elif file_extension1 == '.yaml' or file_extension1 == '.yml':
        f1 = yaml.safe_load(open(first_file))
        keys_list1 = set(f1.keys())
    if file_extension2 == '.json':
        f2 = json.load(open(second_file))
        keys_list2 = set(f2.keys())
    elif file_extension2 == '.yaml' or file_extension2 == '.yml':
        f2 = yaml.safe_load(open(second_file))
        keys_list2 = set(f2.keys())
    keys_list = keys_list1 | keys_list2
    return keys_list, f1, f2

# current_dir = Path(__file__).parent
# print(current_dir)
# generate_diff(current_dir / 'tests' / 'fixtures' / 'file1.json',
# current_dir / 'tests' / 'fixtures' / 'file2.json')
# generate_diff(current_dir / 'tests' / 'fixtures' / 'filepath1.yml',
# current_dir / 'tests' / 'fixtures' / 'filepath2.yaml')
