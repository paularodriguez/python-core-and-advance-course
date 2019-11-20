# Install connector using PyCharm
# PyCharm -> Preferences -> Project <name> -> Project Interpreter -> + Button -> Search 'mysql-connector-python' -> Install

import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='')

if conn.is_connected():
    print("Connected to mysql db")

# We need a cursor to do operations
cursor = conn.cursor()

cursor.execute("Select * from emp")

# Get first and iterate through the others
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
conn.close()