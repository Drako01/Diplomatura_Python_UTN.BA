class Indexador:
    texto = "El día está lindo"

    def __getitem__(self, indice):
        return self.texto[indice]


X = Indexador()
print(X[3:8])
