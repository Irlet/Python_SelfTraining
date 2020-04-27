# write a given number from fibonacci numbers:

# 1st option:


def Fib(number):
    if number < 1:
        raise ValueError("Number must be positive")
    if number == 1:
        return 1
    if number == 2:
        return 1
    else:
        return Fib(number-1) + Fib(number-2)


print(Fib(6))

# 2nd option (faster):


def Fib2(number):
    fib_list = [1, 1]
    if number < 1:
        raise ValueError("Number must be positive")
    for i in range(2, number):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list[number-1]


print(Fib2(40))


# Write the first 'n' Fibonacci numbers:


def first_n_fiblist(n):
    fib_list = [0, 1]
    if n < 1:
        raise ValueError("Number must be positive")
    if n == 1:
        fib_list = [0]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list


print(first_n_fiblist(30))
