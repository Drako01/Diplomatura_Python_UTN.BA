u = chr(40960) + 'abcd'
print(u)
print(u.encode('utf-8'))
try:
    print(u.encode('ascii'))
except UnicodeEncodeError:
    print('Se ha dado un error en la codificación')
    
print(u.encode('ascii', 'ignore'))
print(u.encode('ascii', 'replace'))
print(u.encode('ascii', 'xmlcharrefreplace'))
print(u.encode('ascii', 'backslashreplace'))
print(u.encode('ascii', 'namereplace'))
