# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:22:15 2024

@author: hp
"""

semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

jours_ouvrables = semaine[:5]
weekend = semaine[5:]
print(jours_ouvrables)  # Output: ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
print(weekend)  # Output: ['samedi', 'dimanche']

jours_ouvrables = semaine[:-2]
weekend = semaine[-2:]
print(jours_ouvrables)  # Output: ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
print(weekend)  # Output: ['samedi', 'dimanche']

semaine_inverse = semaine[::-1]
print(semaine_inverse)  # Output: ['dimanche', 'samedi', 'vendredi', 'jeudi', 'mercredi', 'mardi', 'lundi']

hiver = ["décembre", "janvier", "février"]
printemps = ["mars", "avril", "mai"]
ete = ["juin", "juillet", "août"]
automne = ["septembre", "octobre", "novembre"]

saisons = [hiver, printemps, ete, automne]

print(saisons[2])  # Output: ['juin', 'juillet', 'août']
print(saisons[1][0])  # Output: 'mars'
print(saisons[1:2])  # Output: [['mars', 'avril', 'mai']]
print(saisons[:][1])  # Output: ['mars', 'avril', 'mai']

nombres_pairs = len([x for x in range(2, 10001) if x % 2 == 0])
print(nombres_pairs)  # Output: 5000