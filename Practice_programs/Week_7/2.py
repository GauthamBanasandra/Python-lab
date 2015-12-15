import re

__author__ = 'gauth_000'
f = open('C:/Users/gauth_000/OneDrive/Documents/Programs/Python/Python_Lab/Week_7/input2.txt', 'r')
lines = f.read()
f.close()
print('a)4 zeros in the end :', re.findall(r'\d+-\d+0000', lines))
print('b)names having 3-digit area code :', re.findall(r'([a-zA-Z]+)\s*\d\d\d-\d{8,8}', lines))
print('c)no. of people having gmail id :', len(re.findall(r'.*@gmail\.com', lines)))
print('d)user names with name starting with G or E and ending with y :',
      re.findall(r'^[GE]\w*y\s+\d+-\d+\s+(\w+)@gmail\.com', lines, flags=re.M))
print('e)improper phone number format :', re.findall(r'([a-zA-Z]+)\s*(?:\d|\d{4,})-\d*', lines))