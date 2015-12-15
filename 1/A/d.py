__author__ = 'gauth_000'
tuples=[(i, j) for i in range(1, 5) for j in range(1, 7)]
print(list(filter(lambda x:not x[0]%x[1], tuples)))