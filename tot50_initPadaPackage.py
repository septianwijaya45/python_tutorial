import tot50_package
from tot50_package.matematika import tambah, kali, pangkatDua

# from tot50_package.matematika import tambah

hasilTambah = tambah(11, 22)
print(f"Hasil Tambah {hasilTambah}")

hasilFisika = tot50_package.fisika.gaya(11, 22)
print(f"Hasil Fisika: {hasilFisika}")


hasilPangkat = pangkatDua(2)(3)
print(f"Hasil Pangkat: {hasilPangkat}")

hasilKali = kali(11, 5)
print(f"Hasil Kali: {hasilKali}")


# tidak disarankan #
# from tot50_package import *
# from tot50_package.matematika import *

# hasilTambah = matematika.basic.tambah(11, 22)
# print(f"Hasil Tambah {hasilTambah}")

# hasilFisika = fisika.gaya(11, 22)
# print(f"Hasil Fisika: {hasilFisika}")

# hasilKali = matematika.basic.kali(11, 5)
# print(f"Hasil Kali: {hasilKali}")