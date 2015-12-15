class Fib:
	def __init__(self, n):
		self.n=n
		self.i=-1
		self.j=0
		self.k=1
		
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.j<=self.n:
			self.i=self.j
			self.j=self.k
			self.k=self.i+self.j		
		else:
			raise StopIteration
		return self.i

for i in Fib(30):
	print(i)
