''' Fungsi dengan return '''

'''
def nama_fungsi(argumen):
    body function
    return output
'''

def kuadrat(input_angka):
    output = input_angka**2
    return output

y = kuadrat(3)
print(y)

print(kuadrat(7))

z = 10 + kuadrat(5)
print(z)

# pertambahan
def func_tambah(a,b):
    hasil = a+b
    return hasil


def operasi_matematika(angka1, angka2):
    tambah  = angka1 + angka2
    kurang  = angka1 - angka2
    bagi    = angka1 / angka2
    kali    = angka1 ** angka2

    return tambah, kurang, bagi, kali

tambah, kurang, bagi, kali = operasi_matematika(9, 5)

print(f"Hasil Tambah\t=> {tambah}")
print(f"Hasil Kurang\t=> {kurang}")
print(f"Hasil Bagi\t=> {bagi}")
print(f"Hasil Kali\t=> {kali}")
