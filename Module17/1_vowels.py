vowels_list = ["у","е","ы","а","о","э","я","и","ю"]
user_input = input("введите текст")

vowels_in_text = []

a = [(vowels_in_text.append(letter) if letter in vowels_list else None) for letter in user_input]

print(vowels_in_text)