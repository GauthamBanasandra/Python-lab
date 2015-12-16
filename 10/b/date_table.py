import sqlite3
import math

__author__ = 'gauth_000'
with sqlite3.connect(':memory:') as conn:
    cur=conn.cursor()
    cur.executescript('''
    create table person
    (
        name text,
        dob date
    );''')
    data=[('a', '1234-01-23'), ('b', '1234-01-7')]
    cur.executemany('insert into person values(?, ?)', data)
    for row in cur.execute('select * from person;'):
        print(row[0], int(row[1].split('-')[0])-2015)