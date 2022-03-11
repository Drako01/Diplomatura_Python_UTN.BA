class AccederInstanciaMail:

    def __init__(self, mail):
        self.mail = mail
    def __get__(self, instance, owner):
        return '%s, %s' % (self.mail, instance.mail)
    def __set__(self, instance, valor):
        instance.mail = valor

class Cliente:

    def __init__(self, mail):
        self.mail = mail
    administradormail = AccederInstanciaMail('ana@gmail.com')

cliente1 = Cliente('juan@gmail.com')
print('1-'*10)
print(cliente1.administradormail)
print('2-'*10)
cliente1.administradormail = 'juanbarreto@gmail.com'
print('3-'*10)
print(cliente1.administradormail)
print('-'*10)
print(cliente1.__dict__)
