import random

nb_mystere = random.randint(1, 1000)
nb_utilisateur = input("Quel est le nombre mystère ?")

if nb_utilisateur.isdigit():
    nb_utilisateur = int(nb_utilisateur)
else:
    exit()

if nb_mystere < nb_utilisateur:
    print(f"Le nombre mystère est plus petit que {nb_utilisateur}")
elif nb_mystere > nb_utilisateur:
    print(f"Le nombre mystère est plus grand que {nb_utilisateur}")
else:
    print("Bravo, vous avez trouvé le nombre mystère !")

