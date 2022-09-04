# tipe data 1
# integer (angka satuan)

data_integer = 1
print(type(data_integer))
print("Data: ", data_integer, ", Bertipe: ", type(data_integer))

# tipe data 2
# float (angka dengan koma)

data_float = 1.5
print(type(data_float))
print("Data: ", data_float, ", Bertipe: ", type(data_float))

# tipe data 3
# string (kumpulan karakter)
data_string = "Budi"
print(type(data_string))
print("Data: ", data_string, ", Bertipe: ", type(data_string))

# tipe data 4
# biner atau boolean (true/false)
data_bool = False
print(type(data_bool))
print("Data: ", data_bool, ", Bertipe: ", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print(type(data_complex))
print("Data: ", data_complex, ", Bertipe: ", type(data_complex))

## tipe data dari bahasa C
from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.4)
print(type(data_c_double))
print("Data: ", data_c_double, ", Bertipe: ", type(data_c_double))