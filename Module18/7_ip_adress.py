# user_input = '192.168.250.57'

# user_input_divided = user_input.split('.')
#
# if len(user_input_divided) != 4:
#     print('Адрес — это четыре числа, разделённые точками.')

# for numb in user_input_divided:
#     if numb.isdigit() and 0 <= int(numb) <= 255:

# correct_mass = [True if numb.isdigit() and 0 <= int(numb) <= 255 else False for numb in user_input_divided]
#
# print(correct_mass)

# letters = list('qwertyuiopasdfghjklzxcvbnm')
# splitted_input = [simb for simb in user_input]
# print(splitted_input)
# print(letters)
# if not all(letter in letters for letter in splitted_input):
#     print('в адресе буквы')
#секционно
# for i in range(6):
#     splitted_input = user_input.split('.')
#     for part in user_input:
#         if 0 < int(part) < 256 and not ',' in splitted_input:
#             print('IP-адрес корректен')
### TODO не выполняется проверка на наличие букв в адресе


while True:
    usr = input('IP -> ')
    user = usr.split('.')
    if len(user) == 4:
        for _ in user:
            if not _.isdigit() or int(_) < 0 or int(_) > 256:
                print('Error', _)
                break
        else:
            exit('Good')
