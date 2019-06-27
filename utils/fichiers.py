import os
import json

# ---------------------------------------------------- #
# création d'un dossier pourri
path = "../../PythonBasique"
dossier = os.path.join(path, 'dossierTest')

if not os.path.exists(dossier):
    os.makedirs(dossier)

# ---------------------------------------------------- #
# lire le contenu d'un fichier
chemin = "../dossierTest/fichieralire.txt"

# avec repr
with open(chemin, "r") as f:
    contenu = repr(f.read())
    print(contenu)

# avec readLines
with open(chemin, "r") as f:
    contenu = f.readlines()
    print(contenu)

# avec splitLines
with open(chemin, "r") as f:
    contenu = f.read().splitlines()
    print(contenu)

# ---------------------------------------------------- #
# écrire dans un fichier

pathToWrite = "../dossierTest/fichierouecrire.txt"

# en mode write "w" --> efface le contenu et écrit dedans
with open(chemin, "w") as f:
    f.write("\nJ'écris dans le fichier !")

# en mode append "a" --> ajoute le contenu à la suite du fichier
with open(chemin, "a") as f:
    f.write("\nAu revoir ce fichier tout pourri !")

# ---------------------------------------------------- #
# fichiers json, écrire dans un fichier json

pathJson = "../dossierTest/fichier.json"
with open(pathJson, "w") as f:
    json.dump(list(range(10)), f, indent=4)

#lire un fichier json
with open(pathJson, "r") as f:
    liste = json.load(f)
    print(liste)


