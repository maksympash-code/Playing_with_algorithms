def sum(array):
    if array == []:
        return 0
    else:
        return array[0] + sum(array[1:])


print(sum([1, 2, 3, 4, 5]))