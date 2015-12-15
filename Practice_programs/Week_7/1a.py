import re
string='''hill, this is multiline string.
Hi I don't know Java.
java is ubiquitous.'''
s=re.finditer('\shi\s', string, re.M|re.I)
for i in s:
	print(i.group(), i.span())
