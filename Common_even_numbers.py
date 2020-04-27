first = [1, 2, 3, 4, 5, 6, 7]
second = [4, 5, 6, 7, 8, 9, 10]


def get_common_even_el(first, second):
    if len(first) < 1 or len(second) < 1:
        raise ValueError("List cannot be empty)")
    result = []
    for element in first:
        if element in second and element % 2 == 0:
            result.append(element)
    return result


print(get_common_even_el(first, second))


def get_common_odd_el(first, second):
    if len(first) < 1 or len(second) < 1:
        raise ValueError("List cannot be empty)")
    result = []
    for element in first:
        if element in second and element % 2 != 0:
            result.append(element)
    return result


print(get_common_odd_el(first, second))


def get_not_common_odd_el(first, second):
    if len(first) < 1 or len(second) < 1:
        raise ValueError("List cannot be empty)")
    result = []
    for element in first:
        if element not in second and element % 2 != 0:
            result.append(element)
    for element in second:
        if element not in first and element % 2 != 0:
            result.append(element)

    return result


print(get_not_common_odd_el(first, second))


def get_not_common_even_el(first, second):
    if len(first) < 1 or len(second) < 1:
        raise ValueError("List cannot be empty)")
    result = []
    for element in first:
        if element not in second and element % 2 == 0:
            result.append(element)
    for element in second:
        if element not in first and element % 2 == 0:
            result.append(element)

    return result


print(get_not_common_even_el(first, second))
