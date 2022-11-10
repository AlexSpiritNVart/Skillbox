import random

user_input = random.randint(0, 30)

list_of_numb = [random.randint(0, 2) for _ in range(random.randint(0, 30))]

count_of_zeros = 0
for count, value in enumerate(list_of_numb):
    if value == 0:
        count_of_zeros += 1

for zeros in range(count_of_zeros):
    list_of_numb.remove(0)
    
print(list_of_numb)
