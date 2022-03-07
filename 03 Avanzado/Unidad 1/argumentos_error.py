try: 
    print(b'\x80abc'.decode("utf-8", "strict"))
except UnicodeDecodeError:
    print("Ha existido un error en la decodificación")
    
print(b'\x80abc'.decode("utf-8", "replace"))
print(b'\x80abc'.decode("utf-8", "backslashreplace"))
print(b'\x80abc'.decode("utf-8", "ignore"))