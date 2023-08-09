dt_angka = [1,2,1,3,4,2,6,4,5,9]

print(f"Awal Data Angka: {dt_angka}")


# count data berdasarkan isi
tot_dt_4 = dt_angka.count(4)
tot_dt_1 = dt_angka.count(5)

print(f"jumlah angka ke-4 : {tot_dt_4}")
print(f"jumlah angka ke-1 : {tot_dt_1}")

# mengambil posisi data
data = ["ucup", "Otong", "Dading"]
print(f"Data Nama: {data}")

index_ucup = data.index("ucup")
index_otong = data.index("Otong")
print(f"Posisi Ucup: {index_ucup}")
print(f"Posisi Otong: {index_otong}")

# mengurutkan data
dt_angka.sort()
data.sort()
print(f"uruttan data angka: {dt_angka}") 
print(f"uruttan data: {data}")

# membalikkan data
dt_angka.reverse()
data.reverse()
print(f"reverse data angka: {dt_angka}") 
print(f"reverse data: {data}")