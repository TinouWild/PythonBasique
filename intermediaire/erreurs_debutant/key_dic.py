dic = {'Pierre': 'Serveur',
       'Julien': 'Libraire',
       'Marie': 'Ingenieure'}

prenom = 'Paul'

# Mauvaise façon de faire
# profession = dic[prenom]

# profession = dic.get(prenom)
# print(profession)

profession = dic.get(prenom, "{} n'est pas dans le registre.".format(prenom))
print(profession)
