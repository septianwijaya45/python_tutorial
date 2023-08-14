# List Bersarang, list di dalam list

data_0 = [1, 2]
data_1 = [3, 4]

data_list_biasa = [1,2,3,4]

print(f"data list biasa => {data_list_biasa}")

# NESTED LIST 2D
list_2D = [data_0, data_1]
print(f"List 2D => {list_2D}")

# Contoh penggunaan nested list
peserta_0 = ["ucup", 25, "Pria"]
peserta_1 = ["miko", 35, "Wanita"]
peserta_2 = ["yanto", 10, "Pria"]

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f"List Peserta; {list_peserta}")

# menampilkan data list
print("Menampilkan data Nested List")

for peserta in list_peserta:
    print(f"Nama\t => {peserta[0]}")
    print(f"Umur\t => {peserta[1]}")
    print(f"Gender\t => {peserta[2]}\n")

# akan bermasalah apabila menggunakan .copy
list_copy = list_peserta.copy()
print(f"List Peserta Copy: {list_copy}\n")
peserta_0[0] = "Michael"
print(f"List Peserta Copy; {list_copy}\n")
print(f"List Peserta; {list_peserta}\n")
'''
akan berubah semuanya
Hal ini dikarenakan masih 1 reference dengan peserta_0 walaupun sudah diganto
'''