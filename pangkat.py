def pangkat(x,y):
 if y == 0:
  return 1
 else:
  hasil_sementara = x* pangkat(x,y -1)
  print(f"{x} pangkat {y}:{hasil_sementara}")
  return hasil_sementara

x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))

print()
for i in range (y, -1, -1) :
 print(f"{x} pangkat {i} = {x ** i}")



 