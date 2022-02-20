import sys
try:
    my_list = [3,7, 9, 4, 6]
    print(my_list[6]) 
except IndexError as e:
    print(e)
    print(sys.exc_info())