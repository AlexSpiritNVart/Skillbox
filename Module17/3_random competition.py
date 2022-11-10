import random

first_team = [round(random.uniform(5, 10), 2) for i in range(20)]
second_team = [round(random.uniform(5, 10), 2) for i2 in range(20)]
winners = [(first_team[num] if first_team[num] > second_team[num] else second_team[num]) for num in range(20)]

print(first_team)
print(second_team)
print(winners)
