import random

sticks_in_row = [i for i in range(1, int(input('количество палок: ')))]
threw_stones = int(input('количество камней: '))

for K in range(1,threw_stones+1):
    print(f'___Бросок {K}___')
    Left_i = random.randint(1, len(sticks_in_row) - 1)
    Right_i = random.randint(Left_i, len(sticks_in_row))
    print(f'___Сбиты палки с {Left_i} по {Right_i} ___')
    for i in range(Left_i, Right_i + 1):
        sticks_in_row[i-1] = 0
    print(f"Остались в списке {sticks_in_row}")
draw_sticks = [("." if i == 0 else "I") for i in sticks_in_row]
print(''.join(draw_sticks))
