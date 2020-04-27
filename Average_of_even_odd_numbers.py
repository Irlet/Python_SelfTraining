""" def average_of_first_x_even_numbers(x, start=0)
raise ValueError ('Numbers count parametr must be greater than zero')
example: x=3
start =20
result = [20,22,24] / x = 22 """


def average_of_first_x_even_numbers(x, start):

    first_x_even_numbers = []

    if x <= 0:
        raise ValueError('Numbers count parameter must be greater than zero')

    for element in range(start, (start+(x*2))):
        if element >= start and element % 2 == 0 and len(first_x_even_numbers) <= x:
            first_x_even_numbers.append(element)

    average_result = sum(first_x_even_numbers) / x
    return average_result


print(average_of_first_x_even_numbers(3, 20))


# For odd numbers:


def average_of_first_x_odd_numbers(x, start):
    average = 0
    list_numbers = []
    element = start
    if x <= 0:
        raise ValueError('Numbers count parameter must be greater than zero')
    while len(list_numbers) < x:
        if element % 2 != 0:
            list_numbers.append(element)
        element += 1
    average = sum(list_numbers) / x
    return average


print(average_of_first_x_odd_numbers(3, -20))


# For odd numbers without the 'sum' function:

def average_of_first_x_odd_numbers2(x, start):
    sum_odd2 = 0
    list_numbers2 = []
    element2 = start
    if x <= 0:
        raise ValueError('Numbers count parameter must be greater than zero')
    while len(list_numbers2) < x:
        if element2 % 2 != 0:
            list_numbers2.append(element2)
        element2 += 1
    for elem in list_numbers2:
        sum_odd2 += elem
    return sum_odd2 / x


print(average_of_first_x_odd_numbers2(3, -9))
