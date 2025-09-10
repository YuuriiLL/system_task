import os
import mysql.connector

password = os.environ["MADBY_PASS"]

print(password)

def open_db():
    return mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='root', password=password, database='system_task',
                                   buffered=True, autocommit=True)


