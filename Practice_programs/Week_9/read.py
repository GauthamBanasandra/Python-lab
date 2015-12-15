import sqlite3
name='employee'
table='department'
conn=sqlite3.connect(name+'.db')
cur=conn.cursor()
rows=cur.execute('select * from '+table)
for row in rows:
	print(row)
conn.execute('drop table '+table)
conn.commit()
conn.close()
