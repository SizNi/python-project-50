import json
def main(first_file, second_file):
    summ_dict = {}
    f1 = json.load(open(first_file))
    f2 = json.load(open(second_file))
    keys_list1 = set(f1.keys())
    keys_list2 = set(f2.keys())
    keys_list = keys_list1 | keys_list2  # общий список всех ключей из двух файлов
    for elem in keys_list:
        if elem in f1 and elem in f2:  # случай 1. Ключ есть в обоих словарях:
            if f1[elem] == f2[elem]:  # случай 1.1. значения ключей равны
                summ_dict[f'%{elem}'] = f1[elem]  # добавили в результирующий словарь ключ и значение
            elif f1[elem] != f2[elem]:  # если значения не равны записываем из первого словая с - из второго с +                    
                summ_dict[f'-{elem}'] = f1[elem]
                summ_dict[f'+{elem}'] = f2[elem]
        elif elem in f1 and elem not in f2:  # если элемент есть в списке ф1 и его нет в списке ф2
            summ_dict[f'-{elem}'] = f1[elem]
        elif elem in f2 and elem not in f2:
            summ_dict[f'+{elem}'] = f2[elem]
    for elem in summ_dict:  # приведение булевых объектов к строке и в нижний регистр
        if type(summ_dict[elem]) == bool:
            summ_dict[elem] = str(summ_dict[elem]).lower()
    result = dict_transform(summ_dict)
    return result



def dict_transform(summ_dict):  # сортирует и трансформирует словарь в нужный вид
    summ_list = list(sorted(summ_dict.items(), key = sort_key))
    summ_dict = dict(summ_list)
    summ_str = str(summ_dict)
    summ_str = summ_str.replace(',', '\n')
    summ_str = summ_str.replace(' ', '')
    summ_str = summ_str.replace("'", '')
    summ_str = summ_str.replace('-', '  - ')
    summ_str = summ_str.replace('+', '  + ')
    summ_str = summ_str.replace('%', '    ')
    summ_str = summ_str[:1] +'\n' + summ_str[1:-1] + '\n' + summ_str[-1:]
    return(summ_str)


def sort_key(e):  # функция сортировки по алфавиту без учета минусов и плюсов
    word = e[0]
    return word[1]


def generate_diff(first_file, second_file):  # функция, вызывающая main, чтоб при импорте модуля это все не сработало
    if __name__ == 'gendiff':
        return main(first_file, second_file)

