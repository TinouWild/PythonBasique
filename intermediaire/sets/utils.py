a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print('Union de A et B :')
print(a.union(b))
# print(a | b)

print('Intersection de A et B')
print(a.intersection(b))
# print(a & b)

print('Différence de A et B')
print(a.difference(b))
print(b.difference(a))
# print(a - b)
# print(b - a)

print('Différence symétrique (Union - intersection')
print(a.symmetric_difference(b))
# print(a ^ b)
