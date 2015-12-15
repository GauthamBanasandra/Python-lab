vowels=0
cons=0
for char in input():
	if char.isalpha():
		if char in ['a', 'e', 'i', 'o', 'u']:
			vowels+=1
		else:
			cons+=1
print('vowels='+str(vowels), 'consonants='+str(cons))
