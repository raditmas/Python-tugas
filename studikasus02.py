# deklarasi matriks 4x4
matriks = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

# isi matriks
for i in range(4):
    for j in range(4):
        if j <= i:  # isi angka sesuai baris
            matriks[i][j] = i+1
        else:
            matriks[i][j] = 0
# cetak matriks
for i in range(4):
    print(matriks[i])
