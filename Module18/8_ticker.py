first_string = input('ведите первую строку ')
second_string = input('ведите вторую строку ')
for comb in range(len(first_string)):
    if first_string == second_string:
        print(f'Первая строка получается из второй со сдвигом {comb}')
        break
    second_string = '{}{}'.format(second_string[1:],second_string[0])
    if comb == len(first_string) - 1:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига')
