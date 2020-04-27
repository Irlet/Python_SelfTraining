
def multiplication_of_first_x_even_numbers(x, start=0):

    even_numbers = []
    if start == 0:
        element = start + 1
    else:
        element = start
    multiplicated = 1
    if x <= 0:
        raise ValueError('Enter positive number of elements')
    while len(even_numbers) < x:
        if element % 2 == 0:
            even_numbers.append(element)
        element += 1
    for elem in even_numbers:
        multiplicated *= elem
    return multiplicated


print(multiplication_of_first_x_even_numbers(4, start=0))
print(multiplication_of_first_x_even_numbers(3, 20))
print(multiplication_of_first_x_even_numbers(5, -10))
