import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
)
""")

# Insérer des données
# d = {"prenom": "Etienne", "nom": "Walch"}
# c.execute("INSERT INTO employees VALUES (:prenom, :nom)", d)

# Récupérer des données
c.execute("SELECT * FROM employees")
donnees = c.fetchall()
c.execute("SELECT * FROM employees")
donnee = c.fetchone()

print(donnees)
print(donnee)

conn.commit()
conn.close()
