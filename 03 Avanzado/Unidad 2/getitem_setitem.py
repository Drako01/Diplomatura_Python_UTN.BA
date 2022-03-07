class Indexador:  
    lista = ['M','a','n','z','a','n','a']    
    def __getitem__(self, indice):            
        return self.lista[indice]

    def __setitem__(self, indice, valor):
        self.lista[indice] = valor
        
X = Indexador() 
X[6] = 'o'    
print(X.lista) 
 
