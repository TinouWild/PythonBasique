chemin = "/home/etienne/Documents/FormationPython/PythonBasique/dossierTest"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

import os

for key, values in d.items():
    for dossier in values:
        sous_dossier = os.path.join(chemin, key, dossier)
        os.makedirs(sous_dossier, exist_ok=1)

