import re

adresses_mail = ['christian_martin@gmail.com',
                 'JaiOublieLarobasegmail.com',
                 'MarieHutchinson03523@yahoo.co.uk',
                 'UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com',
                 'ceciNestPasUneDresseMail']

for mail in adresses_mail:
    a = re.search(r'[a-zA-Z0-9!_-]+@[a-zA-Z]+.[a-zA-Z]+(.[a-zA-Z]*)', mail)
    if a != None:
        print(mail + ' est une adresse mail valide !')
    else:
        print(mail + ' est une adresse mail invalide !')

# L'adresse christian_martin@gmail.com est valide
# L'adresse JaiOublieLarobasegmail.com est invalide
# L'adresse MarieHutchinson03523@yahoo.co.uk est valide
# L'adresse UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com est valide
# L'adresse ceciNestPasUneDresseMail est invalide
