liste = range(10)

index = 2

# premiere solution
try:
    r = liste[index]
    print(r)
except IndexError:
    print("L'index {} n'existe pas.".format(index))

# deuxieme solution
r = liste[index] if len(liste) > index else None
print(r)
