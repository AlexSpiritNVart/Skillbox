phonebook = dict()


def add_contact(phonebook, name_and_surname, phone_number):
    phonebook[name_and_surname] = phone_number
    return phonebook


def find_contact(phonebook, surname):
    intermediate_phonebook = dict()
    for key, value in phonebook.items():
        if surname in key:
            key = key.split()
            key = (key[0], key[1])
            intermediate_phonebook[key] = value
    return intermediate_phonebook


while True:

    user_input = int(input('Введите номер действия: 1. Добавить контакт 2. Найти человека 3. Выход '))

    if user_input == 1:
        name_and_surname = input('Введите имя и фамилию нового контакта (через пробел): ')
        phone_number = int(input('Введите номер телефона: '))
        print(add_contact(phonebook, name_and_surname, phone_number))

    elif user_input == 2:
        surname = input('Введите фамилию для поиска: ')
        print(find_contact(phonebook, surname))

    elif user_input == 3:
        break
