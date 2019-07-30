liste = [1, 2, 3, 4, 5]
liste_double = [i * 2 for i in liste]
print(liste_double)

# for i in liste:
#     liste_double.append(i * 2)

print('----------------')

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double = [i * 2 for i in liste if i > 0]
print(liste_double)

# for i in liste:
#     if i > 0:
#         liste_double.append(i * 2)

print('----------------')

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double = [i * 2 if i > 0 else i * 3 for i in liste]
print(liste_double)

# for i in liste:
#     if i > 0:
#         liste_double.append(i * 2)
#     else:
#         liste_double.append(i * 3)

print('----------------')

liste_finale = []
for a in range(10):
    for b in range(2):
        liste_finale.append((a, b))
print(liste_finale)
liste = [(a, b) for a in range(10) for b in range(2)]
print(liste)
