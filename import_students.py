from database import *

"""
with open("csv_fichier/students.csv", encoding='latin-1') as file:
    next(file)
    for line in file:
        row = line.strip().split(";")
        class_id = get_class_id_from_name(row[3])
        try:
            if class_id:
                add_student(row[0], row[1], class_id)
            else:
                print(f"La classe {row[3]} n'existe pas pour la ligne: {row}")
        except mysql.connector.errors.IntegrityError as error:
            if error.errno == 1062:
                raise
"""





with open("csv_fichier/students.csv",encoding='latin-1') as file:
    next(file)
    for line in file:
        parts = line.strip().split(";")
        class_id = get_class_id_from_name(parts[3])
        try:
            add_student(parts[0], parts[1], class_id)
        except mysql.connector.errors.IntegrityError as error:
            if error.errno == 1062:
                print("Doublon de l'élève "+parts[0]+" insertion ignorée")
            else:
                raise

