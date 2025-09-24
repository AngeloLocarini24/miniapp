import sqlite3

connection = sqlite3.connect('db.sqlite3')  # Crea il file db.sqlite3 se non esiste

with open('schema.sql') as f:
    connection.executescript(f.read())  # Esegue il contenuto del file schema.sql

connection.commit()
connection.close()

print("Database creato con successo!")
