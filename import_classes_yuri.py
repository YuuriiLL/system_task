#import database
import csv

from database import *

# Lire le fichier classes.csv
# Pour chaque ligne, il faut insére avec add_student(,,)

"""
with open('csv_fichier/classes.csv', newline='') as csv_classes:
    lire_fichier = csv.reader(csv_classes, delimiter=';')

    for row in lire_fichier:
        print(row)
"""


with open('csv_fichier/classes.csv') as csv_classes:
    next(csv_classes)
    for line in csv_classes:
        parts = line.split(";")
        try:
            add_class(parts[0], parts[1].strip())
        except mysql.connector.errors.IntegrityError as error:
            if error.errno == 1062:
                print("Doublon de la classe "+parts[0]+" insertion ignorée")
            else:
                raise
