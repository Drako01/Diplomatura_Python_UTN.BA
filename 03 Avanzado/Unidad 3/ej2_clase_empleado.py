EDAD_JUBILACION = 65

class EmpleadoDescriptor():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instancia, type=None):
        return instancia.__dict__.get(self.name)

    def __set__(self, instancia, valor):
        if self.name == "edad":
            if valor < 0:
                raise ValueError("La edad del empleado no puede ser negativa")
            elif valor == EDAD_JUBILACION - 1:
                print("El empleado está a un año de la edad de jubilación")
        instancia.__dict__[self.name] = valor
    
class Empleado():
    nombre = EmpleadoDescriptor()
    edad = EmpleadoDescriptor()
    salario = EmpleadoDescriptor()

    def __str__(self):
        return "Nombre: {} - Edad: {} - Salario: {}".format(
            self.nombre, 
            str(self.edad), 
            str(self.salario)
        ) 

try:
    print("Creando al empleado Gaspar...")
    gaspar = Empleado()
    gaspar.nombre = "Gaspar"
    gaspar.edad = 64
    gaspar.salario = 10000
    print(gaspar, "\n")
    
    print("Creando al empleado Melchor...")
    melchor = Empleado()
    melchor.nombre = "Melchor"
    melchor.edad = 65
    melchor.salario = 15000
    print(melchor, "\n")

    print("Creando al empleado Baltazar...")
    baltazar = Empleado()
    baltazar.nombre = "Baltazar"
    baltazar.edad = -40
    baltazar.salario = 20000
    print(baltazar, "\n")
    
except ValueError as err:
    print(str(err))