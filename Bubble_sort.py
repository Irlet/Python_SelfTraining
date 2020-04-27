list_to__be_sorted = [3, 12, -1, 6, 15, 356, 1, 0]

# ascending:


def sort_ascending(unsorted_list):
    n = len(unsorted_list)
    while n > 1:
        for i in range(n-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                tmp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = tmp
        n -= 1
    return unsorted_list


print(sort_ascending(list_to__be_sorted))

# descending:


def sort_descending(unsorted_list):
    n = len(unsorted_list)
    while n > 1:
        for i in range(n-1):
            if unsorted_list[i] < unsorted_list[i+1]:
                tmp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = tmp
        n -= 1
    return unsorted_list


print(sort_descending(list_to__be_sorted))
