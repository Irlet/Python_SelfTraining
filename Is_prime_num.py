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
