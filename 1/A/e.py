from functools import reduce
import random

__author__ = 'gauth_000'
integers = [random.randint(0, 200) for i in range(5)]
print(integers, reduce(lambda x, y: '' + x + y, map(str, integers)), sep='\n')