f=open('/home/student/1PI13CS060/Lab_6/words.txt', 'r')
fwords=f.read().strip().split()
print(fwords)
f.close()
fdict={}
wdict={}
for word in fwords:
	if word[0] in fdict:
		fdict[word[0]]+=1
	else:
		fdict[word[0]]=1
for word in fwords:
	if word[0] in wdict:
		wdict[word[0]].append(word)
	else:
		wdict[word[0]]=[word]
f=open('/home/student/1PI13CS060/Lab_6/words_output.txt', 'w')
for k, v in sorted(fdict.items()):
	f.write(str(k)+' '+str(v)+' ['+', '.join(wdict[k])+']\n')
f.close()
