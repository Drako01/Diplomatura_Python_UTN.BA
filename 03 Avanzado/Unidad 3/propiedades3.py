class Cliente:

    def __init__(self, usuario):
        self._usuario = usuario

    @property        
    def usuario(self):
        "Datos adicionales"
        print('Recupera el usuario...')
        return self._usuario.upper()

    @usuario.setter
    def usuario(self, valor):
        print('Modifica el usuario...')
        self._usuario = valor

    @usuario.deleter
    def usuario(self):
        print('Remueve el usuario...')
        del self._usuario

cliente1 = Cliente('Juan')
print(cliente1.usuario)
cliente1.usuario = 'Pedro'
print(cliente1.usuario)
print(list(cliente1.__dict__.keys()))
del cliente1.usuario
print(Cliente.usuario.__doc__)



