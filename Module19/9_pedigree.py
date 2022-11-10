quantity = int(input('Введите количество человек: '))

family_tree = dict()

for i in range(quantity):
    pair = input(f'{i+1} пара: ').split()
    offspring_name = pair[0]
    parent_name = pair[1]
    if parent_name not in family_tree.keys():
        family_tree[parent_name] = 0
    family_tree[offspring_name] = family_tree[parent_name]+1

for key in sorted(family_tree.keys()):
    print(key, family_tree[key])
