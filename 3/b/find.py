import re

__author__ = 'gauth_000'
with open('input.txt') as file:
    a = []
    b = []
    c = []
    d = []
    e = []
    for line in file.readlines():
        match = re.search(r'\d{2,3}-\d{4,4}0{4,4}', line)
        a.append(match.group()) if match else None
        match = re.search(r'([a-zA-Z]+) \d{3,3}-\d{8,8}', line)
        b.append(match.group(1)) if match else None
        match = re.search(r'([a-zA-Z]+).*\w+@gmail.com', line)
        c.append(match.group(1)) if match else None
        match = re.match(r'(?:[GE]\w*|\w*y).* (\w+)@\w+\.com', line)
        d.append(match.group(1)) if match else None
        match = re.search(r'(\w+) (?:\d{,1}|\d{4,})-(?:\d{,7}|\d{9,})', line)
        e.append(match.group(1)) if match else None
    print('4 0s in end:', ', '.join(a))
    print('3 digit area code:', ', '.join(b))
    print('gmail id:', ', '.join(c))
    print('usernames for G/E|.*y:', ', '.join(d))
    print('improper phone number:', ', '.join(e))
