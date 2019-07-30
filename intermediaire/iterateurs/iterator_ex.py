from random import randint


class lettre_random:
    def __init__(self, nom):
        self.i = 0
        self.max = len(nom)
        self.nom_restant = list(nom)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.max:
            lettre = self.nom_restant.pop(randint(0, len(self.nom_restant) - 1))
            self.i += 1
            return lettre
        else:
            raise StopIteration()


nom = 'Bonjour'
nom_random = lettre_random(nom)
nom_melange = [l for l in nom_random]
print(nom_melange)
print(''.join(nom_melange))

