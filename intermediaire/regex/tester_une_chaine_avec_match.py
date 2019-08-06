import re

# Pourquoi on met un 'r'
print('\tBonjour') # sans r, \t est évalué comme une tabulation
print(r'\tBonjour') # avec, non évalué donc interpreté comme faisant partie du string

a = re.match(r'.+', 'Pierre Dupont')
print(a.group())

a = re.match(r'(\w+)(\s)(\w+)', 'Pierre Dupont')
print(a.group(0))
print(a.group(1))
print(a.group(2))
print(a.group(3))

a = re.match(r'(?P<prenom>\w+) (?P<nom>\w+)', 'Pierre Dupont')
print(a.group('prenom'))
print(a.group('nom'))

print(a.groups())
print(a.groupdict())

b = re.match(r'\s+', 'pierre dupont')
print(b)
