class Birthday:
    def __init__(self, body, age):
        self.body = body
        self.age = age
        print(f"Joyeux anniversaire {self.body} pour tes {self.age} années !")
        self.instructions()

    def loop_one(self):
        print("Ceci est mon premier cadeau !")

    def loop_two(self):
        print("Ceci est mon deuxième cadeau !")

    def loop_three(self):
        print("Ceci est mon dernier cadeau !")

    def confirmation(self, loop_index):
        response = input(f"Es-tu en train d'ouvrir le cadeau numéro {loop_index} ?")
        if response == "Y":
            pass
        else:
            print("Tu dois répondre par Y si c'est le cas")

    def appel_contexte(self):
        response = input("Souhaites-tu mettre en place un contexte ? (Y or N)")
        if response == "Y":
            print("Une invitation à tous tes contacts vient d'être envoyée.")
        elif response == "N":
            print("Nul.")
        else:
            print("Pas compris.")

    def instructions(self, nb_gifts=3):
        for _ in range(1, nb_gifts + 1):
            if _.__index__() == 1:
                self.confirmation(_.__index__())
                self.loop_one()
                print("Chose promise, chose dûe ! Je t'avais promis une maison pour ton anniversaire !")
            elif _.__index__() == 2:
                self.confirmation(_.__index__())
                self.loop_two()
                print("Bon. J'ai essayé de noyer le poisson mais tu es trop douée... Reste à trouver le contexte")
                self.appel_contexte()
            else:
                self.confirmation(_.__index__())
                self.loop_three()
                print("A défaut d'un site te permettant de bloguer tous tes voyages, j'espère que cela te plaira et "
                      "te donnera l'occasion de scratcher quelques pays supplémentaires dans les années à venir !")


julie = Birthday("Julie", 35)
