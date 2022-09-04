# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean
# >, <, >=, <=, !=, is, is not

print('\n\n')

a = 4
b = 2

# >
hasil = a > 3
print('===== > =====')
print(a, '>', 3, '=', hasil)

# <
hasil = a < b
print('===== < =====')
print(a, '<', b, '=', hasil)

# >=
hasil = a >= b
print('===== >= =====')
print(a, '>=', b, '=', hasil)

# <=
hasil = a <= b
print('===== <= =====')
print(a, '<=', b, '=', hasil)

# ==
print('===== == =====')
hasil = a == 4
print(a, '==', 4, '=', hasil)

# !=
print('===== != =====')
hasil = a != 4
print(a, '!=', 4, '=', hasil)

'''
    >, <, >=, <=, ==, !=    => termasuk syntax literal 
    is, is not              => membandingkan memory/object
'''

print('===== Object Identity (IS) =====')
# 'is' sebagai komparasi object identity
x = 5   # assignment membuat object
y = 5
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

x = 5   # assignment membuat object
y = 6
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)


print('===== Object Identity (IS NOT) =====')
x = 5   # assignment membuat object
y = 6
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)

print('\n\n')