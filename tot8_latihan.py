# latihan konversi suhu

# program konversi celcius ke satuan lain
print('\nPROGRAM KONVERSI TEMPERATUR\n')

celcius = float(input('Masukkan suhu dalam celcius : '))
print('Suhu = ', celcius, 'Celcius')

# reamur
# (4/5) * C
reamur = (4/5) * celcius
print("Suhu Reamur adalah ", reamur, " Reamur")

# Fahrenheit
# 9/5 * celcius + 32
fahrenheit = ((9/5) * celcius) + 32
print("Suhu Fahrenheit adalah ", fahrenheit, " Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu Kelvin adalah ", kelvin, " Kelvin")