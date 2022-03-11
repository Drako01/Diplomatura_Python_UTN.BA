class Auto:
    def __setattr__(self, atributo, valor):
        if atributo == 'precio':
            #self.__dict__[atributo] = valor + 202000
            self.atributo = valor + 202000

        else:
            raise Auto(atributo + ' No permitido')
auto1 = Auto()
auto1.precio = 1000000
print(auto1.precio)