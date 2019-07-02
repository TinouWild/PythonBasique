fichier = input("Entrez un fichier à ouvrir : ")

try:
    f = open(fichier, 'r')
    print(f.read())
except FileNotFoundError as e:
    print("Erreur :", e)
except UnicodeDecodeError as e:
    print("Erreur :", e)
else:
    f.close()