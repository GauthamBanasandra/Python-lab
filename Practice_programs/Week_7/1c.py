import re
strings=['h9i, this_ is multiline string', "_Hi I don't know Java", "9java is ubquitous."]
for string in strings:
	s=re.match('\d.*|_.*', string)
	print(s)
