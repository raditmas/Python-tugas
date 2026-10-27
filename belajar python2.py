# Tugas Mandiri Menghitung sisa uang ibu

#input
berat_telur = 5                     # kg
harga_perkg = 26000                 # rupiah per kg
ongkos = 3500 * 2                   # pulang pergi
uang_ibu = 200000                   # total uang yang dibawa

#proses
total_harga_telur = berat_telur * harga_perkg
total_pengeluaran = total_harga_telur + ongkos
sisa_uang = uang_ibu - total_pengeluaran

#output
print("total harga telur :", total_harga_telur)
print("ongkos pulang pergi :", ongkos)
print("total pengeluaran :", total_pengeluaran)
print("sisa uang ibu :", sisa_uang)