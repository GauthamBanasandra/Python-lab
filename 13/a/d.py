__author__ = 'gauth_000'
print([i for i in filter(lambda x: x ** .5 == int(x ** .5), range(1, 1000)) if sum(list(map(int, str(i)))) < 10])
