# znajduje pierwsza nie-kolejna liczbe


def first_non_consecutive(arr):
    consecutive_arr = range(arr[0], len(arr) + arr[0])

    index = 0
    for element in arr:
        if element != consecutive_arr[index]:
            return element
        index += 1


print(first_non_consecutive([1, 2, 3, 8]))
print(first_non_consecutive([-4, -3, 0, 1]))
