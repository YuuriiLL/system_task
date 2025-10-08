import mysql.connector
import os

"""
def open_db():
    return mysql.connector.connect(host=os.getenv('DB_HOST', '127.0.0.1'), port=os.getenv('DB_PORT', '3306'),
                                   user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database=os.getenv('DB_DATABASE'),
                                   buffered=True, autocommit=True)

"""
def open_db():
    return mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='root', password=os.getenv('MADBY_PASS'), database='system_task',
                                   buffered=True, autocommit=True)

db_connection = open_db()

def get_class_id_from_name(name):
    query = "SELECT id FROM classes WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (name,))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]

def add_class(name, room):
    query = "INSERT INTO classes (name, room) values (%s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, room))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def add_student(first_name, last_name, class_id):
    query = "INSERT INTO students (first_name, last_name, class_id) values (%s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (first_name, last_name, class_id))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def get_student(id):
    query = "SELECT first_name, last_name FROM students WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    row = cursor.fetchone()
    cursor.close()
    return row

def delete_students(db_connection, name):
    query = "DELETE FROM students WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (name,))
    db_connection.commit()
    cursor.close()