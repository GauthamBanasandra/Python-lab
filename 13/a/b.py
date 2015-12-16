import re

__author__ = 'gauth_000'
string='''do you think this is the longest string?
perhaps this one?
or this?
i don't know.'''
print(list(filter(lambda x:x, (re.search(r'(.).*\1', word) for word in string.split()))))