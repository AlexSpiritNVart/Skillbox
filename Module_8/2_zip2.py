def shotest(first_mass, second_mass):
    return sorted([first_mass, second_mass], key=len)[0]


numbers_1 = 'asda'
numbers_2 = ['asda','asdghr',2.3]

par_gen = ((numbers_1[i],numbers_2[i]) for i in range(len(shotest(numbers_1, numbers_2))))

par_list = list(par_gen)

print(par_list)
