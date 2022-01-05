class AbueloPaterno(object):

    def __init__(self):
        print("AbueloPaterno")
        super(AbueloPaterno, self).__init__()


class AbueloMaterno(object):

    def __init__(self):
        print("AbueloMaterno")
        super(AbueloMaterno, self).__init__()


class Padre(AbueloPaterno):

    def __init__(self, arg):
        print("Padre", "arg = ", arg)
        super(Padre, self).__init__()


class Madre(AbueloMaterno):

    def __init__(self, arg):
        print("Madre", "arg = ", arg)
        super(Madre, self).__init__()


class Hijo(Padre, Madre):

    def __init__(self, arg):
        print("Hijo", "arg = ", arg)
        super(Hijo, self).__init__(arg)


objeto = Hijo("celeste")

input()
