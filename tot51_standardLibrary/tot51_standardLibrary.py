# waktu
import datetime

waktu = datetime.datetime.now()
print(f"Waktu Sekarang: {waktu}")
print(f"Tahun: {waktu.year}")
print(f"Hari: {waktu.strftime('%A')}")

# pengelompokan data
from collections import Counter

'''
# Cara Biasa
data = ["a", "b", "c", "a", "d", "e"]

count = 0
for i in data:
    if i == "a":
        count += 1

print(f"Total angka a = {count}")
'''

#dengan counter 
data = ["a", "b", "c", "a", "d", "a"]
dtCounter = Counter(data)

print(f"Dictionary Pengelompokan: {dtCounter}")
print(f"Total A: {dtCounter['a']}")
print(f"Total B: {dtCounter['b']}")

# membaca file
import io

file = io.open("tot51_standardLibrary.txt", "r")
print(file.read())