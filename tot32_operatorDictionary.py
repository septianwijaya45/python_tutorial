dtDict = {
    "Nama": "Agung Widodo",
    "Umur": 22,
    "Alamat": "Jl Ahmad Yani No 11, Surakarta"
}

LENDICT = len(dtDict)
print(f"\nPanjang data dictionary => {LENDICT}")

# cek key if exist
KEY = "Nama"
CHECKKEY = KEY in dtDict
print(f"Check Key => {CHECKKEY}")

# Mengakses value dengan get
print("\nAkses Menggunakan get()")
getDict = dtDict.get("Nama")
getDictNo = d~tDict.get("aaa", "key tidak ditemukan") # dengan message default
print(getDict)
print(getDictNo)

# Update Dictionary
dtDict["Nama"] = "Ahmad Agung Setiawan"
print("Data Setelah diubah\n",dtDict)
dtDict["Umur"] = 29
print("Data Setelah diubah\n",dtDict)

dtDict.update({"Umur": 32})
print("\nData Setelah diubah\n",dtDict)

# jika key tidak ada dalam dictionary, akan bertambah otomatis
dtDict.update({"Jenis Kelamin": "Laki-Laki"})
print("Data Setelah diubah\n",dtDict)