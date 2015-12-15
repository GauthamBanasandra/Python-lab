import sqlite3
__author__ = 'gauth_000'
conn=sqlite3.connect(':memory:')
curr=conn.cursor()
curr.execute('create table if not exists person(name text, age int);')
curr.execute('insert into person values ("a", 5);')
curr.executemany('insert into person values (?, ?)', ((chr(i), i) for i in range(97, 123)))
curr.execute('select * from person;')
for row in curr.fetchall():
    print(row)
conn.close()