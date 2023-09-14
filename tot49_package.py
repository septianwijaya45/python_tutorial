''' PACKAGE SEDERHANA '''
# import time

# t_start = time.time()
import tot49_packageModule.matematika # cara 1
# from tot49_packageModule import fisika # cara 2
from tot49_packageModule.fisika import gaya # cara 3

tambah = tot49_packageModule.matematika.tambah(1,3,4,2,1)
print(f"Hasil tambah dari package: {tambah}")

# gaya = fisika.gaya(10, 11)
# print(f"Gaya : {gaya}")

gaya = gaya(15, 11)
print(f"Gaya : {gaya}")

# t_end = time.time()
# print(f"Import Module Time: {t_end - t_start}")