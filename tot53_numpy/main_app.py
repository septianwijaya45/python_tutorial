import numpy as np

listA = [1,2,3,4]
vectorA = np.array([1,2,3,4])

print(f"List A: {listA}")
print(f"Vector A: {vectorA}")

# jika dipangkatkan, akan error pada list
# print(f"List Pangkat: {listA**2}") <-- ERROR

print(f"Vector a pangkat 2: {vectorA**2}")
print(f"Vector a pangkat 3: {vectorA**3}")

# contoh matrix

matrixB = np.array([(1,2), (3,4)])
print(f"\nMatrix B: \n{matrixB}")
print(f"Matrix B Pangkat 2: \n{matrixB**2}")

zerosC = np.zeros((2,5))
print(f"\n Zeros C:\n{zerosC}")

onesD = np.ones((2,2))
print(f"\nOnes D: \n{onesD}")

jumlah = matrixB + matrixB**2 + onesD
print(f"\nJumlah Matrix:\n{jumlah}")

# numpy biasanya dibuat untuk data scientist