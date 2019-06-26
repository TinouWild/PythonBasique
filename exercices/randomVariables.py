import random

a = random.randint(1, 100)
b = random.randint(1, 100)

if a < b:
    print(f"Le nombre {a} est plus petit que le nombre {b}")
elif a > b:
    print(f"Le nombre {a} est plus grand que le nombre {b}")
else:
    print(f"Le nombre {a} et {b} sont égaux.")