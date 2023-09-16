from . import Operation

def readConsole():
    readData = Operation.read()
    
    index="No"
    judul="Judul"
    penulis="Penulis"
    tahun="Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # Data
    for index, data in enumerate(readData):
        dtSplit = data.split(',')
        pk = dtSplit[0]
        date = dtSplit[1]
        penulis = dtSplit[2]
        judul = dtSplit[3]
        tahun = dtSplit[4]

        print(f"{index+1:4} | {judul:40} | {penulis:40} | {tahun:4}\n", end="")

    # Footer
    print("="*100+"\n")

def createConsole():
    print("\n\n"+"="*100)
    print("Silahkan Tambah Data Buku\n")

    penulis = input("Penulis\t: ")
    judul   = input("Judul\t: ")

    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Harus Angka, Berformat YYYY!")
        except:
            print("Tahun Harus Angka, Berformat YYYY!")

    Operation.createData(penulis, judul, tahun)
    print("\nSukses Mengimputkan Data!")
    readConsole()

def updateConsole():
    readConsole()
    while(True):
        print("\Pilih Nomor yang Akan Di Update!")
        noBuku = int(input("Nomor Buku\t: "))
        dtBuku = Operation.read(index=noBuku)

        if dtBuku:
            break
        else:
            print("Nomor Tidak Valid!") 

    dtSplit = dtBuku.split(',')
    pk = dtSplit[0]
    date = dtSplit[1]
    penulis = dtSplit[2] 
    judul = dtSplit[3]
    tahun = dtSplit[4]

    while(True):
        print("\n"+"="*100)
        print("Pilih Data yang Diubah!")
        print(f"1. Judul \t: {judul}")
        print(f"2. Penulis \t: {penulis}")
        print(f"3. Tahun \t: {tahun}")

        optionUser = input("Pilih Data\t: ")
        print("\n"+"="*100)
        match optionUser:
            case "1":
                judul = input("Masukkan Judul Baru\t: ")
            case "2":
                penulis = input("Masukkan Penulis Baru\t: ")
            case "3":
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun Harus Angka, Berformat YYYY!")
                    except:
                        print("Tahun Harus Angka, Berformat YYYY!")
            case _:
                print("Index Tidak Cocok!")

        isDone = input("Apakah Anda Ingin Selesai Update Data (Y/N)? ")
        if isDone == "y" or isDone == "Y" or isDone == "yes" or isDone == "Yes":
            break
    
    Operation.update(noBuku, pk, date, penulis, judul, tahun)

def deleteConsole():
    readConsole()
    while(True):
        print("\Pilih Nomor yang Akan Di DELETE!")
        noBuku = int(input("Nomor Buku\t: "))
        dtBuku = Operation.read(index=noBuku)

        if dtBuku:
            dtSplit = dtBuku.split(',')
            pk = dtSplit[0]
            date = dtSplit[1]
            penulis = dtSplit[2] 
            judul = dtSplit[3]
            tahun = dtSplit[4]

            print("\n"+"="*100)
            print("Pilih Data yang Dihapus!")
            print(f"1. Judul \t: {judul}")
            print(f"2. Penulis \t: {penulis}")
            print(f"3. Tahun \t: {tahun}")

            isDone = input("Apakah Anda Yakin Delete Data (Y/N)? ")
            if isDone == "y" or isDone == "Y" or isDone == "yes" or isDone == "Yes":   
                Operation.delete(noBuku)
                break 
        else:
            print("Nomor Tidak Valid!")
    print("Data Berhasil Dihapus")