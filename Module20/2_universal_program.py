def is_prime(number):
    k = 0
    for i in range(2, number // 2 ):
        if (number % i == 0):
            k = k + 1
    if (k <= 0) and number != 1:
        return number
    else:
        return False


def crypto(mass):
    new_mass = []
    for count, value in enumerate(mass):
        prime_number = is_prime(count)
        if prime_number:
            new_mass.append(value)
        else:
            pass
    return new_mass


# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))