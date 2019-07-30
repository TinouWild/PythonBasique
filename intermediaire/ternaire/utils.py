a = 19

if a >= 18:
    print('Vous etes majeur')
else:
    print('Vous etes mineur')

# Possible avec Python 3.x mais pas avec 2.x
print('Vous etes majeur') if a >= 18 else print('Vous etes mineur')

# Avec Python 2.x
majeur_ou_mineur = 'majeur' if a >= 18 else 'mineur'
print('Vous etes {}'.format(majeur_ou_mineur))

#####################
# Avec opérateur ternaire
a = 5
a_positif = True if a > 0 else False
print(a_positif)

age = 20
majeur = True if age >= 18 else False
print(majeur)

#######################
# Sans opérateur ternaire
a = 5
if a > 0:
    a_positif = True
elif a < 0:
    a_positif = False

print(a_positif)
