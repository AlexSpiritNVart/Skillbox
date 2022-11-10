nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = []
[[[new_list.append(i) for i in third_itr] for third_itr in second_itr] for second_itr in nice_list]

print(new_list)
