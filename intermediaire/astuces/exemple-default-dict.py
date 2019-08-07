from collections import defaultdict

# Retourne une erreur car la clé n'existe pas
# mot = 'anticonstitutionnellement'
#
# d = {}
# for lettre in mot:
#     d[lettre] += 1
#
# print(d.items())

# Fonctionne mais nécessite une structure conditionnelle
mot = 'anticonstitutionnellement'

d = {}
for lettre in mot:
    if not d.get(lettre):
        d[lettre] = 1
    else:
        d[lettre] += 1

print(d.items())

# Code allégé grâce au defaultdict()
mot = 'anticonstitutionnellement'

d = defaultdict(dict)
for lettre in mot:
    d[lettre] = 1

print(d.items())
