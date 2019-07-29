# Objet muable (modifiable, l'id ne change pas ( liste, dictionnaire, set))
liste = [1, 2, 3]
print(id(liste))
liste.append(4)
print(id(liste))

print('---------------')

# Objet immuable (int, float, boolean, tupple, string)
prenom = 'Pierre'
print(id(prenom))
prenom += ' Dupont'
print(id(prenom))

print('---------------')

## module TIME permet de checker les performances du script