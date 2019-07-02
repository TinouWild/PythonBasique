import glob
import json

dossier = "/home/etienne/Documents/FormationPython/PythonBasique/dossierTest/dossier_exemple/**"
files = glob.glob(dossier, recursive=True)


numero_bancaire = None
numero_secu = None

for f in files:
    if f.endswith('json'):
        with open(f, "r") as file:
            liste = json.load(file)
            if 'Credit Mutuel' in liste:
                numero_bancaire = liste['Credit Mutuel']['Numero de compte']
    elif f.endswith('txt'):
        with open(f, "r") as file:
            contenu = file.read()
            if 'Numéro de sécurité sociale' in contenu:
                numero_secu = contenu.split(":")[-1]

print(f"Numero de compte : {numero_bancaire}")
print(f"Numero de sécu : {numero_secu}")