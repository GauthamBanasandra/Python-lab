import re
__author__ = 'gauth_000'
with open('re.txt') as file:
    functions=re.findall(r'FUNCTIONS.*DATA', file.read(), flags=re.DOTALL)
    functions=re.findall(r'(\w+)\(.*?\)', functions[0], flags=re.DOTALL)
    print('\n'.join(functions))