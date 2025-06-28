def max_element(array):
    if len(array) == 1:
        return array[0]
    else:
        max_el = max_element(array[1:])
        return array[0] if array[0] > max_el else max_el


print(max_element([1, 200, 5, 70, 24]))