# exemple de fichier en Python2 pour tester la conversion avec lib2to3
import json


def greet(firstname):
    print "Hello, {0}!".format(firstname)


name = raw_input("What's your name?")
greet(name)
