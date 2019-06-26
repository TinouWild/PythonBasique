import os

chemin = "/home/etienne/Documents/FormationPython"
dossier = os.path.join(chemin, "test")

if not os.path.exists(dossier):
    os.makedirs(dossier)
    print(f"Le dossier {dossier} a été créé !")
else:
    print(f"Le dossier {dossier} existe déjà !")

