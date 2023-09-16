from . import Operation

DB_NAME = "finalProject/data.txt"
TEMPLATE = {
    "pk": "XXXXX",
    "date_add": "YYYY-MM-DD",
    "judul": 255*" ",
    "penulis": 255*" ",
    "tahun": "YYYY"
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database Tersedia, Inisiasi Data...")
    except:
        print("Database Tidak Tersedia, Sedang Membuat...")
        with open(DB_NAME, "w", encoding="UTF-8") as  file:
            Operation.create()