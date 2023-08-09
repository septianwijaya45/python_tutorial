# List di python => array di pemrograman lain

# kumpulan data numbers
dt_angka = [1,5,3,2]
print(dt_angka)

# kumpulan data string
dt_string = ['andi', 'ubin', 'adi']
print(dt_string)

# kumpulan data boolean
dt_boolean = [True, False, True]
print(dt_boolean)

# kumpulan campuran
dt_campuran = [1, 'bolang-baling', True, 2, 'Cireng', False]
print(dt_campuran)

# alternatif membuat list
dt_range = range(0,10,2) # start, stop, step
print(dt_range)
dt_range_list = list(dt_range)
print(dt_range_list)

# membuat list dengan for loop, LIST COMPHERENSIVE
dt_list_for = [i for i in range(1, 10)]
print(dt_list_for)


# membuat list dengan for loop berpangkat
dt_list_for = [i**2 for i in range(1, 10)]
print(dt_list_for)

# membuat list menggunakan for if
dt_list_for_if = [i for i in range(1,10) if i != 5] # angka 5 tidak ditampilkan
print(dt_list_for_if)

# membuat list menggunakan for if ganjil
dt_list_for_if_ganjil = [i for i in range(1,10) if i%2 != 0]
print(dt_list_for_if_ganjil)

# membuat list menggunakan for if genap
dt_list_for_if_genap = [i for i in range(1,10) if i%2 == 0]
print(dt_list_for_if_genap)