# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:20:08 2024

@author: hp
"""

liste = ['chien', 'chat', 1, 2 , 3, 'girafe']
#Fonction .insert()
liste.insert(0, 'souris')
print(liste)
liste.insert(7, 'leopard')
print(liste)
liste.insert(8, 3)
print(liste)
liste.insert(9, ['mouton', 'chèvre'])
print(liste)
liste.insert(10,3.4)
print(liste)

# Fonction del 
del liste[-1]
print(liste)

#del liste

print(liste)

# Fonction pop 
liste.pop(2)

print(liste)

liste.pop(4)
print(liste)

#Fonction .sort()
liste2 = [1, 3, 4, 5, -2, 2.5 , 4]

liste2.sort()

print(liste2)
# Fonction .sort() avec reverse = True
liste2.sort(reverse = True)
print(liste2)

liste3 = ['lun', 'mar', 'mer', 'jeu', 'ven']

liste3.sort()

print(liste3)

liste3.sort(reverse = True)
print(liste3)

# Fonction sorted()
print(sorted(liste2))
print(liste2)
liste2 = sorted(liste2)
print( liste2)


# Fonction sorted avec reverse = True 
liste2  = sorted(liste2, reverse = True)
print(liste2)

# Fonction .count()
liste4 = [1,1,3,3,1,3,4,5]
print(liste4.count(1))
print(liste4.count(3))

# Fonction .join()
liste5 = ['Ale', 'est','de', 'plus','en', 'plus', 'bizarre']
' '.join(liste5)
liste6 = ['Good' , 'morning', 'everyone' ,'!']
'__'.join(liste6)

# Fonction .extend()
liste3.extend(['sam' ,'dim'])
print(liste3)

# Fonction .index()
liste3.index('dim')
# Foncton .clear()
liste3.clear()


# Fonction .copy()

liste7 = liste5.copy()
print(liste7)