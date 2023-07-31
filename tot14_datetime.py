# Date and Time 
import datetime as dt

# contoh
"""
hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2023,7,30)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")
"""

print("Silahkan masukkan tanggal, Bulan dan tahun\n")
tanggal = int(input('Tanggal\t\t:'))
bulan   = int(input('Bulan\t\t:'))
tahun   = int(input('Tahun\t\t:'))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
today = dt.date.today()
umur_hari = today - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30

print(f"Tanggal Lahir Anda: {tanggal_lahir}")
print(f"Tanggal Lahir Anda: {tanggal_lahir:%A}")
print(f"Umur Anda (Hari):{umur_hari}")
print(f"Umur Anda (Tahun):{umur_tahun}")
print(f"Umur Anda (Bulan):{umur_bulan}")