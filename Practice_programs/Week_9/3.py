import sqlite3

conn = sqlite3.connect('employee.db')


def display(table):
    for row in conn.execute('select * from ' + table):
        print(row)


conn.execute("create table if not exists department(id int primary key, name text);")
conn.execute(
    "create table if not exists employee(id int primary key, name text, age int, salary real, deptid int references department);")
conn.execute("insert into department values(1, 'CS')")
conn.execute("insert into department values(2, 'IS')")
conn.execute("insert into department values(3, 'EC')")
conn.execute("insert into department values(4, 'EE')")
# display('department')
conn.execute("insert into employee values(11, 'A', 55, 550000, 1)")
conn.execute("insert into employee values(12, 'B', 65, 6550000, 2)")
conn.execute("insert into employee values(13, 'C', 75, 7550000, 3)")
conn.execute("insert into employee values(14, 'D', 55, 50000, 1)")
conn.execute("insert into employee values(15, 'AB', 75, 52131200, 2)")
# display('employee')

print('youngest in each dept:')
for row in conn.execute("select *, min(age) from employee group by deptid order by age"):
    print(row)
print('employees in dept:')
for row in conn.execute(
        "select department.name as dname, count(*) from employee, department where employee.deptid=department.id group by dname"):
    print(row)
print('highest paid employee:', list(conn.execute(
    "select employee.name, department.name from employee, department where department.id=employee.deptid order by employee.salary desc"))[
    0])
conn.execute('drop table department')
conn.execute('drop table employee')
conn.commit()
conn.close()
