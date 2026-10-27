# tugas 1 pola segitiga sama kaki
#input
n = int(input("Masukan jumlah baris(1-100): "))
karakter = input("Masukan karakter: ")

#proses dan output
for i in range(1,n + 1):
    spasi=" " * (n-i)
    bentuk = karakter *(2*i-1)
    print(spasi + bentuk)

print("==" * 35)


# tugas 2 : lagu anak ayam
n = int(input("Masukan jumlah anak ayam (1-100) :"))
#output awal
print("tek kotek kotek kotek anak ayam turun berkotek")
#proses menampilkan lagu
for i in range(n,0,-1):
    if i > 1 :
     print(f"anak ayam turunlah {i} mati satu tinggalah {i - 1}")
else :
    print("anak ayam turunlah 1, mati tinggallah induknya")