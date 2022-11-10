alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
user_inp = input('Введите текст:  ')
k = int(input('Введите значение сдвига:  '))

new = list(alph)
new.extend(new[0:k])

for _ in range(k):
    new.remove(new[0])

text = [(new[alph.index(letter)] if letter in alph else ' ') for letter in user_inp]

print(''.join(text))
