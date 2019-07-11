class Voiture:
    def __init__(self):
        self.essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d'essence.")

    def roule(self, km):
        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return

        if self.essence > (km * 5) / 100:
            if 0 < self.essence < 10:
                print("Vous n'avez bientôt plus d'essence !")
            self.essence -= (km * 5) / 100
        else:
            self.essence = 0
            print("Panne sèche")
            return

        self.afficher_reservoir()

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")


