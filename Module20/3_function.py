def slicer(cort, number):
    cort = list(cort[:])
    number_1 = cort.index(number)
    number_2 = cort.index(number, number_1 + 1)
    return tuple(cort[number_1:number_2])

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))