def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        hasil_sementara = n * faktorial(n - 1)
        return hasil_sementara

n = int(input("Masukkan Nilai N : "))

for i in range(n, -1, -1) :
    print(f"{i}! = {faktorial(i)}")
