from tkinter import *


class MiApp:
    def __init__(self, parent=None, **configs):

        # ##################################################################
        # Defino parámetros
        # ##################################################################
        ancho_boton = 10

        # ##################################################################
        # Defino variables por defecto
        # ##################################################################
        self.temas = StringVar()
        self.temas.set("tema1")

        self.nombres = StringVar()
        self.nombres.set("VyH")

        self.side_option = StringVar()
        self.side_option.set(LEFT)

        self.fill_option = StringVar()
        self.fill_option.set(NONE)

        self.expand_option = StringVar()
        self.expand_option.set(YES)

        self.anchor_option = StringVar()
        self.anchor_option.set(N)

        # Agrego variables de contorl para eleccion de tema
        self.tema_option = IntVar(value=0)

        # ##################################################################
        # Ventana principal
        # ##################################################################
        self.my_parent = parent
        self.my_parent.geometry("700x600")

        # ##################################################################
        # Agrego contenedor
        # ##################################################################
        self.contenedor = Frame(self.my_parent, bg="#444")
        self.contenedor.pack(expand=YES, fill=BOTH)
        # ##################################################################
        # Agrego Secciones Principales
        # ##################################################################
        #####  CERRAR #####
        self.seccion_cerrar = Frame(
            self.contenedor, bg="#FF7F50", height=22, borderwidth=2, relief=RAISED
        )
        self.seccion_cerrar.pack(side=TOP, expand=NO, fill=X, padx=7)
        self.cerrar = Frame(self.seccion_cerrar, bg="#222", height=22)
        self.cerrar.pack(side=TOP, expand=NO, fill=X)

        #####  SECCIÓN CONTROLES #####
        self.seccion_controles = Frame(
            self.contenedor, bg="red", borderwidth=2, relief=RAISED
        )
        self.seccion_controles.pack(side=TOP, expand=NO, fill=BOTH, padx=7, pady=7)
        titulo_controles = "Controles"
        Label(
            self.seccion_controles,
            text=titulo_controles,
            bg="#222",
            fg="OrangeRed",
            justify=LEFT,
        ).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.controles = Frame(self.seccion_controles, bg="#222")
        self.controles.pack(side=TOP, expand=NO, fill=X)

        #####  SECCIÓN REPRESENTACIÓN #####
        self.seccion_representacion = Frame(
            self.contenedor, bg="red", borderwidth=2, relief=RAISED
        )
        self.seccion_representacion.pack(
            side=BOTTOM, expand=YES, fill=BOTH, padx=7, pady=7
        )
        titulo_grafico = "Representación gráfica"
        Label(
            self.seccion_representacion,
            text=titulo_grafico,
            bg="#222",
            fg="OrangeRed",
            justify=LEFT,
        ).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.representacion = Frame(self.seccion_representacion, bg="OrangeRed")
        self.representacion.pack(side=TOP, expand=YES, fill=BOTH)
        # ##################################################################
        # Controles
        # ##################################################################
        self.temas_opciones = Frame(self.controles, borderwidth=5, bg="#222")
        self.nombres_opciones = Frame(self.controles, borderwidth=5, bg="#222")
        self.side_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.fill_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.expand_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.anchor_contenedor = Frame(self.controles, borderwidth=5, bg="#222")

        self.temas_opciones.pack(side=LEFT, expand=NO, fill=Y, anchor=N)
        self.nombres_opciones.pack(side=LEFT, expand=YES, fill=Y, anchor=N)
        self.side_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.fill_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.expand_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.anchor_contenedor.pack(side=LEFT, expand=YES, anchor=N)

        Label(
            self.temas_opciones,
            borderwidth=4,
            relief=RAISED,
            text="Temas",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.nombres_opciones,
            borderwidth=4,
            relief=RAISED,
            text="Opciones",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.side_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Side",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.fill_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Fill",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.expand_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Expand",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.anchor_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Anchor",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)

        # ##################################################################
        # Representación
        # ##################################################################
        self.representacion_superior = Frame(self.representacion, bg="red")
        self.representacion_superior.pack(side=TOP, expand=YES, fill=BOTH)

        self.deslizador_central = Frame(
            self.representacion_superior,
            background="black",
            borderwidth=4,
            relief=SUNKEN,
            width=250,
        )
        self.deslizador_central.pack(side=LEFT, expand=YES, fill=BOTH)

        self.deslizador_vertical = Frame(
            self.representacion_superior,
            background="#FF7F50",
            borderwidth=4,
            relief=SUNKEN,
            width=50,
        )
        self.deslizador_vertical.pack(side=RIGHT, expand=NO, fill=Y)

        self.deslizador_horizontal = Frame(
            self.representacion, borderwidth=4, relief=SUNKEN, height=50, bg="OrangeRed"
        )
        self.deslizador_horizontal.pack(side=TOP, fill=X)
        # ##################################################################
        # Texto de botones parte gráfica
        # ##################################################################

        self.botonVyH = Button(self.deslizador_central, text="VyH")
        self.botonVyH.pack()
        self.botonV = Button(self.deslizador_vertical, text="V")
        self.botonV.pack()
        self.botonH = Button(self.deslizador_horizontal, text="H")
        self.botonH.pack()
        self.elegir_nombre_botones = {
            "VyH": self.botonVyH,
            "V": self.botonV,
            "H": self.botonH,
        }

        # ##################################################################
        # Nombres en controles
        # ##################################################################
        temas = ["tema1", "tema2", "tema3"]
        nombres = ["VyH", "V", "H"]
        side_options = [LEFT, TOP, RIGHT, BOTTOM]
        fill_options = [X, Y, BOTH, NONE]
        expand_options = [YES, NO]
        anchor_options = [NW, N, NE, E, SE, S, SW, W, CENTER]

        # Agrego opciones de colores para bg y fg
        self.bg_colors = ["#222", "blue", "OrangeRed"]

        # ##################################################################
        # Opciones de controles
        # ##################################################################

        for opcion in temas:
            boton = Radiobutton(
                self.temas_opciones,
                text=str(opcion),
                indicatoron=0,
                value=int(opcion[-1]) - 1,
                variable=self.tema_option,
                bg="#222",
                fg="OrangeRed",
                command=self.bg_fg_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in nombres:
            boton = Radiobutton(
                self.nombres_opciones,
                text=str(opcion),
                indicatoron=1,
                value=opcion,
                command=self.reseteo,
                variable=self.nombres,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in side_options:
            boton = Radiobutton(
                self.side_contenedor,
                text=str(opcion),
                indicatoron=0,
                value=opcion,
                command=self.actualizar,
                variable=self.side_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in fill_options:
            boton = Radiobutton(
                self.fill_contenedor,
                text=str(opcion),
                indicatoron=0,
                value=opcion,
                command=self.actualizar,
                variable=self.fill_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in expand_options:
            boton = Radiobutton(
                self.expand_contenedor,
                text=str(opcion),
                indicatoron=0,
                value=opcion,
                command=self.actualizar,
                variable=self.expand_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in anchor_options:
            boton = Radiobutton(
                self.anchor_contenedor,
                text=str(opcion),
                indicatoron=0,
                value=opcion,
                command=self.actualizar,
                variable=self.anchor_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        # ##################################################################
        # Botón de cancelar
        # ##################################################################
        self.cancelar = Button(self.cerrar, text="Cancel", background="red")
        self.cancelar.pack(side=BOTTOM, anchor=S)
        self.cancelar.bind("<Button-1>", self.cerrarApp)

    # ##################################################################
    # Destruir
    # ##################################################################
    def cerrarApp(self, event):
        self.my_parent.destroy()

    # ##################################################################
    # Defino función de reseteo
    # ##################################################################
    def reseteo(self):
        button = self.elegir_nombre_botones[self.nombres.get()]
        properties = button.pack_info()
        self.fill_option.set(properties["fill"])
        self.side_option.set(properties["side"])
        self.expand_option.set(properties["expand"])
        self.anchor_option.set(properties["anchor"])

    # ##################################################################
    # Defino función actualizar
    # ##################################################################
    def actualizar(self):
        button = self.elegir_nombre_botones[self.nombres.get()]
        button.pack(
            fill=self.fill_option.get(),
            side=self.side_option.get(),
            expand=self.expand_option.get(),
            anchor=self.anchor_option.get(),
        )

    def bg_fg_option(self):
        self.cerrar["bg"] = self.bg_colors[self.tema_option.get()]
        self.controles["bg"] = self.bg_colors[self.tema_option.get()]
        self.temas_opciones["bg"] = self.bg_colors[self.tema_option.get()]
        self.nombres_opciones["bg"] = self.bg_colors[self.tema_option.get()]
        self.side_contenedor["bg"] = self.bg_colors[self.tema_option.get()]
        self.fill_contenedor["bg"] = self.bg_colors[self.tema_option.get()]
        self.expand_contenedor["bg"] = self.bg_colors[self.tema_option.get()]
        self.anchor_contenedor["bg"] = self.bg_colors[self.tema_option.get()]
        self.representacion["bg"] = self.bg_colors[self.tema_option.get()]
        self.representacion_superior["bg"] = self.bg_colors[self.tema_option.get()]
        self.deslizador_central["bg"] = self.bg_colors[self.tema_option.get()]
        self.deslizador_vertical["bg"] = self.bg_colors[self.tema_option.get()]
        self.deslizador_horizontal["bg"] = self.bg_colors[self.tema_option.get()]


if __name__ == "__main__":
    root = Tk()
    MiApp(root)
    root.mainloop()
