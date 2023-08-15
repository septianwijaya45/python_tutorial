# Looping dari list
print("\n For Looping")

numbers = [4,7,6,2,3]

for i in numbers:
    print(f"Angka Ke-{i}")

participants = ["andi", "yudi", "ardi", "yono"]

for p in participants:
    print(f"Peserta :{p}")

# Looping dan range
print("\n For Looping dan range")

numbs = [9,11,293,19,55,42,15]

panjangNumbs = len(numbs)

for i in range(len(numbs)):
    print(f"Angka Ke-{i} : {numbs[i]}")

# While
print("\n While Loop")
numbs = [9,11,293,19,55,42,15]

panjangNumbs = len(numbs)
i = 0

while i < panjangNumbs:
    print(f"Angka Ke-{i} : {numbs[i]}")
    i += 1

# List Comprehension
print("\n List Comprehension")
data = ["andi", 11, "Yono", 39, "Udang", 21]

[print(f"Ini Data Ke-{i} => {data[i]}") for i in range(len(data))]

angka = [1,2,3,4,5]
angkaKuadrat = [i**2 for i in angka]
print(angkaKuadrat)


# enumerate
print("\n Enumerate")
dtList = ["andi", 11, "Yono", 39, "Udang", 21]

for index, data in enumerate(dtList):
    print(f"Index:{index} => {data}")
