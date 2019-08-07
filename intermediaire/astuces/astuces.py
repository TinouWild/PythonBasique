import os
from pprint import pprint

# Trouver le chemin d'un module
print("Trouver le chemin d'un module :")
print(os.__file__)
print(__file__)
dossier_courant = os.path.dirname(__file__)
print(dossier_courant)

print("=" * 100)

# La fonction join
print("Utiliser la fonction join")
tags_photo = ['vacances', 'italie', 'juin', '2018']
nom_fichier = tags_photo[0] + '_' + tags_photo[1] + '_' + tags_photo[2] + '_' + tags_photo[3]
nom_fichier = '{}_{}_{}_{}'.format(tags_photo[0], tags_photo[1], tags_photo[2], tags_photo[3])
nom_fichier = '{}_{}_{}_{}'.format(*tags_photo)
print(nom_fichier)
# Avec join
nom_fichier = '_'.join(tags_photo)
print(nom_fichier)

print("=" * 100)

# Chainer les comparateurs
print("Chaîner les comparateurs")
nombre = 25
if 1 < nombre < 50:
    print('Le nombre est compris entre 1 et 50.')

print("=" * 100)

# .For Else
print(".For Else")
invites = ['Julien', 'Marie', 'Pierre', 'Pascal']
for invite in invites:
    if invite == 'Pascal':
        print('Pascal a deja ete invite !')
        break
else:
    print("Pascal n'a pas ete invite :(")

print("=" * 100)

# Inverser les clés et valeurs d'un dictionnaire
print("Inverser les clés et valeurs d'un dictionnaire")
LONG_NAMES = {
    'anm_scn': 'Animation Scene',
    'anm_out': 'Animation Publish',
    'sim_scn': 'Simulation Scene',
    'sim_out': 'Simulation Publish'
}

pprint(list(zip(LONG_NAMES.values(), LONG_NAMES.keys())))
SHORT_NAMES = dict(zip(LONG_NAMES.values(), LONG_NAMES.keys()))

print(LONG_NAMES.get('anm_scn'))
print(SHORT_NAMES.get('Animation Scene'))

print("=" * 100)

# Aplatir une liste et enlever les doublons
print("Aplatir une liste et enlever les doublons")
ma_liste = [[1, 7, 3], [3, 4], [12, 1, 4, 8], [1, 3, 3]]
ma_liste_aplatie = sum(ma_liste, [])
print(ma_liste_aplatie)
ma_liste_sans_doublons = sorted(list(set(ma_liste_aplatie)))
print(ma_liste_sans_doublons)

print("=" * 100)

# Enlever certains éléments d'une liste
print("Enlever certains éléments d'une liste")
prenom = 'Pierre'
nom = 'Dupont'
id_membre = '142352'

liste = [id_membre, nom, prenom]
nom_complet = '_'.join(liste)
print(nom_complet)

prenom = 'Etienne'
nom = 'Walch'
id_membre = None

# 1ere option
liste = filter(None, [id_membre, nom, prenom])
# 2e option avec compréhension de liste
liste = [e for e in [id_membre, nom, prenom] if e]
nom_complet = '_'.join(liste)
print(nom_complet)

print("=" * 100)

# La fonction pprint
print("La fonction pprint")
mon_dict = {'firstName': 'Bidhan', 'lastName': 'Chatterjee', 'age': 40,
            'address': {'streetAddress': '144 J B Hazra', 'city': 'Burdwan', 'state': 'Paschimbanga',
                        'postalCode': '713102'},
            'phoneNumber': [{'type': 'personal', 'number': '09832209761'}, {'type': 'fax', 'number': '91-342-2567692'}]}
print(mon_dict)
print('=' * 100)
pprint(mon_dict)

print("=" * 100)

# Utilisation avancée de la fonction format
print("Utilisation avancée de la fonction format")

text = '{} {}'.format('Pierre', 'Dupont')
print(text)

text = '{0} {1}'.format('Pierre', 'Dupont')
print(text)
text = '{1} {0}'.format('Pierre', 'Dupont')
print(text)
text = '{0} {0}'.format('Pierre', 'Dupont')
print(text)

text = '{} a {} ans'.format('Pierre', 18)
print(text)

text = '{:10} {}'.format('Debut', 'Fin')
print(text)

text = '{:>10} {}'.format('Debut', 'Fin')
print(text)

text = '{} {:=>10}'.format('Debut', '  Fin')
print(text)

text = '{:+^50}'.format(' Partie 01 ')
print(text)

text = '{:.3}'.format('Pierre')
print(text)
text = '{:.3}'.format(2.51888)
print(text)

user = {'Prenom': 'Etienne', 'Nom': 'Walch'}
text = 'Bonjour, je m\'appelle {d[Prenom]} {d[Nom]}'.format(d=user)
print(text)


class MaVoiture(object):
    def __init__(self):
        self.couleur = 'Rouge'
        self.marque = 'Mercedes'


text = "J'ai une {o.marque} de couleur {o.couleur}".format(o=MaVoiture())
print(text)

print("="*100)
