# Install connector using PyCharm
# PyCharm -> Preferences -> Project <name> -> Project Interpreter -> + Button -> Search 'mysql-connector-python' -> Install

import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='')

if conn.is_connected():
    print("Connected to mysql db")