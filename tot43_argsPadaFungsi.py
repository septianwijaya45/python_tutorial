''' *args pada fungsi '''

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Budi", 172, 59)

def fungsi(dataList):
    data = dataList.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["Bina", 165, 55])
    

# Penggunaan ARGS

def orang(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

orang("Nana", 180, 60)

# studi kasus
def tambah(*data):
    # data tipenya tuple, bisa diiterasikan
    output = 0
    for angka in data:
        output += angka

    return output


hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil Penambahan: {hasil}")