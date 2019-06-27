# affectation simple
a = 5
b = 2

# affectation parallèle
a, b = 6,  10

# affectation multiples
a = b = c = 20

#input
nombre = input("Entrez un nombre: ")
# print(nombre)

#conversion de types
b = "10"
b = int(b)
# print(a + b)

#fstring depuis la 3.6
prenom = "Etienne"
# print(f"Coucou {prenom} !")

#concaténation avant 3.6
nbr = 6
# print("Le nombre est égal à {}".format(nbr))
# print("{} est une machine et travaille vachement bien avec {} son demi-cerveau".format("Julie", "Etienne"))

# opérations mathématiques avec le module math
# import du module
import math

math.ceil(4.3) # entier supérieur
math.exp(2) # exponentielle
math.isinf(3.3) # teste si la valeur est infinie (booléen)

# Compréhension de listes
liste = [-5, 6, 8, 12, 14, 0, 1, 5, 17, 4]
nombres_positifs = [i for i in liste if i % 2 == 0]
print(nombres_positifs)