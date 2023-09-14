''' Type hints untuk fungsi '''

# bentuk standard fungsi
'''
def fungsi(parameter):  # akan bermasalah, karena parameter ini bertipe semua / any
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi('ucup')
fungsi(True)
'''

# penggunaan type hints

def fungsiWithHints(argument:int) -> int:
    output = argument**2
    return output

hasil = fungsiWithHints(2.3)
print(hasil)

def display(argument:str):
    print(argument)

display('Andia')

import os

hasil = os.system("cls")
print(hasil)

