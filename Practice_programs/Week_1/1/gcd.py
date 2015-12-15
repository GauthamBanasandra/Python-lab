a=eval(input())
b=eval(input())
if a>b:
	min=b
else:
	min=a
gcd=1
for i in range(2, min+1):
	if a%i==0 and b%i==0:
		gcd=i
print(gcd)
