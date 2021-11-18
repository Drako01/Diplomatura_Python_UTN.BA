ingreso = 0 

def nuevoIngreso(): 
    global ingreso
    ingreso += 1 
    print('Se ha realizado un nuevo ingreso',ingreso) 

nuevoIngreso() 
nuevoIngreso() 
nuevoIngreso() 
nuevoIngreso() 
print(ingreso)

