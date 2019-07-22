class Voiture:
    voiture_crees = 0
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    def __str__(self):
        return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse}."

    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche" ,vitesse=200, prix=180000)

    # Pouvoir utiliser une méthode sans passer d'argument de classe
    @staticmethod
    def afficher_nombre_voitures():
        print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")

lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
Voiture.afficher_nombre_voitures()