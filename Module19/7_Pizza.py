orders = int(input('Введите количество заказов: '))

order_dict = dict()
for order in range(orders):
    user_input = input(f'{order+1} заказ: ').split()
    name = user_input[0]
    pizza = user_input[1]
    quantity = int(user_input[2])
    if name in order_dict:
        if pizza in order_dict[name].keys():
            order_dict[name][pizza] += quantity
        else:
            order_dict[name][pizza] = quantity
    else:
        order_dict[name] = dict()
        order_dict[name][pizza] = quantity


for name in order_dict.keys():
    print(name)
    for key, value in order_dict[name].items():
        print(key, ':', value)
