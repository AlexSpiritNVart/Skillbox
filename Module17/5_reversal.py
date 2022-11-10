user_inp = input('введите строку: ')

flag = False
first_count = 0
second_count = 0

for count, value in enumerate(user_inp):
    if value == 'h' and flag is False:
        first_count = count
        flag = True
    elif value == 'h' and flag is True:
        second_count = count - 1

print(user_inp[second_count:first_count:-1])
