import itertools


def stylish(value, replacer='    ', spaces_count=1):
    def iter_(current_value, depth):
        # если не словарь - возвращаем строчное значение value
        if isinstance(current_value, bool):
            return str(current_value).lower()
        if current_value is None:
            return 'null'
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent_size = depth + spaces_count  # отсчет количества отступов
        # умножаем количество отступов на значение отступа
        deep_indent = replacer * deep_indent_size
        # текущий отступ (в начале = 0, тк depth = 0)
        current_indent = replacer * depth
        lines = []
        # для ключа и значения в value
        for key, val in current_value.items():
            lines.append(
                f'{deep_indent[:-2]}{key}: {iter_(val, deep_indent_size)}'
            )
        # добавляет открывающие и закрывающие скобки
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
