list_to__be_sorted = [3, 12, -1, 6, 15, 356, 1, 0]

# ascending:


def sort(unsorted_list):
    n = len(unsorted_list)
    while n > 1:
        for i in range(n-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                tmp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = tmp
        n -= 1
    return unsorted_list


print(sort(list_to__be_sorted))

# descending:


def descending_order(unsorted_list):
    n = len(unsorted_list)
    while n > 1:
        for i in range(n-1):
            if unsorted_list[i] < unsorted_list[i+1]:
                tmp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = tmp
        n -= 1
    return unsorted_list


print(descending_order(list_to__be_sorted))
