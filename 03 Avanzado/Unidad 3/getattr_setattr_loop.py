class Auto:
    def __init__(self):
        self.color = 'Rojo'
    def __getattribute__(self, color):
        return self.color

auto1 = Auto()
print(auto1.color) 