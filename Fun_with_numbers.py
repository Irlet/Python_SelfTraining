"""
no imports, no list comprehensions, no lambdas, no enumerate!
"""


def get_odd_elements(x, start):
    """ Return a list containing first 'x' odd elements starting from 'start'"""

    list_x_odd_elemets = []
    element = start
    if x <= 0:
        raise ValueError('Numbers count parameter must be greater than zero')
    while len(list_x_odd_elemets) < x:
        if element % 2 != 0:
            list_x_odd_elemets.append(element)
        element += 1
    return list_x_odd_elemets


print(get_odd_elements(6, 21))


def get_even_numbers(x, stop, z):
    """Returns a list containing first 'x' even elements lower than 'stop'.
       Those elements must be divisible by 'z' """

    result = []
    number = stop - 1
    while len(result) < x:
        if number % z == 0 and number % 2 == 0:
            result.append(number)
        number -= 1
    return result


print(get_even_numbers(4, 29, 3))


def get_sum_of_greatest_elements(my_list, x):
    """Returns a single integer, which is a sum of  'x' biggest elements from 'my_list'
       i.e. Returns a sum of 3 biggest elements from [2, 18, 5, -11, 7, 6, 9]"""

    result = 0
    n = len(my_list)
    for i in range(n):
        for j in range(i+1, n):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    for i in range(x):
        result += my_list[i]

    return result


my_list = [1, 8, 3, 7, 5, 19]
print(get_sum_of_greatest_elements(my_list, 3))


# The same, but with a different sorting method:

def get_sum_of_greatest_elements2(my_list, x):
    result = 0
    n = len(my_list)
    while n > 1:
        for i in range(n-1):
            if my_list[i] < my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        n -= 1
    for i in range(x):
        result += my_list[i]

    return result


my_list = [1, 8, 3, 7, 5, 19]
print(get_sum_of_greatest_elements2(my_list, 3))


def get_average_of_elements(first_list, second_list):
    """Returns a single integer, which is an average from elements that are on
       'first_list' but not on 'second_list'"""

    extract = []
    result = 0
    for element in first_list:
        if element not in second_list:
            extract.append(element)
    for element in extract:
        result += element
    n = len(extract)
    return result/n


print(get_average_of_elements([1, 2, 3, 4], [2, 4, 5, 8]))


def get_max_common_element(first_list, second_list):
    """Select common elements from both lists and return one with the max value.
       :raises ValueError: if any of the input lists are empty.
       Error message: 'Input lists cannot be empty'
       :raises ValueError: if there are no common elements.
       Error message: 'There are no common elements' """

    common_list = []
    if first_list == [] or second_list == []:
        raise ValueError('Input lists cannot be empty')
    for element in first_list:
        if element in second_list:
            common_list.append(element)
    if common_list == []:
        raise ValueError('There are no common elements')
    n = len(common_list)
    for i in range(n):
        for j in range(i+1, n):
            if common_list[i] < common_list[j]:
                common_list[i], common_list[j] = common_list[j], common_list[i]

    return common_list[0]


print(get_max_common_element([1, 4, 3, 2, 10], [2, 4, 5, 8, 10]))
# print(get_max_common_element([1, 3, 2, 10], []))
# print(get_max_common_element([1, 3, 2, 10], [4, 5, 8]))


# The same, but with a different sorting method:

def get_max_common_element2(first_list, second_list):
    common_list = []
    if first_list == [] or second_list == []:
        raise ValueError('Input lists cannot be empty')
    for element in first_list:
        if element in second_list:
            common_list.append(element)
    if common_list == []:
        raise ValueError('There are no common elements')
    n = len(common_list)
    while n > 1:
        for i in range(n-1):
            if common_list[i] < common_list[i+1]:
                common_list[i], common_list[i+1] = common_list[i+1], common_list[i]
        n -= 1
    return common_list[0]


print(get_max_common_element2([1, 4, 3, 2, 10], [2, 4, 5, 8, 10]))
