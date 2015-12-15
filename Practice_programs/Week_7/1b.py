import re
string='''hi, this is multiline\tstring. Hi I don't know Java. java is ubquitous.'''
s=re.findall('[^aeiouAEIOU\s]', string)
print(''.join(s))
