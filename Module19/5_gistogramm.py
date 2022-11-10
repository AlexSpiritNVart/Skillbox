user_input = input('Введите текст: ')
text_dict = dict()


for simb in user_input:
    if simb in text_dict.keys():
        text_dict[simb] += 1
    else:
        text_dict[simb] = 1


inverted_dict = dict()
for key, value in text_dict.items():
    if value in inverted_dict.keys():
        inverted_dict[value].append(key)
    else:
        inverted_dict[value] = [key]


for key, value in inverted_dict.items():
    print(key,':', value)
