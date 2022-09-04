# operasi logika
# not, or, and, xor

# not
from operator import xor


print('\n===== NOT =====')
a = True
c = not a
print('data a =', a)
print('---------- NOT')
print('data c =', c)

# or (Jika salah satu True, Hasil akan True)
print('\n===== OR =====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)


# AND (Jika semua True, Hasil akan True. Jika salah satu True, hasil False)
print('\n===== AND =====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)


# XOR (Jika semua True, Hasil akan FALSE. Jika salah satu True, hasil TRUE)
print('\n===== XOR =====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)