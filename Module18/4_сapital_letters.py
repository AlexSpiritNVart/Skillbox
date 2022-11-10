user_input = input('Введите строку: ')
word_list = user_input.split()
new_word_list = [word_list[word][0].upper() + word_list[word][1:].lower() for word in range(len(word_list))]

print(' '.join(new_word_list))
