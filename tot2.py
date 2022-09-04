import time
start_time = time.time()

print('Hello World')

# cara run di terminal => python3 tot2.py

a = 10 # ini variabel
print(a);

"""
    Multiple Line
"""

# Compile python menggunakan bycode
# bycode : bentuk set instruksi yang dirancang untuk eksekusi yang efisien oleh penerjemah perangkat lunak
# jalankan code => python3 -m py_compile tot2.py
# masuk ke __pycache__
# jalankan code => python3 tot2.cpython-310.pyc

for i in range(1, 1000):
    print(i)

print(time.time() - start_time, "detik")