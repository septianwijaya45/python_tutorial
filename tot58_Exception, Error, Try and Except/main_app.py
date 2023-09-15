''' EXCEPTION '''

# exception akan terjadi saat program mengalami error saat runtime
# contoh sederhana

from math import nan

'''
inputUser = int(input("Masukkan Angka = "))
hasil = nan

try:
    hasil = 10/inputUser
except:
    print("Input Tidak Boleh 0!")

print(f"Hasil = {hasil}")
'''

# Contoh di aplikasi
'''
while(True):
    angka = int(input("Masukkan Angka = "))
    try:
        hasil = 10/angka
        print(f"Hasil => {hasil}")
        is_done = input("Lanjutkan (ketik y/n)? ")
        if is_done == "n":
            break
    except:
        print("Pembagi Nol! Silahkan Input Lagi")

print("Akhir dari program")
'''

# contoh membuat file
while(True):
    try:
        with open("tot58_Exception, Error, Try and Except/data.txt", "r") as file:
            print(file.read())
        break
    except:
        print("GAGAL! Sedang Dibuatkan File...")
        with open("tot58_Exception, Error, Try and Except/data.txt", "w", encoding="UTF-8") as file:
            file.write("new File")
        break
print("Akhir dari Program 2")