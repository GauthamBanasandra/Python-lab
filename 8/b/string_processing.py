import re
__author__ = 'gauth_000'
string='1This is 1multiline string. It has many many lines. Well, many many is not too many. It is just 4lines.'
# for match in re.findall(r'\b(\w+)\b.*?\1', string):
#     print(match)
match=re.findall(r'[^aeiou ]', string)
print(''.join(match))
match=re.match(r'_|\d.*', string)
print(match)