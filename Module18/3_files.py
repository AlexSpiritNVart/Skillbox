user_input = input('Полное название файла: ')
not_possible_simb = list('@№$%^&*()')

if not user_input.endswith('.txt') and not user_input.endswith('.docx'):
    print('неверное расширение файла. Ожидалось .txt или .docx.')
elif not all(simb in user_input for simb in not_possible_simb):
    print('название начинается на один из специальных символов')
else:
    print('Файл назван верно.')
