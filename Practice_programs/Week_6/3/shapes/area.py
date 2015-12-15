def circle(r):
	return 3.14*r*r

def rect(l, b):
	return l*b

def tri(a, b, c):
	s=(a+b+c)/2
	return (s*(s-a)*(s-b)*(s-c))**0.5
