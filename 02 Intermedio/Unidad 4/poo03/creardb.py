if __name__ == "__main__":
    from datosiniciop.personam import Persona

    Juan = Persona("Juan Garcia", 42)
    Susana = Persona("Susana Gomez", 45, 40000)

    personas = [Juan, Susana]
    for persona in personas:
        print(persona.nombre, persona.sueldo)
    print("-----------------------")

    # ########################################
    # Por comprension
    # ########################################
    x = [(persona.nombre, persona.sueldo) for persona in personas]
    print(x)
    print("-----------------------")

    y = [
        (persona.edad ** 2 if persona.edad >= 7 else persona.edad)
        for persona in personas
    ]
    print(y)
    print("-----------------------")
