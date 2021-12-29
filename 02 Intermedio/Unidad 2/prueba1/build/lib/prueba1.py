def recorrerLista(item, nivel=0):      # Agrego valor por defecto
    for x in item: 
       if isinstance(x, list): 
          recorrerLista(x, nivel + 1) 
       else: 
          for y in range(nivel): 
              print("\t", end="")                # Agrego indentación en lugar de saltos de línea
          print(x)
