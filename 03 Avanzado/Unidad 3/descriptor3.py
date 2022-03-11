class DescriptorUsuario:

    def __get__(*args):
        print('get')
        
    def __set__(*args):
        raise AttributeError('No se puede realizar un set')

class Cliente:

    usuario = DescriptorUsuario()

cliente1 = Cliente()
cliente1.usuario
Cliente.usuario
cliente1.usuario = 'Juan'

