#Kodingan Program
#deklarasi matrik 4x4
matriks=([0,0,0,0],[0,0,0,0],[0,0,
0,0],[0,0,0,0])
#isi matriks 4x4
for i in range(4):
  for j in range(4):
   if i==j:
    matriks[i][j]= "X"
   if i<j:
    matriks[i][j]= "A"
   if i>j:
    matriks[i][j]= "B"
#cetak bentuk matriks
for i in range(4): 
    print("   ".join(matriks[i]))