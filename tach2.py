# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:07:15 2024

@author: hp
"""

print("Table de multiplication par 9 :")
for i in range(1, 11):
    print(f"9 x {i} = {9 * i}")
    
# Liste des éléments
animaux = ["vache", "souris", "levure", "bacterie"]

# Avec une boucle for (méthode 1)
print("Méthode 1 avec for :")
for animal in animaux:
    print(animal)

# Avec une boucle for (méthode 2)
print("\nMéthode 2 avec for (avec index) :")
for i in range(len(animaux)):
    print(animaux[i])

# Avec une boucle while
print("\nMéthode avec while :")
i = 0
while i < len(animaux):
    print(animaux[i])
    i += 1

# Liste des jours de la semaine
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

# Afficher les jours de la semaine avec une boucle for
print("Jours de la semaine :")
for jour in semaine:
    print(jour)

# Afficher les jours du week-end avec une boucle while
print("\nJours du week-end :")
i = 5
while i < len(semaine):
    print(semaine[i])
    i += 1
    
# Liste des nombres impairs
impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# Créer une liste des nombres pairs
pairs = [x + 1 for x in impairs]

print("Liste des nombres pairs :", pairs)

# Notes de l'étudiant
notes = [14, 9, 6, 8, 12]

# Calculer la moyenne
moyenne = sum(notes) / len(notes)

# Afficher la moyenne avec deux décimales
print(f"Moyenne : {moyenne:.2f}")

# Créer la liste des entiers pairs de 2 à 20 inclus
entiers = list(range(2, 21, 2))

# Calculer le produit des nombres consécutifs deux à deux
print("Produit des nombres consécutifs deux à deux :")
for i in range(len(entiers) - 1):
    produit = entiers[i] * entiers[i + 1]
    print(f"{entiers[i]} x {entiers[i + 1]} = {produit}")
    
print("Triangle :")
for i in range(1, 11):
    print('*' * i)
    
print("Triangle inversé :")
for i in range(10, 0, -1):
    print('*' * i)
    
print("Triangle gauche :")
for i in range(1, 11):
    print(' ' * (10 - i) + '*' * i)