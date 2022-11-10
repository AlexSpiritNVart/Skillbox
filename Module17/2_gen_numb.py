user_numb = int(input('ведите число: '))

output_mass = [(1 if numb % 2 == 0 else numb % 5)for numb in range(user_numb)]

print(output_mass)
