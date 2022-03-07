class Indexador:
    def __getitem__(self, indice):
        return indice ** 0.5


X = Indexador()
print(X[64])
