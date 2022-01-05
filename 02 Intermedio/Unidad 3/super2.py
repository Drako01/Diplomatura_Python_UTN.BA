class AbueloPaterno(object):

    def __init__(self, *args, **kwargs):
        print("AbueloPaterno")
        super(AbueloPaterno, self).__init__(*args, **kwargs)


class AbueloMaterno(object):

    def __init__(self, *args, **kwargs):
        print("AbueloMaterno")
        super(AbueloMaterno, self).__init__(*args, **kwargs)


class Padre(AbueloPaterno):

    def __init__(self, arg, *args, **kwargs):
        print("Padre", "arg = ", arg)
        super(Padre, self).__init__(arg, *args, **kwargs)


class Madre(AbueloMaterno):

    def __init__(self, arg, *args, **kwargs):
        print("Madre", "arg = ", arg)
        super(Madre, self).__init__(*args, **kwargs)


class Hijo(Padre, Madre):

    def __init__(self, arg, *args, **kwargs):
        print("Hijo", "arg = ", arg)
        super(Hijo, self).__init__(arg, *args, **kwargs)


objeto = Hijo("celeste")



input()
