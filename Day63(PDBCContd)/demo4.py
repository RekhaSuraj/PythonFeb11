import mysql.connector

v1 = mysql.connector.connect(user='root',password='root',host='localhost',database='Phone')

v2 = v1.cursor()

# Delete a record
# Syntax: delete from student where column_name = value(unique identifier)

v2.execute('delete from student where Slno = 13')
v1.commit()

v2.execute('select * from student')
print(v2.fetchall())

# [(1, 'Aparna', 20, 'BTM-Bangalore'), (12, 'Praveen', 25, 'Hospet')]
