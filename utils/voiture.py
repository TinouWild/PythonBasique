class Voiture:
    voitures_crees = 0

    def __init__(self, marque):
        Voiture.voitures_crees += 1
        self.marque = marque


voiture = Voiture("Ferrari")