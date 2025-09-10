#import database
import csv

from database import add_classes

# Lire le fichier classes.csv
# Pour chaque ligne, il faut insére avec add_student(,,)

"""
with open('csv_fichier/classes.csv', newline='') as csv_classes:
    lire_fichier = csv.reader(csv_classes, delimiter=';')

    for row in lire_fichier:
        print(row)

"""



add_classes("SI-C2b", "C-313")