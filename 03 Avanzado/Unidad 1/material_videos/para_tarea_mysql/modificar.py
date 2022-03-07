from tkinter import *

archivo = 'persona'
campos = ('id', 'Titulo','Descripcion')


def imprimir(variables):
    for variable in variables:
        print('Input => "%s"' % variable.get())



def CrearFormModificar(root, campos):

    print("hole")
    formulario = Frame(root)
    div1 = Frame(formulario, width=100)
    div2 = Frame(formulario, padx=7, pady=2)
    formulario.pack(fill=X)
    div1.pack(side=LEFT)
    div2.pack(side=RIGHT, expand=YES, fill=X)
    variables = []
    
    for field in campos:
        lab = Label(div1, width=10, text=field)
        ent = Entry(div2, width=30, relief=SUNKEN)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        var.set('---')
        variables.append(var)
    return variables
    """    """
    

if __name__ == '__main__':
    root = Tk()
    vars_modifica = CrearFormModificar(root, campos)
    Button(root, text='Imprimir', command=(lambda: imprimir(vars_modifica))).pack(side=LEFT)
    Cerrar(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: imprimir(vars_modifica)))  
    root.mainloop()
