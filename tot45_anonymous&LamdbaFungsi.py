''' Lamdba function & Anonymous Function '''

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


