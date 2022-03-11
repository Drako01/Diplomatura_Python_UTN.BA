class AccederInstanciaMail:
    def __get__(self, instance, owner):
        print('Obtener Estado de Instancia')
        return instance._mail + '.ar'
    def __set__(self, instance, valor):
        print('Seteo de Estado de Instancia')
        instance._mail = valor


class Cliente:
    def __init__(self, usuario, _mail):
        self._usuario = usuario
        self._mail = _mail
        
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
            
    usuario = DescriptorUsuario()
    mail = AccederInstanciaMail()
    
    
cliente1 = Cliente('Juan', 'juan@gmail.com')
print(cliente1.usuario, cliente1._mail, cliente1.mail)
cliente1.usuario = 'Ana'
print(cliente1.usuario)
cliente1.mail = 'ana@gmail.com'
print(cliente1.usuario, cliente1._mail, cliente1.mail)
print(cliente1.__dict__)