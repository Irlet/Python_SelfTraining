def return_prime_numbers_less_than_100():
    """Returns a list containing prime numbers that are less than 100"""

    numbers = list(range(2, 100))
    prime_numbers = list(range(2, 100))
    for number in numbers:
        for element in range(2, number):
            if number % element == 0 and number in prime_numbers:
                prime_numbers.remove(number)

    return prime_numbers


print(return_prime_numbers_less_than_100())
