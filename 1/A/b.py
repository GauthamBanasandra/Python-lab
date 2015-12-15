__author__ = 'gauth_000'
strings="this is a 1line string".split()
print(' '.join(filter(lambda x:x[0].isalpha(), strings)))