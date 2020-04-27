# converting negative numbers to positive numbers and vice versa


def invert(lst):
    inverted_list = []
    for element in lst:
        inverted_list.append(element * (-1))
    return inverted_list


print(invert([1, 4, 8, 10]))
