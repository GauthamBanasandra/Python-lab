__author__ = 'gauth_000'
string='''do you think this is the longest string?
perhaps this one?
or this?
i don't know.'''
print(sorted(list(i for i in string.split()), key=len, reverse=True)[:2])