import math

__author__ = 'gauth_000'


def generate_prime(n):
    for i in range(2, n):
        if is_prime(i):
            yield i


def is_prime(n):
    for i in range(2, math.floor(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(list(generate_prime(20)))
