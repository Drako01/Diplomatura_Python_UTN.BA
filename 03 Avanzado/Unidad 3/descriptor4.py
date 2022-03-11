class DescriptorUsuario:

    "Documentación de descriptor de nombre"
    def __get__(self, instance, owner):
        print('Atrapa valor... ')
        return instance._usuario.upper()

    def __set__(self, instance, valor):
        print('Cambia el valor ...')
        instance._usuario = valor

    def __delete__(self, instance):
        print('Remover el atributo ...')
        del instance._usuario
        
class Cliente:
    def __init__(self, usuario):
        self._usuario = usuario

    usuario = DescriptorUsuario()

cliente1 = Cliente('Juan')
print(cliente1.usuario)
cliente1.usuario = 'Pedro'
print(cliente1.usuario)
del cliente1.usuario
print(cliente1.usuario)