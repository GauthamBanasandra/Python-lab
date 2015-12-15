import re

__author__ = 'gauth_000'
f=open('re.doc', 'r')
lines=f.read().replace('\n', '')
f.close()
lines=re.search(r'FUNCTIONS.*DATA', lines).group()
functions=re.findall(r'(\w+)\(.*?\)', lines)
for function in functions:
    print(function)