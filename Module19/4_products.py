goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def return_name(val):
    for key, value in goods.items():
        if val == value:
            return key


for key, value in store.items():
    sum_furniture = 0
    count_furniture = 0
    for elem in value:
        sum_furniture += elem["quantity"] * elem["price"]
        count_furniture += elem["quantity"]
    print(f'{return_name(key)} - {count_furniture} штук, стоимостью {sum_furniture} штук ')
