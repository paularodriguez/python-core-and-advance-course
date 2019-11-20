# Install connector using PyCharm
# PyCharm -> Preferences -> Project <name> -> Project Interpreter -> + Button -> Search 'mysql-connector-python' -> Install

import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='')

if conn.is_connected():
    print("Connected to mysql db")

# We need a cursor to do operations
cursor = conn.cursor()

try:
    cursor.execute("Insert into emp values(4, 'Paula', 10000)")
    conn.commit()
    print("Employee added")
except:
    conn.rollback()

cursor.close()
conn.close()