# operasi ditambah dengan assignment

a = 5 # adalah assignment
print('nilai a =', a)

a += 1
print('nilai a += 1, nilai a =', a)

a -= 2
print('nilai a -= 2, nilai a =', a)

a *= 5
print('nilai a *= 5, nilai a =', a)

a /= 2
print('nilai a /= 2, nilai a = ', a)


b = 10
print('\nNilai b = ', b)

b %= 3
print('nilai a %= 3, nilai b = ', b)


b = 10
b //= 3
print('nilai b //= 3, nilai b = ', b)

a = 5
print('\nNilai a =', a)
a **= 3
print('nilai a**=3, nilai a menjadi', a)



# operasi bitwise
# OR |
c = True
print('\nNilai c = ', c)
c |= False
print('nilai c |= False, nilai c menjadi = ', c)

c = False
print('\nNilai c = ', c)
c |= False
print('nilai c |= False, nilai c menjadi = ', c)

# AND &
c = True
print('\nNilai c = ', c)
c &= False
print('nilai c &= False, nilai c menjadi = ', c)

c = False
print('\nNilai c = ', c)
c &= False
print('nilai c &= False, nilai c menjadi = ', c)

# XOR ^
c = True
print('\nNilai c = ', c)
c ^= False
print('nilai c ^= False, nilai c menjadi = ', c)

c = True
print('\nNilai c = ', c)
c ^= True
print('nilai c ^= True, nilai c menjadi = ', c)

c = False
print('\nNilai c = ', c)
c ^= False
print('nilai c ^= False, nilai c menjadi = ', c)

# geser 
d = 0b0100
print('\nNilai d = ', format(d, '04b'))
d >>= 2
print('nilai d >>=2, nilai d menjadi', format(d, '04b'));
d <<= 1
print('nilai d <<=1, nilai d menjadi', format(d, '04b'));
