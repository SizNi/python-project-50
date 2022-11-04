def plain(lines):
    result = plain_format(lines)
    return gendiff_plain(result)


def plain_format(d, parent_key: str = '', sep: str = '.'):  # получает путь и значение и преобразует в формат для обработки
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k[2:] if parent_key else k[2:]
        if k[0] in ['+', '-']:
            items.append((new_key, v, k[0]))
        elif isinstance(v, dict):
            items.extend(plain_format(v, new_key, sep=sep))
        else:
            items.append((new_key, v, k[0]))
    return items


def gendiff_plain(value):
    i = 0
    summ_list = []
    for i in range(len(value)):
        path = value[i]
        if i + 1 < len(value):  # проверка на существование следующего элемента в списке value
            next_path = value[i + 1]
        else:
            next_path = (None, None, None)
        previous_path = value[i - 1]
        if path[2] == '-':  # если в кортеже -
            if path[0] != next_path[0]:  # если путь первого кортежа не равен пути второго кортежа
                summ_list.append(f"Property '{path[0]}' was removed")
                i += 1
            elif path[0] == next_path[0]:  # если пути в кортежах равны
                summ_list.append(
                    f"Property '{path[0]}' was updated. From {path_check(path[1])} to {path_check(next_path[1])}"
                    )
                i += 2
        elif path[2] == '+':  # если в кортеже +
            if path[0] != previous_path[0]: # если пути в кортежах не равны
                summ_list.append(
                    f"Property '{path[0]}' was added with value: {path_check(path[1])}"
                )
                i += 1
        elif path[2] == ' ':
            i += 1
    a = '\n'.join(summ_list)
    return a


def path_check(value):  # если словарь - заменяем на [complex value], булевое и нон - к нижнему
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(f"'{value}'")

# gendiff_plain(value)