''' DEFAULT ARGUMENT '''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya)

# contoh 1
def say_hello(nama = 'Lolo'):
    '''Fungsi dengan default argument'''
    print(f"Hallo {nama}")

say_hello('Nana')
say_hello()

# contoh 2
def sapa_dia(nama, pesan="Default Pesan"):
    '''Fungsi dengan satu input biasa. dan satu default pesan'''
    print(f"Hai {nama}, {pesan}")

sapa_dia('Anyi', 'Hallo')
sapa_dia('anya')

# contoh 3
def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

#contoh 4
def fungsi(i1 = 1, i2 = 2, i3 = 3, i4 = 4):
    hasil = i1 + i2 + i3 + i4
    return hasil

print(fungsi())
print(fungsi(i1=10))