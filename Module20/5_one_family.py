family = {
    ('Сидоров', 'Иван'): 36,
    ('Сидорова', 'Алина'): 38,
    ('Сидоров', 'Николай'): 26,
    ('Петров', 'Павел'): 16,
    ('Петров', 'Никита'): 44,
    ('Петрова', 'Наталья'): 61,
    ('Петрова', 'Надежда'): 22,
}
user_input = input("Введите фамилию: ").lower()

for key, value in family.items():
    surname = key[0].lower()
    if surname.startswith(user_input) or surname.startswith(user_input[:-1]):
        print(key[0], key[1], value)
