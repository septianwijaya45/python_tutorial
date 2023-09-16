from . import Database
from .Util import generatePrimary
import time
import os

def create():
    penulis = input("Penulis:\t")
    judul   = input("Judul: \t")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Harus Angka, Berformat YYYY!")
        except:
            print("Tahun Harus Angka, Berformat YYYY!")

    data = Database.TEMPLATE.copy()

    data["pk"] = generatePrimary(10)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"]  = penulis + Database.TEMPLATE["penulis"][len(penulis)]
    data["judul"]  = judul + Database.TEMPLATE["judul"][len(judul )]
    data["tahun"]  = str(tahun)

    dataNew = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"
    print(f"Data Baru: {dataNew}")

    try:
        with open(Database.DB_NAME, "w", encoding="UTF-8") as file:
            file.write(dataNew)
    except:
        print("Gagal Menyimpan Data!")    

def createData(penulis, judul, tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = generatePrimary(10)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"]  = penulis + Database.TEMPLATE["penulis"][len(penulis)]
    data["judul"]  = judul + Database.TEMPLATE["judul"][len(judul )]
    data["tahun"]  = str(tahun)

    dataNew = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"
    print(f"Data Baru: {dataNew}")   

    try:
        with open(Database.DB_NAME, "a", encoding="UTF-8") as file:
            file.write(dataNew)
    except:
        print("Gagal Menyimpan Data!") 


def read(**kwargs):

    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            jumlah = len(content)
            if "index" in kwargs:
                indexBuku = kwargs["index"] - 1
                if indexBuku < 0 or indexBuku > jumlah:
                    return False
                else:
                    return content[indexBuku]
            else:
                return content
    except:
        print("Gagal Membaca Data!")
        return False
    
def update(noBuku, pk, date, penulis, judul, tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date
    data["penulis"]  = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"]  = judul + Database.TEMPLATE["judul"][len(judul)]
    data["tahun"]  = str(tahun)

    dataNew = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"
    print(f"Data Update: {dataNew}")   

    dtLength = len(dataNew)
    try:
        with(open(Database.DB_NAME, "r+", encoding="UTF-8")) as file:
            file.seek(dtLength*(noBuku-1)) 
            file.write(dataNew)
    except:
        return False
    
def delete(noBuku):
    try:
        with open(Database.DB_NAME, 'r') as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == noBuku -1:
                    pass
                else:
                    with open("finalProject/data_temp.txt", 'a', encoding="UTF-8") as tempFile:
                        tempFile.write(content)
                content += 1
    except:
        print("Data Tidak Ditemukan!")

    os.rename("finalProject/data_temp.txt", Database.DB_NAME)