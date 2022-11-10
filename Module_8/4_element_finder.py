key_user_input = input('Введите искомый ключ: ')


def need_a_depth():
    while True:
        is_depth_input = input('Хотите ввести максимальную глубину? Y/N: ').lower()
        if is_depth_input == 'y':
            max_depth_input = int(input('Введите максимальную глубину: '))
            return max_depth_input
        elif is_depth_input == 'n':
            return None
        else:
            print('непонятен ввод, введите Y/N ')


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def key_finder(key_to_find, where_to_find, depth):
    if depth == 0:
        result = None
    else:
        if key_to_find in where_to_find:
            return where_to_find[key_to_find]

        for sub_struct in where_to_find.values():
            if isinstance(sub_struct, dict):
                result = key_finder(key_to_find, sub_struct, depth-1)
                if result or depth == 0:
                    break
        else:
            result = None
    return result


depth = need_a_depth()
value = key_finder(key_user_input,site,depth)

print(f'Значение ключа: {value}')
