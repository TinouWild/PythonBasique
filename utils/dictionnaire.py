d = {
    "prenom": "Etienne",
    "age": 30,
    "ville": "Mulhouse"
}
print(d.get('prenom'))

d["prenom"] = "Martine"
print(d.get('prenom'))

## Supprimer une clé : del d["prenom"]

print(d.keys())
print(d.values())

print(d.items())