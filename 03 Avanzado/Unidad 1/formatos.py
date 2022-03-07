mi_string = "as"

print(mi_string.encode('ascii'))
print(mi_string.encode('latin1'))
print(mi_string.encode('utf8'))
print(mi_string.encode('utf16'))
print(mi_string.encode('utf32'))

var = b'\xff\xfe\x00\x00a\x00\x00\x00s\x00\x00\x00'
print(var.decode('utf32'))

print("\N{GREEK CAPITAL LETTER DELTA}")
print("\u0394")
print("\U00000394")

