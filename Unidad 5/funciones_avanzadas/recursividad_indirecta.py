# ##############################################
# Recursión ####
# ##############################################


def misuma(L):
    if not L:
        return 0
    return novacia(L)  # llama a otra función que llama a misuma


def novacia(L):
    return L[0] + misuma(L[1:])  # Recursividad indirecta

print(misuma([1.1, 2.2, 3.3, 4.4]))

input()