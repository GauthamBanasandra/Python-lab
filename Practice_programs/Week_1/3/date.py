date=str(input()).strip().split('/')
for i in range(len(date)):
	date[i]=int(date[i])
month={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
leap=False
if (date[2]%4==0 and date[2]%100!=0) or (date[2]%4!=0 and date[2]%100==0) or date[2]%400==0:
	leap=True
if not leap:
	if date[0]>month[date[1]]:
		print('Invalid')
	else:
		print('Valid')
if leap:
	if date[1]==2:
		if date[0]>29:
			print('Invalid')
		else:
			print('Valid')
	else:
		if date[0]>month[date[1]]:
			print('Invalid')
		else:
			print('Valid')
