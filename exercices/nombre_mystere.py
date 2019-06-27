import random

nb_mystere = random.randint(1, 50)
i = 1
while i <= 5:
    nb_utilisateur = input(f"Essai numéro {i} ::: Quel est le nombre mystère ?")
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
        exit()
    i += 1
print(f"Vous avez perdu, le nombre mystère était {nb_mystere}")



