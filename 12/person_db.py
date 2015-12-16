import sqlite3
__author__ = 'gauth_000'
with sqlite3.connect('person.db', isolation_level=None) as conn:
    cur=conn.cursor()
    cur.executescript('''
    create table person
    (
        name text,
        age integer,
        interest text,
        occupation text
    );
    insert into person values('a', 2, 'dance', 'dance');
    insert into person values('b', 2, 'dancing', 'dance');
    insert into person values('c', 2, 'music', 'dance');
    insert into person values('d', 2, 'travel', 'dance');
    insert into person values('e', 2, 'dance', 'dance');''')
    cur.execute("delete from person where interest not in ('dance', 'music', 'travel');")
    for row in cur.execute('select * from person;'):
        print(row)