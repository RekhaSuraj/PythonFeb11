# CRUD = C = Create
#        R = Read
       # U = Update
       # D = Delete

# TO create Database
# syntax: Mysql : create database Database_Name;

import mysql.connector
v1 = mysql.connector.connect(user='root',password='root',host='localhost')

v2 = v1.cursor()

# v2.execute('create database Phone')
# print('Created',v2)
# Created CMySQLCursor: create database Phone

v2.execute('show databases')

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
# ('phone',)
# ('product',)
# ('sys',)

