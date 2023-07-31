# continue, pass, break

# pass -> berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass # tidak akan dieksekusi, atau tidak terjadi apa-apa

    print(angka)

"""
digunakan sebagai abaikan function, contoh
def angka():
    pass
"""

# ================== Continue ====================  #

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"Angka Sekarang: {angka}")

    if angka == 3:
        print('nice')
        continue # akan membuat loop meloncat ke atas

    print("black while")

print("finish")