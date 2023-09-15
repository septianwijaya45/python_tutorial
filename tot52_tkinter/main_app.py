''' GUI (Graphic User Interface) '''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()


#####=== WINDOW SETUP ===#####
window.configure(bg="white") # warna background
window.geometry("300x200") # ukuran program
window.resizable(False, False) # ukuran diperbesar x dan y dimatikan
window.title("Tutorial 52")
#####=== WINDOW SETUP ===#####

#####=== FUNGSI EKSEKUSI ===#####
def tombolClick():
    ''' Fungsi memanggil informasi ketika button klik '''
    getNamaDepan = NAMA_DEPAN .get()
    getNamaBelakang = NAMA_BELAKANG .get()
    pesan = f"Hallo {getNamaDepan} {getNamaBelakang}, Pinjem 100"
    showinfo(title="NJENG!", message=pesan)
#####=== FUNGSI EKSEKUSI ===#####

#####=== FRAME INPUT ===#####
inputFrame = ttk.Frame(window) # frame ini berada didalam window diatas
# Penempatan terdiri: Grid, Pack, Place

# paddingx, paddingy, posisi berada di horizontal (X), responsive true
inputFrame.pack(padx=10, pady=10, fill="x", expand=True)

# Komponen-komponen
# Label Nama Depan
lblNamaDepan = ttk.Label(inputFrame, text="Nama Depan: ")
lblNamaDepan.pack(padx=10, fill="x", expand=True)
# Entry Nama Depan
NAMA_DEPAN = tk.StringVar()
entryNamaDepan = ttk.Entry(inputFrame, textvariable=NAMA_DEPAN)
entryNamaDepan.pack(padx=10, fill="x", expand=True)

# Label Nama Belakang
lblNamaBelakang = ttk.Label(inputFrame, text="Nama Belakang: ")
lblNamaBelakang.pack(padx=10, fill="x", expand=True)
# Entry Nama Belakang
NAMA_BELAKANG = tk.StringVar()
entryNamaBelakang = ttk.Entry(inputFrame, textvariable=NAMA_BELAKANG)
entryNamaBelakang.pack(padx=10, fill="x", expand=True)
# Tombol
tombolSubmit = ttk.Button(inputFrame,text="Submit", command=tombolClick)
tombolSubmit.pack(padx=10, pady=15, fill="x", expand=True)
#####=== FRAME INPUT ===#####


#####=== BUKA PROGRAM ===#####
window.mainloop()
#####=== BUKA PROGRAM ===#####