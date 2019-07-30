liste = [1, 2, 3, 4, 5]
liste_double = []
for i in liste:
    liste_double.append(i * 2)

liste = liste_double[:]
print(liste)

print('----------------')
# Avec compréhension de liste
liste = [1, 2, 3, 4, 5]
liste = [i * 2 for i in liste]
print(liste)

print('----------------')
liste = [1, 2, 3, 4, 5]
liste = [i * 2 for i in liste if i % 2 == 0]
print(liste)

print('----------------')
liste = [1, 2, 3, 4, 5]
liste = [i * 2 if i % 2 == 0 else i for i in liste]
print(liste)