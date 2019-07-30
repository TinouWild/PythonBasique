for i in [1, 2, 3, 4, 5]:
    print(i)

for l in 'Udemy':
    print(l)

for key in {'user_01': 'Paul', 'user_02': 'Pierre'}:
    print(key)

iterateur = iter('Udemy')

print(iterateur)
print(iterateur.__next__())
print(next(iterateur))