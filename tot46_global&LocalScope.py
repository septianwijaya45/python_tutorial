''' Global & Local Scope '''

# ====================== GLOBAL SCOPE ====================== #

namaGlobal = "Pandit~"  # <- global scope

# Akses variabel global dalam fungsi
def fungsi():
    print(f"Fungsi menampilkan {namaGlobal}")

fungsi()

# akses variabel global dalam loop

for i in range(0,5):
    print(f"ke-{i} - {namaGlobal}")

# Percabangan
if True:
    print(f"Percabangan {namaGlobal}")

# ====================== GLOBAL SCOPE ====================== #


# ====================== LOCAL SCOPE ====================== #
def fungsi2():
    namaLocal = "Andi"

fungsi2()
# print(f"Variabel Local {namaLocal}") #akan error

# ====================== LOCAL SCOPE ====================== #


## Contoh  1
def sayBudi():
    print(f"Hallo Kamu {nama}")

# sayBudi() # akan error, karena deklarasi setelah pemanggilan fungsi
nama = "budi"
sayBudi()

## Contoh  2
angka = 0
nama = "andi"

def angkaUbah(new, newNama):
    global angka, nama # ini akan mengubah isi angka, jika tidak digunakan tidak terjadi apa2
    angka=new
    nama=newNama

print(f"Sebelum diubah: {angka} - {nama}")
angkaUbah(4, "Odang")
print(f"Setelah diubah: {angka} - {nama}")

# Contoh 3
angka = 0

for i in range(0, 5):
    angka += i
    angkaDummy = 0

print(angka)
print(angkaDummy)

if True:
    angka = 10
    angkaDummy = 10

print(angka)
print(angkaDummy)