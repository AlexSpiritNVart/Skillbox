integer_input = input('Строка: ')
tuple_input = input('Кортеж чисел: ')[1:-1].split(',')

zip_func = ((value, int(tuple_input[count])) for count, value in enumerate(integer_input))

print(zip_func)
for i in zip_func:
    print(i)
