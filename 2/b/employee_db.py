import sqlite3
__author__ = 'gauth_000'
with sqlite3.connect(':memory:') as conn:
    cur=conn.cursor()
    cur.executescript('''\
    create table employee
    (
        id integer primary key not null,
        name text,
        age integer,
        salary real,
        deptid integer
    );

    create table dept
    (
        id integer primary key not null,
        name text
    );
    insert into dept values(1, 'CS');
    insert into dept values(2, 'IS');
    insert into dept values(3, 'EC');
    insert into dept values(4, 'TC');
    insert into dept values(5, 'BT');
    insert into dept values(6, 'EE');
    insert into dept values(7, 'ME');
    insert into employee values(12312, 'A', 40, 3244231, 1);
    insert into employee values(123152, 'G', 24, 324423211, 1);
    insert into employee values(342142, 'B', 31, 3254854489, 2);
    insert into employee values(3421242, 'F', 32, 3254854489, 2);
    insert into employee values(4834, 'C', 34, 48848754874, 3);
    insert into employee values(5454, 'D', 57, 87453487, 4);
    insert into employee values(432342, 'E', 67, 87453487, 4);\
    ''')
    print('youngest employee in each dept')
    for row in cur.execute('''  select employee.name, age, dept.name, min(age)
                                from employee, dept
                                where deptid=dept.id
                                group by deptid;'''):
        print(row)
    print('\nnumber of employees in each dept')
    for row in cur.execute('''  select dept.name, count(*)
                                from employee, dept
                                where deptid=dept.id
                                group by dept.id;'''):
        print(row)
    print('\ndept with highest paid employee', cur.execute('''  select dept.name, employee.name, max(salary)
                                                                from employee, dept
                                                                where deptid=dept.id;''').fetchone())