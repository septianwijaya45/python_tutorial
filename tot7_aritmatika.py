a = 10
b = 3

print('\n\n')

# operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian *
hasil = a * b
print(a, 'x', b, '=', hasil)

# operasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '^', b, '=', hasil)

# operasi modulus %
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi, operational precedence
# 1 ()
# 2 eksponen
# 3 *, /, %, //
# 4 + dan -
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', 'z', '//', x, '=', hasil)

print('\n')