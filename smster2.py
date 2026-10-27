import numpy as np

print("KELOMPOK ")
print("Ilham Raditya Wibowo")
print("Fahri ")
print("Ajis")
print("Dede")
print("contoh array 1 dimensi\n\n")

# 1. Array Nilai Praktek (Tipe: INTEGER)
nilai_praktek = np.array([60, 70, 75, 80, 85, 90,])
print("1. Daftar nilai praktek :")
print(nilai_praktek)
print(f"nilai terbaik : {np.max(nilai_praktek)}\n")
print(f"nilai terkecil :{np.min(nilai_praktek)}\n") 



import numpy as np

print("KELOMPOK ")
print("Ilham Raditya Wibowo")
print("Fahri ")
print("Ajis")
print("Dede")
print("contoh array 2 dimensi\n\n")

#1. Array Matriks harga baju
# Baris = jenis baju, Kolom = ukuran

harga_baju = np.array ([
    [75000, 80000, 85000],   # Baju 1 (S, M, L)
    [90000, 95000, 100000],  # Baju 2 (S, M, L)
    [120000, 125000, 130000] # Baju 3 (S, M, L)
])
print(harga_baju)
print("Harga baju 2 ukuran M:", harga_baju[1][1])

