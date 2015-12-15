text=str(input()).strip().split()
for i in range(len(text)):
	text[i]=text[i][0].upper()+text[i][1:]
print(''.join(text))
