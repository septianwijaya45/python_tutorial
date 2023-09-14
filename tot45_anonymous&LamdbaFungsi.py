''' Lamdba function & Anonymous Function '''

# =============================== Lamdba function ========================== #
def f_kuadrat(angka):
    return angka**2

print(f"Hasil Fungsi Kuadrat: {f_kuadrat(3)}")


#### Lamdba Function  ###
# output = lambda argument: expression #
kuadrat = lambda angka:angka**2
print(f"Hasil dari lambda kuadrat: {kuadrat(11)}")

pangkat = lambda num,pow:num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

## Kegunaan Lambda Function ##
# sorting untuk list

dataList = ["Otong", "Ina", "Nani"]
dataList.sort()
print(f"Sorting using method: {dataList}")

'''
def panjangNama(nama):
    return len(nama)

dataList.sort(key=panjang_nama)
print(f"sorted list by panjang: {dataList}")
'''
# menggunakan lamdba
dataList.sort(key=lambda nama:len(nama))
print(f"Sorted list by Lambda: {dataList}")

# sort data berdasarkan panjang
dataList = ["Otong", "Ina", "Nani"]
def panjang_nama(nama):
    return len(nama)
dataList.sort(key=panjang_nama)
print(f"sorted list by panjang function:{dataList}")

# menggunakan lambda
dataList = ["Otong", "Ina", "Nani"]
dataList.sort(key=lambda nama:len(nama))
print(f"sorted list by panjang lamdba:{dataList}")

# filter
dataAngka = [1,2,3,4,5,6,7,8,9,10]

# ==== Kasus Kurang dari 5 ==== #
def kurangDariLima(angka):
    return angka < 5

angkaBaru = list(filter(kurangDariLima, dataAngka))
print(f"Angka Genap: {angkaBaru}")

# menggunakan lambda
angkaLamdba = list(filter(lambda x:x<5, dataAngka))
print(f"Angka Lamdba: {angkaLamdba}")
# ==== Kasus Kurang Dari 5 ==== #

# ==== Kasus Genap ==== #
dtGenap = list(filter(lambda x:(x%2 == 0), dataAngka))
print(f"Angka Genap Lamdba {dtGenap}")
# ==== Kasus Genap ==== #

# ==== Kasus Ganjil ==== #
dtGanjil = list(filter(lambda x:(x%2 != 0), dataAngka))
print(f"Angka Ganjil Lamdba {dtGanjil}")
# ==== Kasus Ganjil ==== #

# ==== Kasus Kelipatan 3 ==== #
dtGanjil = list(filter(lambda x:(x%3 == 0), dataAngka))
print(f"Angka Kelipatan 3 Lamdba {dtGanjil}")
# ==== Kasus Kelipatan 3 ==== #
# =============================== Lamdba function ========================== #


# =============================== Anonymous function ========================== #
print('\n')
# disebut currying function

# contoh biasa
def pangkat(angka, n):
    hasil = angka**n
    return hasil

dataHasil = pangkat(5,3)
print(f"hasil perpangkatan dengan function biasa: {dataHasil}")

#dengan lambda
def pangkatLambda(n):
    return lambda angka:angka**n

pangkatLambda2 = pangkatLambda(2)
print(f"Hasil dari pangkat 2: {pangkatLambda2(5)}")
pangkatLambda3 = pangkatLambda(3)
print(f"Hasil dari pangkat 3: {pangkatLambda3(5)}")
print(f"Hasil dari pangkat bebas: {pangkatLambda(5)(2)}")

# =============================== Anonymous function ========================== #