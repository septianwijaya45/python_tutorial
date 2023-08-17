# looping dictionary

dtClient = {
    "Nama": "Agung Widodo",
    "Umur": 22,
    "Alamat": "Jl Ahmad Yani No 11, Surakarta",
    "Jenis Kelamin": "Laki-Laki"
}

# looping first (yang keluar hanya key)~
for data in dtClient:
    print(data)

# operator untuk mengambil iterable / item
print("="*10,"Pakai keys()","="*10)
key = dtClient.keys()
print("\n", key) # yang keluar hanya key saja

for key in dtClient.keys():
    print(dtClient.get(key))


print('\n',"="*10,"Pakai values()","="*10)
values = dtClient.values()
print(values)

for value in dtClient.values():
    print(value)


print('\n', "="*10,"Pakai items()","="*10)
item = dtClient.items()
print(item)

print('\n yang keluar key dan value dalam bentuk tuple')
for item in dtClient.items():
    print(item)

# bisa diakses menggunakan key dan value
print('\n')
for key, value in dtClient.items():
    print(f"Data Key:{key} => Valuenya: {value}")

