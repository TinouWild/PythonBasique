# Fonction enumerate
# liste = ['Bonjour', 'tout', 'le', 'monde']
# for i in range(len(liste)):
#     if i > 0:
#         print(liste[i])

liste = ['Bonjour', 'tout', 'le', 'monde']
for i, mot in enumerate(liste, 1):
    print(i)
    print(mot)

print('---------------')

# Fonction enumerate sur dictionnaire
dic = {
    'Utilisateur1': 'John',
    'Utilisateur2': 'Peter',
    'Utilisateur3': 'Julie'
}

for i, (cle, valeur) in enumerate(dic.items()):
    print(i, cle, valeur)

print('---------------')
