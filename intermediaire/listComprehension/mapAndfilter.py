liste = [1, 2, 3, 4, 5]

# Avec map
r = map(lambda x: x*x, liste)
print(list(r))

# Avec les listes en compréhension
r = [i*i for i in liste]
print(r)

# Avec filter
r = filter(lambda x: x % 2 == 0, liste)
print(list(r))

# Avec les listes en compréhension
r = [i for i in liste if i % 2 == 0]
print(r)