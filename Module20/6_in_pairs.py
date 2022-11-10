import random

random_number = [random.randint(0,100) for _ in range(10)]

numbers_cort = zip(random_number[0:5], random_number[5:10])

print(list(numbers_cort))
