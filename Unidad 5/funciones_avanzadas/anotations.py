# ##############################################
# Recursión ####
# ##############################################


from typing import Tuple


def func1(a, b, c):
    return a + b + c

print(func1(1, 2, 3))
print('',end='\n################\n' )


def func2(a: str, b: Tuple, c: float) -> int:
    return a + b + c


print(func2(1, 2, 3))
print(func2.__annotations__)
print('',end='\n################\n' )


def func3(a: str = 4, b: Tuple = 5, c: float = 6) -> int:
    return a + b + c

print(func3(1, 2, 3))
print(func3.__annotations__)
print('',end='\n################\n' )

input()