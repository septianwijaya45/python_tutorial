data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0, data_1]
data_copy = data_2D.copy()

print(f"data : {data_2D}")
print(f"data copy: {data_copy}")

# address semua
print(f"address data : {hex(id(data_2D))}")
print(f"address data copy : {hex(id(data_copy))}")

print("Address dari member 1")
print(f"address data : {hex(id(data_2D[0]))}")
print(f"address data copy : {hex(id(data_copy[0]))}\n")

'''
Address akan sama, karena isi komponen tetap sama walaupun list di copy

menggunakan deepcopy
'''
from copy import deepcopy
data_2D = [data_0, data_1, 10]
data_copy = deepcopy(data_2D)

print("Address dari member 1")
print(f"address data : {hex(id(data_2D[0]))}") 
print(f"address data copy : {hex(id(data_copy[0]))}") #address akan berbeda


data_copy[1][0] = 11
print(f"data : {data_2D}")
print(f"data copy: {data_copy}") 