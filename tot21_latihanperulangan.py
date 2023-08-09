# latihan perulangan membuat segitiga

sisi = 12

# 1 Menggunakan For #

# dummy variable
count = 1
for i in range(4):
    print("*"*count)
    count += 1
print('End of For 1')

# 2 Menggunakan While #
count = 1
while True:
    print("*"*count)
    count += 1

    if(count > sisi):
        break
print('End of While 1')

# 3. Bintang Ganjil #
count = 1
while True:
    # if(count % 2 != 0):
    #     print("*"*count)
    # count += 1

    if count%2:
        print("*"*count)
        count += 1
    else:
        count += 1
        continue

    if(count > sisi):
        break
print('End of While 3')

# 4. Segitiga Sama Kaki #
count = 1
spasi = int(sisi/2)
while True:
    if count%2:
        print(" "*spasi,"*"*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue 
    if(count > sisi):
        break
print('End of While 4')