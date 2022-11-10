def tpl_sort(*kwargs):
    cort_to_sort = list(kwargs)
    cort_to_sort_origin = cort_to_sort[:]
    for i in range(len(cort_to_sort)-1):
        if type(cort_to_sort[i]) == float:
            return tuple(cort_to_sort_origin)
        for j in range(len(cort_to_sort)-1):
            if cort_to_sort[j] > cort_to_sort[j+1]:
                cort_to_sort[j], cort_to_sort[j + 1] = cort_to_sort[j+1], cort_to_sort[j]
    return tuple(cort_to_sort)


print(tpl_sort(6, 3, -1, 8, 4.5, 10, -5))
