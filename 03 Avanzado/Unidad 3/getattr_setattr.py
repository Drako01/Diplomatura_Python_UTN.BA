from random import randint

class Auto:

    def __getattr__(self, dato):
        if dato == 'color':
            rojo = randint(0, 255)
            verde = randint(0, 255)
            azul = randint(0, 255)
            return 'rgb('+str(rojo)+','+str(verde)+','+str(azul)+')'
        else:
            raise AttributeError(dato)

    def __setattr__(self, dato, valor):
        print('set: %s %s' % (dato, valor))
        if dato == 'color':
            self.__dict__['_color'] = valor

        else:
            self.__dict__[dato] = valor

auto1 = Auto()
print(auto1.color)
auto1.color = '(f,0,0)'
print('-------------------')
print(auto1._color)
print('-------------------')
print(auto1.color)
print(auto1.color)
print(auto1.color)
print('-------------------')
print(auto1._color)
print('-------------------')

auto1.altura = '1.6 metros'
print(auto1.altura)
print('-------------------')
print(auto1.__dict__)