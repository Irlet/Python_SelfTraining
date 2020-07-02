def return_prime_numbers_less_than_(max_num):
    """Returns a list containing prime numbers that are less than max_num"""

    numbers = list(range(2, max_num))
    prime_numbers = list(range(2, max_num))
    for number in numbers:
        for element in range(2, int((number/2)+1)):
            if number % element == 0:
                prime_numbers.remove(number)
                break
    return prime_numbers


print(return_prime_numbers_less_than_(113))
