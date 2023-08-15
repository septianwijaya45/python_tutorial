# program list buku

listBuku = [];
while True:
    print("\nMasukkan Data Berikut")
    judul = input("Masukkan Judul\t:")
    penulis = input("Masukkan Penulis\t:")

    bukuBaru = [judul, penulis]
    listBuku.append(bukuBaru)
    
    print("\n\n", "="*10, "List Data Bukuku", "="*10)
    for index, data in enumerate(listBuku):
        print(f"No: {index+1}  |  Judul: {data[0]}  |  Penulis:{data[1]}")
    
    con = input("Apakah Ingin Lanjut (Y/N)? ")
    
    if(con == "n" or con == "N" or con == "no"):
        break

print("Program Ended")