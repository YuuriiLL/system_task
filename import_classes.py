def add_classes(name, room):
    query = "INSERT INTO residents (name, room) values (%s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, room))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id