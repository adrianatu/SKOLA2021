import sqlite3

#db = sqlite3.connect('test.db')

# dati = db.execute(""" SELECT name FROM sqlite_schema
#                   WHERE type = 'table'
#                   """)
                  


# dati = db.execute(""" SELECT * FROM edienkarte
#                   JOIN sastavdalas 
#                   ON edienkarte.id = sastavdalas.id
#                   """)

# rezultats = dati.fetchall()

# print(rezultats)

import datetime

start = datetime.datetime.now()

db = sqlite3.connect('titanic DB.db')

#dati = db.execute("SELECT PassengerId FROM titanic ORDER BY Name")
#dati = db.execute("SELECT SUM(Survived) FROM titanic WHERE Survived = 1")
dati = db.execute("SELECT Name FROM titanic ORDER BY Name")

rezultats = dati.fetchall()

#print(rezultats)

end = datetime.datetime.now()


for rinda in rezultats:
  print(rinda)

laiks = end-start
print(laiks)