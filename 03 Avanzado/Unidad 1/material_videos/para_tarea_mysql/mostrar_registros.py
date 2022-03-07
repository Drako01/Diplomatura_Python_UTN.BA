import re
def validar(cad):
    patron="^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
    try:
        print("------------------")
        print(cad)
        re.match(patron,cad)
        if(re.match(patron,cad)):
            return "true"
        else:
            return "false"
    except:
        return "false"
