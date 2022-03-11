class DescriptorUsuario:

    def __get__(*args):
        print('get')
 
class Cliente:

    usuario = DescriptorUsuario()

cliente1 = Cliente()
cliente1.usuario
Cliente.usuario
cliente1.usuario = 'Juan'
print(cliente1.usuario)
print(list(cliente1.__dict__.keys()))