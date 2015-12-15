string=input()
for i in range(len(string)):
	if string[i]!=string[len(string)-i-1]:
		print('not a palindrome')
		break
else:
	print('palindrome')
