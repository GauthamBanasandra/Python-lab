import re

__author__ = 'gauth_000'
with open('input.txt') as file:
    content = file.read()
    content = re.sub(r'( )(\1+)', r' ', content)
    content = re.sub(r'([.?!])\s*([a-z])', lambda x: x.group(1) + ' ' + x.group(2).capitalize(),
                     content[0].capitalize() + content[1:])
    content = re.sub(r'\b(\w+)\b \1', r'\1', content)
    print(content)
