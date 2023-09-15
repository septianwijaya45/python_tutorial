''' WRITE FILE '''

# Akan membuat file baru jika tidak ada
# Jika ada, akan menimpa atau overwrite. Solusi adalah append jika ingin ditambahkan

with open("tot57_writeExternalFile/data.txt", "w", encoding="UTF-8") as file:
    file.write("IAN WIJAYA")

with open("tot57_writeExternalFile/data.txt", "w", encoding="UTF-8") as file:
    file.write("KETIMPA GAES")

# APPEND
with open("tot57_writeExternalFile/data2.txt", "w", encoding="UTF-8") as file:
    file.write("IAN\n")
with open("tot57_writeExternalFile/data2.txt", "a", encoding="UTF-8") as file:
    file.write("IWN\n")
with open("tot57_writeExternalFile/data2.txt", "a", encoding="UTF-8") as file:
    file.write("WAN\n")

# MODE r+
with open("tot57_writeExternalFile/data3.txt", "w", encoding="UTF-8") as file:
    file.write("IAN\n")
with open("tot57_writeExternalFile/data3.txt", "r+", encoding="UTF-8") as file:
    file.write("BARIS-1 \n")
    file.write("BARIS-2 \n")
    file.write("BARIS-3 \n")


with open("tot57_writeExternalFile/data3.txt", "r+", encoding="UTF-8") as file:
    data = file.read()
    print(data)

with open("tot57_writeExternalFile/data3.txt", "r+", encoding="UTF-8") as file:
    file.write("AHAAHAHA \n")