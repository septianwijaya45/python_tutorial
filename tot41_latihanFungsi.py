''' Latihan Fungsi '''

import os

# program menghitung luas dan keliling persegi panjang

# membuat header program
def header():
    ''' FUNGSI HEADER '''
    os.system('clear')
    #os.system('cls)

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-':^40}")


def inputUser():
    LEBAR = int(input("Masukan Nilai Lebar: "))
    PANJANG = int(input("Masukkan Nilai Panjang: "))
    
    return LEBAR, PANJANG

def hitungLuas(p, l):
    ''' HITUNG LUAS '''
    LUAS = p * l
    return LUAS

def hitungKeliling(p, l):
    ''' HITUNG KELILING '''
    KELILING = 2*(p+l)
    return KELILING

def display(message, value):
    ''' FUNGSI DISPLAY '''
    print(f"Hasil Perhitungan {message}: {value}")

while True:
    header()

    LEBAR, PANJANG = inputUser()
    LUAS = hitungLuas(PANJANG, LEBAR)
    KELILING = hitungKeliling(PANJANG, LEBAR)

    display("LUAS PERSEGI PANJANG", LUAS)
    display("KELILING PERSEGI PANJANG", KELILING)

    isContinue = input("Apakah Lanjut (y/n)? ")
    if isContinue == 'n' or isContinue == "N":
        break

print('Program Berakhir')

