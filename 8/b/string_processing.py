import re

__author__ = 'gauth_000'
string = '''1this is a string. is it not a string?
it is nice'''
print('multiple occurances of a word -')
for match in re.finditer(r'\b(\w+)\b(?=.*?\1)', string, flags=re.DOTALL):
    print(match.group(), match.span())
print('consonants -')
match = re.findall(r'[^aeiou ]', string, flags=re.DOTALL)
print(''.join(match))
print('beginning with _ or digit -')
match = re.match(r'_|\d.*?\s', string, flags=re.DOTALL)
print(match)
