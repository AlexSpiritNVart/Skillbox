pair_count = int(input('Введите количество пар слов: '))

synonyms = dict()

for i in range(pair_count):
    pair = input(f'{i+1} пара: ').lower().split()
    synonyms[pair[0]] = pair[2]


def return_name(val):
    for key, value in synonyms.items():
        if val == value:
            return key


while True:
    user_input = input('Введите слово: ').lower()
    if user_input in synonyms.keys():
        print(f"Синоним: {synonyms[user_input]}")
    elif user_input in synonyms.values():
        print(f"Синоним: {return_name(user_input)}")
    elif user_input == 'end':
        break
    else:
        print(f'слова {user_input} нет в словаре')
