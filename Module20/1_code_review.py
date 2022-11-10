students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def dictionary_reader(dict):
    id_plus_age = []
    hobby_list = []
    string = ''
    for key, value in dict.items():Ревью кода
        id_plus_age.append((key, value['age']))
        for i in value['interests']:
            hobby_list.append(i)
        string += value['surname']
    return id_plus_age, hobby_list, len(string)


some_shit = dictionary_reader(students)

print(f'Список пар "ID студента — возраст": {some_shit[0]} ')
print(f'Полный список интересов всех студентов: {some_shit[1]}')
print(f'Общая длина всех фамилий студентов: {some_shit[2]}')
