print(" PROGRAM OPERASI MATRIKS 3x3 Penjumlahan") 
print(" ---------------------------------------------------------")
print(" Nama  : Ilham Raditya Wibowo")
print(" NIM   : 17250028")
print(" Kelas : 17-1A-01")
print(" ---------------------------------------------------------")

# Matriks A (3x3)
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matriks B (3x3)
B = [
    [9, 8, 7],
    [6, 5, 4],
    [4, 3, 2]
]

# Matrik hasil penjumlahan (C = A + B)
C = [[0 for j in range(3)] for i in range(3)]

# Proses penjumlahan
for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

# Menampilkan matriks
print("Matriks A:")
for row in A:
    print(row)

print("\nMatriks B:")
for row in B:
    print(row)

print("\nHasil Penjumlahan Matriks (A + B):")
for row in C:
    print(row)