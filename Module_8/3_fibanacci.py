def fib(numb):
    if numb <= 2:
        return 1
    return fib(numb-1) + fib(numb-2)


print(fib(int(input('Введите число: '))))
