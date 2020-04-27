def get_x_lowest_elements(numbers, x):
    low_num_list = []
    if numbers == []:
        raise ValueError(' Input list cannot be empty')
    if x <= 0:
        raise ValueError('Enter positive number of elements')
    while len(low_num_list) < x:
        low_num = numbers[0]
        for num in numbers:
            if num < low_num:
                low_num = num
        low_num_list.append(low_num)
        numbers.remove(low_num)

    return low_num_list


print(get_x_lowest_elements([4, 2, 15, 7, 2, 9], 3))

# Another way of sorting:


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


def get_x_lowest_elements2(numbers, x):
    if numbers == []:
        raise ValueError('Input list cannot be empty')
    if x <= 0:
        raise ValueError('Enter positive number of elements')
    if x > len(numbers):
        raise ValueError('List lenght is less than {}'.format(x))
    low_num_list = []
    sorted_num = sort(numbers)

    for i in range(x):
        low_num_list.append(sorted_num[i])
    return low_num_list


print(get_x_lowest_elements2([4, 2, 15, 7, 0, 2, 9, -1, -1], 5))
