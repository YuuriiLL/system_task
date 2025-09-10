import os
import mysql.connector


password = os.environ["MADBY_PASS"]

#print(password)

def open_db():
    return mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='root', password=password, database='system_task',
                                   buffered=True, autocommit=True)

db_connection = open_db()

def get_students():
    query = "SELECT first_name, last_name FROM students"
    cursor = db_connection.cursor()
    cursor.execute(query, multi=True)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def get_student(id):
    query = "SELECT first_name, last_name FROM students WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    row = cursor.fetchone()
    cursor.close()
    return row

def add_student(first_name, last_name, classe_id=1):
    query = "INSERT INTO students (first_name, last_name, classe_id) values (%s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (first_name, last_name, classe_id))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def add_classes(name, room):
    query = "INSERT INTO classes (name, room) values (%s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, room))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id