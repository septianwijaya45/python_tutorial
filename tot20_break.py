# Break

angka = 0

# while angka < 5:
while True:
    angka += 1
    print(f"angka sekarang => {angka}")

    if angka == 3:
        break # akan stop disini, karena dihentikan

    print('runn')

print('Final Print')

# CONTOH 2 #

number = 0
input_user = int(input('Masukkan Angka: '))

while True:
    number += 1
    print(f"angka sekarang => {number}")

    if number == input_user:
        break

    print('runn')

print('Final Print')