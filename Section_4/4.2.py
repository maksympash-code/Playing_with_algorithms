def count_el(array):
    if array == []:
        return 0
    else:
        return 1 + count_el(array[1:])

print(count_el([1, 2, 3, 4, 5]))