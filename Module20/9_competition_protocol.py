record_count = int(input('Сколько записей вносится в протокол? '))

player_list = [input(f'{i+1}-я запись: ').split() for i in range(record_count)]


#
# player_list = [
#     ['69485', 'Jack'],
#     ['95715', 'qwerty'],
#     ['95715', 'Alex'],
#     ['83647', 'M'],
#     ['197128', 'qwerty'],
#     ['95715', 'Jack'],
#     ['93289', 'Alex'],
#     ['95715', 'Alex'],
#     ['95715', 'M']
#     ]

for i in range(len(player_list)):
    for count, value in enumerate(player_list):
        if count == len(player_list)-1:
            break
        elif int(value[0]) < int(player_list[count+1][0]):
            player_list[count], player_list[count + 1] = player_list[count + 1], player_list[count]


def check_the_winner():
    for i in range(3):
        if player_list[i][1] == player_list[i+1][1]:
            if int(player_list[i][0]) > int(player_list[i+1][0]):
                player_list.pop(i+1)
            else:
                player_list.pop(i)
    return player_list[:3]


for count, value in enumerate(check_the_winner()):
    print(f'{count+1}-е место {value[1]} ({value[0]})')
