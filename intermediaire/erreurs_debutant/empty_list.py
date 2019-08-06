import random


# def generateur_liste(liste=[]):
#     liste.extend([random.randint(1, 100) for i in range(5)])
#     return liste
#
#
# for i in range(5):
#     print(generateur_liste())


def generateur_liste(liste=None):
    if liste is None:
        liste = []
    liste.extend([random.randint(1, 100) for i in range(5)])
    return liste


for i in range(5):
    print(generateur_liste())
