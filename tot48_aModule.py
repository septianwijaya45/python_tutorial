''' Module '''

# import biasa
'''
import tot48_matematika as mtk

tambah = mtk.tambah(1,3,4,2,1)
print(f"Hasil tambah: {tambah}")

kali = mtk.kali(1,2,3)
print(f"Hasil kali: {kali}")

pangkat = mtk.pangkatDua(2)(9)
print(f"Hasil Pangkat2: {pangkat}")
'''

# import from
from tot48_matematika import tambah, kali #, pangkatDua
# atau
### from tot48_matematika import * # TIDAK direkomendasikan, semua terimport
# pakai alias
from tot48_matematika import pangkatDua as kuadrat

tambah = tambah(1,3,4,2,1)
print(f"Hasil tambah: {tambah}")

kali = kali(1,2,3)
print(f"Hasil kali: {kali}")

pangkat = kuadrat(2)(9)
print(f"Hasil Pangkat2: {pangkat}")