# contoh dari exception

from numbers import Number

def angka(a,b):
    if not isinstance(a, Number) and not isinstance(b, Number):
        print("ISIAN TIDAK BERUPA ANGKA!")
    return a+b

# print(angka(1,'2'))
print(angka(1,2))

angka = 0

try:
    hasil = 10/angka
except Exception as error_message:
    print(error_message)
print(angka)