def binary_search(list, item):
    l = 0
    r = len(list) - 1

    while l <= r:
        mid = (l + r) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            r = mid - 1
        if guess < item:
            l = mid + 1
    return None

if __name__ == '__main__':
    list = [1, 3, 5, 7, 9]

    print(binary_search(list, 3))
    print(binary_search(list, -1 ))