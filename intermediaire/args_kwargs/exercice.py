import os


def concatenation_chemin(*args):
    return os.path.normpath(os.path.join(*args))


chemin_complet = concatenation_chemin('C:/Utilisateurs', 'ThibH', 'Images')
print(chemin_complet)
