# for example for n=4, 4!=1*2*3*4


def factorial(n):
    product = 1
    if n < 0:
        raise ValueError("Number cannot be negative")
    if n == 0:
        return 1

    for element in range(1, (n+1)):
        product = product*element
    return product


print(factorial(5))
print(factorial(3))
