''' Fungsi dengan argumen (input) '''
'''

def name_function(argument):
    body function

'''

def helloWorld(nama):
    print(f"Selamat Datang Dunia Wahai {nama}")

helloWorld('Anjaini')

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"Hasil Pertambahan {angka1} + {angka2} = {hasil}")

tambah(1,55)

def arrayFunction(listArray):
    listArray[1] = 'Ara'
    peserta = listArray.copy()
    for anggota in peserta:
        print(f"\nPeserta yang masuk => {anggota}")

anggota = ['Dicky', 'Ian', 'Budi', 'Andi']
arrayFunction(anggota)
