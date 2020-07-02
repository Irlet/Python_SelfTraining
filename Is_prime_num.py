''' is the number a prime number?'''


def is_prime(n):
    if n < 2:
        return False
    a = 2
    while a*a <= n:
        if n % a == 0:
            return False
        a += 1
    return True


print(is_prime(19))


# Another, easier way:

def is_prime2(n):
    if n < 2:
        return False
    for number in range(2, n):
        if n % number == 0:
            return False
    return True


print(is_prime2(122))
print(is_prime2(11))

# Another, faster & professional way:


def is_prime_number(num):
    if not isinstance(num, int) or num < 2:
        return False
    for number in range(2, int((num/2)+1)):
        if num % number == 0:
            return False
    return True


print(is_prime_number(3.5))
print(is_prime_number(0))
print(is_prime_number(-2))
print(is_prime_number(97))
print(is_prime_number(113))
print(is_prime_number("g"))