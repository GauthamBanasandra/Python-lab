import os

f=open('/home/student/1PI13CS060/Lab_6/sample_etc_passwd.txt', 'r')
flines=[line.strip() for line in f.readlines()]
f.close()
bin_shell=0
for line in flines:
	if line.split(':')[-1]=='/bin/bash':
		bin_shell+=1
print('No. of entries=', len(flines))
print('No. of /bin/bash users=', bin_shell)
