user_input = input('введите текст: ')
user_input = user_input.split(' ')
encoded_message = []
simb_list = '!@#$%^&*(_)><?.,;:'

for element in range(len(user_input)):
    for simb in user_input[element]:
        if simb in simb_list:
            global user_input_news
            user_input_new = '{letters}{punctuation}'.format(
                letters=user_input[element][-2::-1],
                punctuation=user_input[element][-1]
            )
        else:user_input_new=user_input[element][::-1]
    encoded_message.append(user_input_new)
print(' '.join(encoded_message))
