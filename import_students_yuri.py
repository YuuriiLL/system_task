from xml.sax import parse

from database import *
import csv


# Lire le fichier classes.csv
# Pour chaque ligne, il faut insére avec add_student(,,)


with open('csv_fichier/students.csv') as csv_students:
    next(csv_students)
    for line in csv_students:
        parts = line.split(";")
        add_student(parts[0], parts[1], parts[2], parts[3].strip())
    #lire_fichier = csv.reader(csv_students, delimiter=';')






#add_student()