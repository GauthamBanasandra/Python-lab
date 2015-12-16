__author__ = 'gauth_000'


def next_prime(a, b):
    while a <= b:
        if is_prime(a):
            yield a
        a += 1


def is_prime(num):
    for i in range(2, num):
        if not num % i:
            return False
    return True


primes = next_prime(2, 10)
print(list(primes))
