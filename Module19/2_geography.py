countries_quantity = int(input('Количество стран: '))
countries_dictionary = dict()
for country in range(countries_quantity):
    country_and_city = input(f'{country+1} страна: ').split()
    countries_dictionary[country_and_city[0]] = country_and_city[1:]

for number in range(3):
    user_input = input(f'{number+1} город: ')
    for country in countries_dictionary.keys():
        if user_input in countries_dictionary[country]:
            print(f'Город {user_input} расположен в стране {country}')
        else:
            print(f'По городу {user_input} данных нет')