import string

prenom = 'Astrid'
tab_index = [string.ascii_lowercase.index(i) for i in prenom.lower()]
resultat = zip(prenom, tab_index)
for a in resultat:
    print(str(list(a)[0]) + ' => ' + str(list(a)[1] + 1))
