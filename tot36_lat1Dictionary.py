import datetime
import os

template = {
    "nama"      : "nama",
    "nim"       : "nim",
    "sks_lulus" : 130,
    "beasiswa"  : 0,
    "lahir"     : datetime.datetime(1111,1,11)
}

dtMhs = {}

os.system('cls') # command untuk hapus isi terminal di windows
os.system('clear') # command untuk hapus isi terminal di mac os


print(f"{'SELAMAT DATANG': <20}")
print(f"{'DATA MAHASISWA': <20}")
print('-'*20)

# membuat dictionary dengan format template diatas
mhs = dict.fromkeys(template.keys())

mhs['nama'] = input('Nama Mahasiswa: ')
mhs['nim']  = input('NIM Mahasiswa: ')
mhs['sks_lulus'] = input('SKS Mahasiswa: ')
beasiswa  = input('Beasiswa (Yes/No): ')
mhs['beasiswa'] = 1 if beasiswa == 'yes' else 0
TGL_LAHIR = int(input('Tanggal Lahir (1-31): '))
BLN_LAHIR = int(input('Bulan Lahir (1-12): '))
TAHUN_LAHIR = int(input('Tahun Lahir(YYYY): '))
mhs['lahir'] = datetime.datetime(TAHUN_LAHIR, BLN_LAHIR, TGL_LAHIR)
print(mhs)