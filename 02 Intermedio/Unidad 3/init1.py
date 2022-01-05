class Comentario:
    def imprimir( self ):
        print(self.texto)

objeto = Comentario()
objeto.texto = "Hola variable de instancia"
objeto.imprimir()
input()
