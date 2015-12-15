text=str(input()).strip().split()
for i in range(len(text)):
	if text[i][0].isalpha():
		temp=''
		for ch in text[i]:
			if ch!='z':
				temp+=chr(ord(ch)+1)
			else:
				temp+='a'
		text[i]=temp
	elif text[i][0].isdigit():
		text[i]=text[i][::-1]
	elif text[i][0]=='$':
		set1=list(text[i][::2])
		temp='z'+text[i]
		set2=list(temp[::2])[1:]
		temp=''
		for j in range(len(set2)):
			temp+=set2[j]+set1[j]
		if len(set1)!=len(set2):
			temp+=set1[-1]
		text[i]=temp
print(' '.join(text))
