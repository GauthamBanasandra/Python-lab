import re

__author__ = 'gauth_000'
string="Assassins creed is the best game. ABA"
for word in list((re.findall(r'(\b\w*?([a-zA-Z])\w*\2\w*?\b)', w) for w in string.split())):
    print(word)