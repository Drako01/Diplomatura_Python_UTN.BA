class MiEmpresa:

    def __init__(self, usuario):
        self._usuario = usuario

    def get_usuario(self):
        print('Recupera el usuario...')
        return self._usuario.upper()

    def set_usuario(self, valor):
        print('Modifica el usuario...')
        self._usuario = valor

    def del_usuario(self):
        print('Remueve el usuario...')
        del self._usuario
    usuario = property(get_usuario, set_usuario, del_usuario, "Datos adicionales")

class Cliente(MiEmpresa): pass    
    
cliente1 = Cliente('Juan')
print(cliente1.usuario)
cliente1.usuario = 'Pedro'
print(cliente1.usuario)
del cliente1.usuario
print(Cliente.usuario.__doc__)