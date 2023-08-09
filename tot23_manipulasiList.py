## operasi manipulasi list
'''
    Setiap list memiliki index yang dimulai dari 0
'''

data = ["ucup", "Otong", "Dading"]

# mengambil data dari list #
dt_0 = data[0]
dt_last = data[-1 ]
print(f"data pertama (index[0]): {dt_0} ")
print(f"data terakhir (index[0]): {dt_last} ")

# mengambil info jumlah data
length_data = len(data)
print(f"Panjang data adalah {length_data}")



######################## MANIPULASI DATA ########################
print(f"Data Sebelum Diubah: {data}")

# menambahkan item pada list sesuai posisi
data.insert(1, "Andi")
print(f"data ditambahkan di tengah: {data}")

# menambahkan item pada list terakhir
data.append("Indra")
print(f"data ditambah di terakhir: {data}")

# menambahkan list dengan list
dt_new = ["Kaisha", "Aris", "Dedy"]
data.extend(dt_new)
print(f"Data Gabungan List:  {data}")

# mengubah data berdasarkan posisi
data[2] = "Michele"
print(f"data ubah: {data}")

# menghapus data berdasarkan isi
data.remove('Dedy')
print(f"data setelah dihapus: {data}")

# menghapus data paling akhir
data.pop()
print(f"hapus data terakhir: {data}")