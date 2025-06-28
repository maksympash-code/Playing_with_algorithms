def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i < pivot]

        greatest = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greatest)


if __name__ == '__main__':
    print(quick_sort([5, 4, 3, 2, 1]))