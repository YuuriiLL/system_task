def get_students():
    query = "SELECT first_name, last_name FROM students"
    cursor = db_connection.cursor()
    cursor.execute(query, multi=True)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def get_students(id):
    query = "SELECT first_name, last_name FROM students WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    row = cursor.fetchone()
    cursor.close()
    return row

def add_students(first_name, last_name, classe_id=1):
    query = "INSERT INTO residents (first_name, last_name, classe_id) values (%s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (first_name, last_name, classe_id))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id