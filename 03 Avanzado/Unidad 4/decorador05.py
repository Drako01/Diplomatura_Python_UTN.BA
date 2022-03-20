def cambio_estado(f):
    def inner(*args, **kwargs):
        if args[0]:
            f(*args, **kwargs)
            print("El motor se ha encendido")
        else:
            f(*args, **kwargs)
            print("El motor se ha apagado")

    return inner


def aviso_cambio_estado(f):
    def inner(*args, **kwargs):
        print("Se envia un mensaje a dispositivo movil.")
        f(*args, **kwargs)
        print("Se ejecuto %s" % f.__name__)

    return inner


@cambio_estado
@aviso_cambio_estado
def estado_motor(estado):
    print(estado)


estado_motor(True)
print("---" * 20)
estado_motor(False)