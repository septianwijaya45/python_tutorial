# penambahan

def tambah(*args):
    hasil = 0
    for data in args:
        hasil += data
    return hasil

def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data
    return hasil

def pangkatDua(n:int):
    return lambda angka:angka**n