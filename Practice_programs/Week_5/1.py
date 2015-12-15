import os

f=open('/home/student/1PI13CS060/Lab_6/stateinfo.txt', 'r')
flines=f.readlines()
f.close()
for line in flines:
	print(line)
