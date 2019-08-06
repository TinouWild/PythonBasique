import re

numeros_de_telephone = ['06-71-45-34-23',
                        '02-12-33-75-12',
                        '00-23-14-52-44',
                        '514-235-0293',
                        '03-52-31-56-34']

for numero in numeros_de_telephone:
    a = re.search(r'([0]{1}[1-9]{1})-((\d){2}-){3}(\d){2}', numero)
    if a != None:
        print(a.group() + ' est un numéro valide !')

# Le numéro 06-71-45-34-23 est valide
# Le numéro 02-12-33-75-12 est valide
# Le numéro 00-23-14-52-44 est invalide
# Le numéro 514-235-0293 est invalide
# Le numéro 03-52-31-56-34 est valide
