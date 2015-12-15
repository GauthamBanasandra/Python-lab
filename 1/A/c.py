from functools import reduce

__author__ = 'gauth_000'
numbers=list(range(5))
print(reduce(lambda x, y:x if x>y else y, numbers))