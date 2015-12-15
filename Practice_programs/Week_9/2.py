import sqlite3

conn = sqlite3.connect('person.db')
conn.execute("create table if not exists person(name text, age int, area_of_interest text, occupation text);")
conn.execute("insert into person values('A Charma', 54, 'Music', 'Agriculture')")
conn.execute("insert into person values('B Sharma', 45, 'Music', 'Astronaut')")
conn.execute("insert into person values('C Rao', 14, 'Dance', 'Musician')")
conn.execute("insert into person values('Superman Kent', 54, 'Dance', 'Cricket coach')")
conn.execute("insert into person values('Ironman Stark', 54, 'Travel', 'Travel guide')")
conn.commit()
print('people having Sharma as their last name:',
      ', '.join([row[0] for row in conn.execute('select * from person') if row[0].split()[1] == 'Sharma']))
print('most common area of interest:',
      sorted(conn.execute("select area_of_interest, count(*) from person group by area_of_interest"),
             key=lambda x: x[1], reverse=True)[0][0])
conn.execute("delete from person where area_of_interest not in ('Music', 'Dance', 'Sports', 'Travel')")
for row in conn.execute('select * from person'):
    print(row)
conn.execute('drop table person')
conn.commit()
conn.close()
