class DescriptorValor():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instancia, type=None):
        return instancia.__dict__.get(self.name)

    def __set__(self, instancia, valor):
        instancia.__dict__[self.name] = valor if valor % 2 == 0 else 0

class Evaluar:
    valor1 = DescriptorValor()
    valor2 = DescriptorValor()
    valor3 = DescriptorValor()
    valor4 = DescriptorValor()
    valor5 = DescriptorValor()
    valor6 = DescriptorValor()
    valor7 = DescriptorValor()
        
el_valor = Evaluar()
el_valor.valor1 = 1
el_valor.valor2 = 2
el_valor.valor3 = 3
el_valor.valor4 = 4
el_valor.valor5 = 5
el_valor.valor6 = 6
el_valor.valor7 = 7
print(el_valor.valor1)
print(el_valor.valor2)
print(el_valor.valor3)
print(el_valor.valor4)
print(el_valor.valor5)
print(el_valor.valor6)
print(el_valor.valor7)