a = 5
b = 5

print(a == b)
# Juste fonctionnel de -5 à 256.
print(a is b)
print(id(a))
print(id(b))

a = -2364
b = -2364
print(a == b)
print(a is b)
print(id(a))
print(id(b))


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(a == b)
print(a is b)
print(id(a))
print(id(b))


a = [1, 2, 3, 4, 5]
b = a
print(a == b)
print(a is b)
print(id(a))
print(id(b))