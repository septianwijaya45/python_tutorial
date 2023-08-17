# copy
print('\n\n Copy')

dtClient = {
    "Nama": "Agung Widodo",
    "Umur": 22,
    "Alamat": "Jl Ahmad Yani No 11, Surakarta",
    "Jenis Kelamin": "Laki-Laki"
}

dtCopy = dtClient.copy()

print(f"data :{dtClient}")
print(f"data copy:{dtCopy}")

# jika diganti salah satu item maka tidak akan terpengaruh data ori karena .copy()
dtClient["Umur"] = 33
print("\nSetelah Diubah key Umur")
print(f"data :{dtClient}")
print(f"data copy:{dtCopy}")


# pop
# mengambil data berdasarkan key
print('\n\n POP')
dtPop = dtClient.pop('Alamat')
print(f"data :{dtClient}")
print(f"data copy:{dtPop}")

# popitem
# mengambil data terakhir

print('\n\n POP ITEM')
dtPop = dtClient.popitem()
print(f"data :{dtClient}")
print(f"data copy:{dtPop}")