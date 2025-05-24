import mysql.connector

# Create a table in DB Phone

v1 = mysql.connector.connect(user='root',password='root',host='localhost',database='Phone')

v2 = v1.cursor()

# To create Table
# Cmysql : create table Table_Name(col1 datatype, col2 datatype ,...........)

# v2.execute('create table student(Slno int, FName varchar(20), Age int, Address varchar(30))' )
# print('Created',v2)

# Created CMySQLCursor: create table student(Slno int, FName var..

v2.execute('desc student')
for i in v2:
    print(i)

# ('Slno', 'int', 'YES', '', None, '')
# ('FName', 'varchar(20)', 'YES', '', None, '')
# ('Age', 'int', 'YES', '', None, '')
# ('Address', 'varchar(30)', 'YES', '', None, '')

# Index	Field Name	Meaning
# 0	Field	Column name (e.g., 'Fname')
# 1	Type	Data type (e.g., b'varchar(30)')
# 2	Null	Whether NULL values are allowed ('YES' or 'NO')
# 3	Key	    Key type ('PRI' for primary, 'MUL' for index, etc.)
# 4	Default	Default value (e.g., None means no default)
# 5	Extra	Extra info (e.g., 'auto_increment')

