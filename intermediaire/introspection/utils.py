import random

help(random)
help(random.randint)

import sys

print(sys.version)
print(sys.version_info.major)
print(sys.version_info.minor)
print(sys.platform)
print(sys.path)
print(sys.getwindowsversion().major)
print(sys.executable)
print(sys.argv)

import pprint

print(type(pprint))
print(type(pprint.pprint))
print(type(type))

import json
import os

fichier = os.path.join(os.path.dirname(__file__), 'variable.json')

with open(fichier, 'r') as f:
    variable = json.load(f)

print(type(variable))
variable = True if variable == 'True' else False
print(type(variable))

if type(variable) == bool:
    print('La variable est un boolean')
elif type(variable) == str:
    print('La variable est une chaine de caractere')
