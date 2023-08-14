## mengcopy list

a = ["andi", "noah", "deda"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# mengubah salah satu data, apa yang terjadi
a[1] = "michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}") 
# code diatas akan berubah walaupun menggunakan beda variable, berikut address pada 2 variable
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

'''
Menduplikat data list tanpa mengubah semua yang ada dikedua variable
menggunakan method copy()
'''

# Menduplikasi menggunakan copy()
print("\nMemcopy data menggunakan copy()")
c = a.copy()
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address b = {hex(id(c))}") #address akan berbeda

print("ubah data pada index 0")
c[0] = "Yahud"
print(f"a = {a}")
print(f"b = {b}") 
print(f"Data C Setelah Diubah: {c}")
