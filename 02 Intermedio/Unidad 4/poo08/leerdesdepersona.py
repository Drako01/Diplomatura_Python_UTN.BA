import shelve
db = shelve.open('persona')
for key in db:
    print(key, '=>\n ', db[key].nombre, db[key].sueldo)

Juan = db['Juan']
print(Juan.apellido())
print(db['Susana'].apellido())
db.close()
