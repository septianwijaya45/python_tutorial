# Casting
# Mengubah dari satu tipe ke tipe lain
# tipe data = int, float, str, bool

########## INTEGER ##########
print('=====  INTEGER  =====');
data_int = 9
# data_int = 0 # data bool akan false
print("data = ", data_int, "\ntipe =", type(data_int))

# int to float
data_float = float(data_int)
print("data = ", data_float, "\ntipe =", type(data_float))
# int to string
data_str = str(data_int)
print("data = ", data_str, "\ntipe =", type(data_str))
# int to bool
data_bool = bool(data_int) # akan false jika nilai float
print("data = ", data_bool, "\ntipe =", type(data_bool))


########## FLOAT ##########
print('=====  FLOAT  =====');
data_float = 0
print("data = ", data_float, "\ntipe =", type(data_float))

# int to float
data_int = int(data_float) # akan dibulatkan ke bawah
print("data = ", data_int, "\ntipe =", type(data_int))
# int to string
data_str = str(data_float)
print("data = ", data_str, "\ntipe =", type(data_str))
# int to bool
data_bool = bool(data_float) # akan false jika nilai float
print("data = ", data_bool, "\ntipe =", type(data_bool))


########## BOOLEAN ##########
print('=====  BOOLEAN  =====');
data_boolean = False
print("data = ", data_boolean, "\ntipe =", type(data_boolean))

# int to float
data_int = int(data_boolean) # akan dibulatkan ke bawah
print("data = ", data_int, "\ntipe =", type(data_int))
# int to string
data_str = str(data_boolean)
print("data = ", data_str, "\ntipe =", type(data_str))
# int to bool
data_float = float(data_boolean) # akan false jika nilai float
print("data = ", data_float, "\ntipe =", type(data_float))


########## STRING ##########
print('=====  STRING  =====');
#data_str = "Budi"
# data_str = "10"
data_str = "False"
print("data = ", data_str, "\ntipe =", type(data_str))

# int to float
data_int = int(data_str) # String harus angka
print("data = ", data_int, "\ntipe =", type(data_int))
# int to string
data_float = float(data_str) # String harus angka
print("data = ", data_float, "\ntipe =", type(data_float))
# int to bool
data_bool = bool(data_str) # akan false jika nilai float
print("data = ", data_bool, "\ntipe =", type(data_bool))