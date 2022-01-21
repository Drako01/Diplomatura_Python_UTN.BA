import shelve
from personap.personam import Persona
from gerentep.gerentem import Gerente

Juan = Persona("Juan Garcia", 42)
Susana = Persona("Susana Gomez", 45, 40000)
Tom = Gerente("Tom Perez", 42, 50000)

db = shelve.open("persona")
Tom = db["Tom"]
Tom.dar_aumento(0.20)
db["Tom"] = Tom
db.close()
