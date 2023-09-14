''' ***kwargs '''

def fungsi(nama, tinggi, berat):
    # Fungsi Biasa
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup", 180, 55)

def fungsi(**kwargs):
    nama=kwargs["nama"]
    tinggi=kwargs["tinggi"]
    berat=kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup", tinggi=180, berat=55) # dictionary type data


# case study
def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        print("Operasi Penjumlahan")
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        print("Operasi Perkali an")
        for angka in args:
            output *= angka
    else:
        print("Tidak Ada Operasi")

    return output

hasil = math(1,2,3,4,5,6,option="tambah")
print(f"Hasil Penjumlahan: {hasil}")

hasil = math(1,2,3,4,5,6,option="kali")
print(f"Hasil Perkalian: {hasil}")