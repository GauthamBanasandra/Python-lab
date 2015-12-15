from math import factorial as fact

__author__ = 'gauth_000'
rows = 5
for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    for j in range(i + 1):
        print(int(fact(i) / (fact(j) * fact(i - j))), end=' ')
    print()
