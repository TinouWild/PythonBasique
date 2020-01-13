# exemple de fichier en Python2 pour tester la conversion avec lib2to3
import json


def greet(name):
    print("Hello, {0}!".format(name))


print("What's your name?")
name = input()
greet(name)
