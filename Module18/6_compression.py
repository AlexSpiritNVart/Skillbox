user_input = list("aaAAbbсaaaA")
repeats = 1
new_pass = []
for count in range(len(user_input) - 1):
    if user_input[count] == user_input[count + 1]:
        repeats += 1
    else:
        new_pass.append(user_input[count])
        new_pass.append(str(repeats))
        repeats = 1
if user_input[-1] != user_input[-2]:
    new_pass.append(user_input[-1])
    new_pass.append(str(repeats))
print(''.join(new_pass))


