class Persona:

    def __init__(self, nombre):
        self._nombre = nombre

    def __getattr__(self, atributo):
        print('get: ' + atributo)
        if atributo == 'nombre':
            return self._nombre
        else:
            raise AttributeError(atributo)

    def __setattr__(self, atributo, valor):
        print('set: ' + atributo)
        if atributo == 'nombre':
            atributo = '_nombre'
        self.__dict__[atributo] = valor

    def __delattr__(self, atributo):
        print('del: ' + atributo)
        if atributo == 'nombre':
            atributo = '_nombre'
        del self.__dict__[atributo]

persona1 = Persona('Juan')
print(persona1.nombre)
persona1.nombre = 'Pedro'
del persona1.nombre
