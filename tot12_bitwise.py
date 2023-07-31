"""
Operasi masing masing bit

ex: 2 => 0 0 0 0 0 1   0 0
         0 0 0 0 0 2^1 0 0 = 2

ex: 1 => 0 0 0 0 0 0 0 0
         0 0 0 0 0 0 0 2^0 = 1

ex: 9 => 0 0 0 0 1   0 0 1
         0 0 0 0 2^3 0 0 2^0 = 8 + 1 = 9

         dijumlahkan ke kanan


"""

# operator bitwise, operasi biner, binary

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n================= OR =================')
print('nilai:',a, ', binary :', format(a, '08b'))
print('nilai:',b, ', binary :', format(b, '08b'))
print('----------------------------------------')
print('nilai:',c, ', binary :', format(c, '08b'))

# bitwise AND (&)
c = a & b
print('\n================= AND ================')
print('nilai:',a, ', binary :', format(a, '08b'))
print('nilai:',b, ', binary :', format(b, '08b'))
print('----------------------------------------')
print('nilai:',c, ', binary :', format(c, '08b'))


# bitwise XOR (^)
c = a ^ b
print('\n================= XOR ================')
print('nilai:',a, ', binary :', format(a, '08b'))
print('nilai:',b, ', binary :', format(b, '08b'))
print('----------------------------------------')
print('nilai:',c, ', binary :', format(c, '08b'))


# bitwise NOT (~) (mirror angka)
"""
mirroring angka pada 2^0 akan bergeser ke bit 1, dan menjadi minus
ex: 9 => 00001001
menjadi
    -10 => -0001010
"""
c = ~a
print('\n================= NOT ================')
print('nilai:',a, ', binary :', format(a, '08b'))
print('----------------------------------------')
print('nilai:',c, ', binary :', format(c, '08b'))
d = 0b000001001
e = 0b111111111
print('nilai :', e^d, ', binary :', format(e^d, '08b'))

# shifting (bergeser)

# shift right (>>)
c = a >> 4
print('\n================= >> ================')
print('nilai:',a, ', binary :', format(a, '08b'))
print('nilai:',c, ', binary :', format(c, '08b'))
print('----------------------------------------')

# shift left (<<)
c = a << 2
print('\n================= << ================')
print('nilai:',a, ', binary :', format(a, '08b'))
print('nilai:',c, ', binary :', format(c, '08b'))
print('----------------------------------------')
