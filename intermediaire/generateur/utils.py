def custom_range(n):
    for i in range(1, n + 1):
        yield i


generateur = custom_range(10)
print(next(generateur))


print('-----------------')

from random import randint


def lettre_random(nom):
    nom_liste = list(nom)
    for i in range(len(nom)):
        rand_index = randint(0, len(nom_liste) - 1)
        yield nom_liste.pop(rand_index)


for l in lettre_random('Bonjour'):
    print(l)

nom_shuffle = ''.join([l for l in lettre_random("Bonjour")])
print(nom_shuffle.capitalize())
