import json
import os
#from pathlib import Path


def generate_diff(first_file, second_file):
    first_size = zero_check(first_file)
    second_size = zero_check(second_file)
    if first_size == 0 or second_size == 0:
        return 'nothing to diff'
    summ_dict = {}
    f1 = json.load(open(first_file))
    f2 = json.load(open(second_file))
    keys_list1 = set(f1.keys())
    keys_list2 = set(f2.keys())
    # общий список всех ключей из двух файлов
    keys_list = keys_list1 | keys_list2
    for elem in keys_list:
        if elem in f1 and elem in f2:  # случай 1. Ключ есть в обоих словарях:
            if f1[elem] == f2[elem]:  # случай 1.1. значения ключей равны
                # добавили в результирующий словарь ключ и значение
                summ_dict[f'%{elem}'] = f1[elem]
            # если значения не равны записываем из
            # первого словая с - из второго с +
            elif f1[elem] != f2[elem]:
                summ_dict[f'-{elem}'] = f1[elem]
                summ_dict[f'+{elem}'] = f2[elem]
        # если элемент есть в списке ф1 и его нет в списке ф2
        elif elem in f1 and elem not in f2:
            summ_dict[f'-{elem}'] = f1[elem]
        elif elem in f2 and elem not in f2:
            summ_dict[f'+{elem}'] = f2[elem]
    # приведение булевых объектов к строке и в нижний регистр
    for elem in summ_dict:
        if type(summ_dict[elem]) == bool:
            summ_dict[elem] = str(summ_dict[elem]).lower()
    result = dict_transform(summ_dict)
    #print(result)
    return result

# проверяет файлы на пустоту


def zero_check(file):
    res_1 = os.stat(file)
    result = res_1.st_size
    return result

# сортирует и трансформирует словарь в нужный вид


def dict_transform(summ_dict):
    summ_list = list(sorted(summ_dict.items(), key=sort_key))
    summ_dict = dict(summ_list)
    summ_str = str(summ_dict)
    summ_str = summ_str.replace(',', '\n')
    summ_str = summ_str.replace('%', '    ')
    summ_str = summ_str.replace("'", '')
    summ_str = summ_str.replace('-', '  - ')
    summ_str = summ_str.replace('   -', '  -')
    summ_str = summ_str.replace(' +', '  + ')
    summ_str = summ_str.replace('     ', '    ')
    summ_str = summ_str[:1] + '\n' + summ_str[1:-1] + '\n' + summ_str[-1:]
    #print(summ_str)
    return (summ_str)

# функция сортировки по алфавиту без учета минусов и плюсов


def sort_key(e):
    word = e[0]
    return word[1]

#current_dir = Path(__file__).parent
#print(current_dir)
#generate_diff(current_dir / 'tests' / 'fixtures' / 'file1.json', current_dir / 'tests' / 'fixtures' / 'file2.json')
