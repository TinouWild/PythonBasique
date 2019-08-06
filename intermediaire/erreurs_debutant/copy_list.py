# liste = [1, 2, 3]
# liste_copie = liste
#
# liste.append(5)
#
# print(liste)
# print(liste_copie)
#
# print(id(liste))
# print(id(liste_copie))

# bonne pratique
liste = [1, 2, 3]
liste_copie = liste[:]
liste_copie = list(liste)
liste_copie = liste.copy()

liste.append(5)

print(liste)
print(liste_copie)

print(id(liste))
print(id(liste_copie))