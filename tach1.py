# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:03:04 2024

@author: hp
"""

# Liste des éléments
elements = [8, 4, 6, 1, 5]

# Initialiser le minimum avec le premier élément de la liste
minimum = elements[0]

# Parcourir la liste pour trouver le minimum
for element in elements:
    if element < minimum:
        minimum = element

print("Le plus petit élément de la liste est :", minimum)
# Séquence des acides aminés
sequence = ["A", "R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]

# Initialiser un dictionnaire pour compter les fréquences
frequence = {"A": 0, "R": 0, "W": 0, "G": 0}

# Parcourir la séquence pour compter les occurrences
for acide in sequence:
    if acide in frequence:
        frequence[acide] += 1

print("Fréquence des acides aminés :")
for acide, count in frequence.items():
    print(f"{acide} : {count}")
# Notes de l'étudiant
notes = [14, 9, 13, 15, 12]

# Calculer la note maximum, minimum et la moyenne
note_max = max(notes)
note_min = min(notes)
moyenne = sum(notes) / len(notes)

# Déterminer la mention
if 10 <= moyenne < 12:
    mention = "passable"
elif 12 <= moyenne < 14:
    mention = "assez bien"
elif moyenne >= 14:
    mention = "bien"
else:
    mention = "non admis"

print(f"Note maximum : {note_max}")
print(f"Note minimum : {note_min}")
print(f"Moyenne : {moyenne:.2f}")
print(f"Mention : {mention}")
print("Nombres pairs inférieurs ou égaux à 10 :")
for i in range(21):
    if i <= 10 and i % 2 == 0:
        print(i, end=' ')

print("\nNombres impairs strictement supérieurs à 10 :")
for i in range(21):
    if i > 10 and i % 2 != 0:
        print(i, end=' ')