''' MEMBACA FILE EKSTERNAL '''

print(3*"=", " Membaca file txt ", 3*"=")
file = open("tot56_readExternalFile/data.txt", mode="r")

print(f"Status Read: {file.readable()}")
print(f"Status Write: {file.writable()}")

# membaca seluruh file
print(file.read())

# membaca per baris
# print(file.readline(), end="") # end untuk menghapus enter
# print(file.readline()) 
# print(file.readline())

# membaca semua text menjadi list
# print(file.readlines())

print(f"Apakah File Close: {file.closed}")
file.close()
print(f"Apakah File Close: {file.closed}")

## salah satu teknik membuka file python
print("\n")
print(3*"=", " Membaca file txt dengan with", 3*"=")

with open("tot56_readExternalFile/data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"Apakah File Close: {file.closed}")
    
print(f"Apakah File Close: {file.closed}")