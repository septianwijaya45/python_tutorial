print(30*"=")
print('Kalkulator Sederhana')
print(30*"=")

operator = input('Pilih Salah Satu Operator Berikut: \n1. +,\n2. -,\n3. *,\n4. /\n:')
angka1 = float(input('angka 1 = '))
angka2 = float(input('angka 2 = '))

if operator == '+':
    print(f"Hasil dari {angka1} + {angka2} = ", angka1+angka2)
elif operator == '-':
    print(f"Hasil dari {angka1} - {angka2} = ", angka1-angka2)
elif operator == '*':
    print(f"Hasil dari {angka1} * {angka2} = ", angka1*angka2)
elif operator == '/':
    print(f"Hasil dari {angka1} / {angka2} = ", angka1/angka2)
else:
    print("Operator Tidak Ditemukan!")
print("\nTerima Kasih")