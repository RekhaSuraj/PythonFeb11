import mysql.connector
# UPDATE
v1 = mysql.connector.connect(user='root',password='root',host='localhost',database='Phone')

v2 = v1.cursor()

# update a record in the table student
# syntax: update Table_Name set column_name = new_value where column_name = old_value(unique identifier)

v2.execute('update student set Address = "Hospet" where Slno = 12')
v1.commit()

# READ
v2.execute('select * from student')
print(v2.fetchall())

# [(1, 'Aparna', 20, 'BTM-Bangalore'), (12, 'Praveen', 25, 'Hospet'), (13, 'Ramesh', 26, 'London')]