''' __main__ '''

# Merupakan Gerbang Utama/Top level code enviroment
# __name__ == "__main__" jika ada di program utama

## __name__ pada file utama
print(f"Nama file pada main_app.py: '{__name__}'")

## __name__ pada file external
import fungsi 


# contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a=int, b=int) -> int:
    return a+b

if __name__ == "__main__":
    a1 = 45
    a2 = 11
    hasil = fungsi_tambah(a1, a2)
    print(f"\nHASIL: {hasil}")

## import package
import package