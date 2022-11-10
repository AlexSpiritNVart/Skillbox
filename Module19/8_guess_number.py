import random
max_number = int(input('Введите максимальное число: '))
artem_number = str(random.randint(0, max_number))
# first_input = input('Нужное число есть среди вот этих чисел: ').split()
comb = set()
# if artem_number in first_input:
#     print('Да')
#     comb.add(first_input)
# else:
#     print('Нет')

is_first_time = False
while True:
    boris_input = input('Нужное число есть среди вот этих чисел: ')
    if boris_input == 'Помогите!':
        print("Артём мог загадать следующие числа:", comb)
        break
    boris_input = set(boris_input.split())
    if artem_number in boris_input and not is_first_time:
        print('Да')
        comb |= boris_input
        is_first_time = True
        # записываем множество.
    elif artem_number in boris_input and is_first_time:
        print('Да')
        comb &= boris_input
    else:
        print("Нет")
        comb -= boris_input
        # разность множества
