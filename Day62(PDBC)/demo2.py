# To check how many databases are present in mysql server

import mysql.connector

v1 = mysql.connector.connect(user='root',password='root',host='localhost')

# Cursor(): cursor as an a object basically communicate an entire mysql db server on your own database

v2 = v1.cursor()

# Use the execute() method
# The execute() methods run the SQL query and returns the result.

v2.execute('show databases')
print(v2)
# CMySQLCursor: show databases

for i in v2:
    print(i)

# ('cap',)
# ('car',)
# ('emp',)
# ('information_schema',)
# ('mango',)
# ('myschema',)
# ('mysql',)
# ('pen',)
# ('performance_schema',)
# ('product',)
# ('sys',)
