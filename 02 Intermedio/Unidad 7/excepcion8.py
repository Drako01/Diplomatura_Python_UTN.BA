import os
import datetime


class RegistroLogError(Exception):

    ruta = os.path.dirname(os.path.abspath(__file__)) + "\\log.txt"

    def __init__(self, linea, archivo, fecha):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha

    def registrar_error(self):
        log = open(self.ruta, "a")
        print("Se ha dado un error:", self.archivo, self.linea, self.fecha, file=log)


def registrar():
    raise RegistroLogError(7, "archivo1.txt", datetime.datetime.now())


try:
    registrar()
except RegistroLogError as log:

    log.registrar_error()
