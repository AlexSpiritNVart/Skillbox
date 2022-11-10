user_input = input('Введите строку: ')

words_list = user_input.split(' ')

for word in range(len(words_list)-1):

    if len(words_list[word]) >= len(words_list[word + 1]):
        longest_word = words_list[word]
    else:
        longest_word = words_list[word + 1]
print(f'Самое длинное слово: {longest_word}')
print(f'Длинна этого слова: {len(longest_word)}')
