

while True:
    min_simb = False
    big_lett = False
    min_numb = False
    numbers = 0
    user_input = input('Введите пароль:  ')
    for letter in user_input:
        if letter.isupper():
            big_lett = True
        elif letter.isdigit():
            numbers += 1
    if len(user_input) >= 8:
        min_simb = True
    if numbers == 3:
        min_numb = True
    results = [big_lett,min_numb,min_simb]
    if all(results):
        break
    else: print('Пароль не верный, введите верный пароль ')

print('Проверка прошла успешно  ')
