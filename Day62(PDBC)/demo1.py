# PDBC:

# PDBC --> Python DataBase Connection
# How to connect MySQL database in Python
# Let’s see how to connect the MySQL database in Python using the ‘MySQL Connector Python’ module.
#
# Arguments required to connect
# You need to know the following detail of the MySQL server to perform the connection from Python.
#
# Argument	Description
# Username	The username that you use to work with MySQL Server. The default username for the MySQL database is a root.
# Password	Password is given by the user at the time of installing the MySQL server.
# If you are using root then you won’t need the password.
# Host name	The server name or Ip address on which MySQL is running.
# if you are running on localhost, then you can use localhost or its IP 127.0.0.0
# Database name	The name of the database to which you want to connect and perform the operations.

import mysql.connector

v1 = mysql.connector.connect(user='root',password='root',host='localhost')
print(v1)

# <mysql.connector.connection_cext.CMySQLConnection object at 0x00000237603A72F0>
if v1:
    print('Connected')
else:
    print('Not Connected')


# Connected
