__author__ = 'gauth_000'
l = eval(input())
print([sum(l[:i + 1]) for i in range(len(l))])
