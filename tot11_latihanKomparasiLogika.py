# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3--------10++++++

inputUser = float(input("\nMasukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10: "))

# ++++++3----------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('Kurang Dari 3 = ', isKurangDari)

# ----------------10++++++
isLebihDari = (inputUser > 10)
print('Lebih dari 10 = ',isLebihDari)

# ++++++3--------10++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ", isCorrect)



# --------3++++++10--------
# Kasus irisan
print('\n=========== -----3+++++10----- ===========')
inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3\ndan\nlebih besar dari 10: "))


# -----3+++++
# lebih dari 3
isLebihDari = inputUser > 3
print('Lebih dari 3 = ', isLebihDari)

# +++++10-----
isKurangDari = inputUser < 10
print('Kurang dari 10 = ', isKurangDari)

# --------3++++++10--------
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan: ", isCorrect)



# ============================ PR ============================ #
print('\n-----0+++++5-----8+++++11-----')

inputUser = float(input("Masukkan angka yang bernilai diatas! : "))

# -----0+++++
isLebih1 = inputUser > 0
print('Lebih dari 0 = ', isLebih1)

# +++++5-----
isKurang1  = inputUser < 5
print('Kurang dari 10 = ', isKurang1)

# -----8+++++
isLebih2 = inputUser > 8
print('Lebih dari 8 = ', isLebih2)

# +++++11-----
isKurang2  = inputUser < 11
print('Kurang dari 11 = ', isKurang2)

# -----0+++++5-----8+++++11-----
isCorrect = (isLebih1 and isKurang1) or (isLebih2 and isKurang2)
print("Angka yang anda masukkan: ", isCorrect)