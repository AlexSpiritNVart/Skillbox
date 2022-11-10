def ten_numbers(number):
    if number !=0:
        ten_numbers(number-1)
    print(number)


ten_numbers(10)
