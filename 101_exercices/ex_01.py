import math
import random
import os
import string
import datetime

chaine = "Pierre, Julien, Anne, Marie, Lucien"
print(', '.join(sorted(chaine.split(', '))))

print("=" * 100)
# (4 pi / 3) x rayon^3
rayon = 10.0
volume = (4 * math.pi / 3) * rayon ** 3
print(volume)

print("=" * 100)
a = 12
if a > 10:
    print('{} est plus grand que 10'.format(a))

print("=" * 100)
print(list(range(5, 15)))

print("=" * 100)
for i in range(1, 7):
    print(random.randint(1, 6))

print("=" * 100)
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
i = 0
for a in phrase:
    if a == lettre_a_chercher:
        i += 1
print(i)
print(phrase.lower().count(lettre_a_chercher))

print("=" * 100)
ma_liste = ["Pierre", "Paul", "Marie"]
print(ma_liste[0])
print(ma_liste[-1])
print(ma_liste[:2])
print(ma_liste[-2:])

print("=" * 100)
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
liste_finale = [nombre for nombre in liste_01 if nombre in liste_02]
print(liste_finale)

print("=" * 100)
liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
liste.sort(key=lambda x: x[1])
print(liste)

print("=" * 100)
employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes.get('01').get('identite').get('prenom'))
print(employes.get('01', {}).get('identite', {}).get('prenom', 'valeur inconnue'))

print("=" * 100)
employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
print(sum(employes.values()))

print("=" * 100)
liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]
resultat = [i * (i + 1 % (i * 5)) for i in sorted(list(set(liste)))]
print(resultat)

print("=" * 100)
fichier = "C:/Python36/python.exe"
extension = os.path.splitext(fichier)[1][1:]
print(extension)

print("=" * 100)
mot = "Udemy"
mot_inverse = []
for a in reversed(mot.lower()):
    mot_inverse.append(a)
resultat = ''.join(mot_inverse).capitalize()
print(resultat)

print("=" * 100)
mot = "Bonjour"
mot = list(mot)
random.shuffle(mot)
print(''.join(mot).capitalize())

print("=" * 100)
nombre = 2938.48872
decimales = 3

print("Nombre tronqué: {nombre:.{decimales}f}".format(nombre=nombre, decimales=decimales))

print("=" * 100)
mot = "Python"
for i in range(len(mot)):
    print(i)

print("=" * 100)


def multiplicateur_mot(mot, mult=5):
    return mot * mult


mot_multiplie = multiplicateur_mot(mot="Bonjour")
print(mot_multiplie)

print("=" * 100)


def addition(a, b):
    return a + b


print(addition(5, 10))

print("=" * 100)
nombre = 7
for i in range(0, 11):
    print(str(i) + ' x ' + str(nombre) + ' = ' + str(i * nombre))

print("=" * 100)
liste = ["Pierre", "Paul", "Marie"]
for i, prenom in enumerate(liste):
    print(str(i) + ' ' + prenom)

print("=" * 100)
nombres = range(50)
nombres_pairs = []
for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)
print(nombres_pairs)

print("=" * 100)
nombres = range(50)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)

print("=" * 100)
nombre = 209812
total = sum([int(i) for i in str(nombre)])
print(total)

print("=" * 100)
liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"
liste_finale = [a.replace(nom_a_chercher, nouveau_nom) for a in liste]
print(liste_finale)

print("=" * 100)
nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
no_doublons = []
for a in nombres:
    if a not in no_doublons:
        no_doublons.append(a)
print(no_doublons)

print("=" * 100)
employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
i = 1
for element in liste:
    if not str(element).isdigit():
        employes["id-{:02d}".format(i)] = element
        i += 1

print(employes)

print("=" * 100)
alphabet = string.ascii_lowercase
d = {}
i = 1
for lettre in list(alphabet):
    d[i] = lettre
    i += 1
print(d)

# solution
alphabet = string.ascii_lowercase
indices = range(1, len(alphabet) + 1)
liste_zip = zip(range(1, len(alphabet) + 1), alphabet)
resultat = dict(liste_zip)

print(resultat)

print("=" * 100)


def longueur(variable):
    total = 0
    for i in list(variable):
        total += 1
    return total


print(longueur("bonjour"))

print("=" * 100)
# Longueur maximale à afficher
n = 8
symbole = '*'
liste = list(range(1, n + 1)) + list(range(n - 1, 0, -1))
for i in liste:
    print(symbole * i)

print("=" * 100)
symbole = "$"
taille = 10
for i in range(1, taille + 1):
    espaces = " " * (taille - i)
    print(espaces + (symbole + " ") * i)

print("=" * 100)
texte = "Bonjour Udemy"
taille = len(texte)
print('-' * taille)
for lettre in texte:
    print('|' + ' ' * int((taille - 3) / 2) + lettre + ' ' * int((taille - 3) / 2) + '|')
print('-' * taille)

print("=" * 100)
nombre = 52039480394023
nombre_inter = []
count = 0
for i in reversed(str(nombre)):
    count += 1
    if count == 3:
        nombre_inter.append(i)
        nombre_inter.append(',')
        count = 0
    else:
        nombre_inter.append(i)
nombre_final = ''.join(reversed(nombre_inter))
print(nombre_final)

print("=" * 100)
age = 25
mois_de_naissance = 10
current_year = datetime.datetime.today().year
current_month = datetime.datetime.today().month
if mois_de_naissance <= current_month:
    print(current_year - age)
else:
    print(current_year - 1 - age)

print("=" * 100)


def somme(a, b):
    if a < b:
        min = a
        max = b
    else:
        min = b
        max = a
    return sum(range(min, max + 1))


print(somme(2, 6))


# solution
def somme(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


print(somme(6, 2))

print("="*100)
dossier = "/Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy"


def remonter_dossier(dossier, nombre=1):
    i = 0
    while i < nombre:
        dossier = os.path.dirname(dossier)
        i += 1
    return dossier


print(remonter_dossier(dossier, 2))

print("="*100)
nombre = 50
diviseurs = []
for i in range(1, nombre + 1):
    if nombre % i == 0:
        diviseurs.append(i)
print(diviseurs)

print("="*100)
nombre = 1000
nombres = []
for i in range(1, nombre + 1):
    if i % 7 == 0 and i % 3 != 0:
        nombres.append(i)
print(nombres)

print("="*100)
nombre = 5
res = 1
for chiffre in range(1, nombre + 1):
    multiplication = res * chiffre
    res = multiplication
print(res)

print("="*100)
octet = ''.join([str(random.randint(0, 1)) for count in range(1, 9)])
print(octet)

print("="*100)
nb_jours = datetime.date(2018, 7, 11) - datetime.date(2014, 7, 2)
print(nb_jours.days)

print("="*100)
taille = 8
all_carac = string.ascii_letters + string.digits + string.punctuation
mdp = ''.join(random.choice(all_carac) for i in range(1, taille + 1))
print(mdp)

print("="*100)
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
mot = "elit"
lorem = lorem.replace(',', '').replace('.', '').lower().split()
print(lorem.count(mot))

print("="*100)
phrase = "Phrase en camel case"
phrase = phrase.lower().split()
print(phrase)

print("="*100)
