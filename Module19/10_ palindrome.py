def is_poly(string):
    letters_dict = dict()
    for letter in string:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

    odd_count = 0
    for i in letters_dict.values():
        if i % 2 != 0:
            odd_count += 1
    return odd_count <= 1


user_input = input('Введите строку: ')

if is_poly(user_input):
    print('Можно сделать полиндром')
else:
    print("Нельзя сделать полиндром")
