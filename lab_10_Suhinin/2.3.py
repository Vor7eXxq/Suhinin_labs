def find_max(lst):
    if len(lst) == 1:  # базовий випадок
        return lst[0]

    max_of_rest = find_max(lst[1:])

    return lst[0] if lst[0] > max_of_rest else max_of_rest
print(find_max([3,7,2,9,1]))