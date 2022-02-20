if __name__ == "__main__":
    from personap.personam import Persona
    from gerentep.gerentem import Gerente

    Juan = Persona("Juan Garcia", 42)
    Susana = Persona("Susana Gomez", 45, 40000)
    Tom = Gerente("Tom Perez", 42, 50000)
    db = [Juan, Susana, Tom]

    for persona in db:
        print(persona.nombre, persona.sueldo)
    print("-----------------------")

    for objeto in db:
        objeto.dar_aumento(0.10)

    for objeto in db:
        print(objeto.nombre, "=>", objeto.sueldo)
    print("-----------------------")

    for objeto in db:
        print(objeto.apellido(), "=>", objeto.sueldo)
    print("-----------------------")

    # #########################################
    # Para llamada a __str__
    # #########################################
    print("--------__str__-----------")
    print(Juan)
    print(Susana)
    print("-----------------------")
