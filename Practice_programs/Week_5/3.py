def stars(f):
	def inner(string):
		print('*'*len(string))
		f(string)
		print('*'*len(string))
	return inner

def dollar(f):
	def inner(string):
		print('$'*len(string))
		f(string)
		print('$'*len(string))
	return inner

@dollar
@stars
def display(string):
	print(string)
	
display(input())
