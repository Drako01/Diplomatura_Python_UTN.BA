class DescriptorUsuario:

    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')

class Cliente:

    usuario = DescriptorUsuario()

cliente1 = Cliente()
cliente1.usuario
print('-'*15)
Cliente.usuario
#cliente1.usuario = 'Juan'
print(cliente1.usuario)
print(list(cliente1.__dict__.keys()))