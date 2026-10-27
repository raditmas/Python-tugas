import os
from datetime import datetime

from numpy import transpose

#==============================================
# Path Folder Aplikasi
#==============================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#===============================================
# Fungsi Data Akun
#===============================================
def load_akun():
    path = os.path.join(BASE_DIR, "akun.txt")
    if not os.path.exists(path):
        return{}
    akun = {}
    with open(path, "r") as f:
        for line in f :
            if "," in line :
                user, pwd = line.strip().split(",",1)
                akun[user] = pwd
    return akun 

def simpan_akun(username,pasword):
    path = os.path.join(BASE_DIR, "akun.txt") 
    with open(path, "a") as f :
        f.write(f"{username},{pasword}\n")

#===================================================
# Fungsi Data Barang
#===================================================
def load_barang():
    path = os.path.join(BASE_DIR, "barang.txt")
    if not os.path.exists(path):
        return{}
    barang = {}
    with open(path, "r") as f :
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                kode, nama, harga = parts
                try:
                    barang[kode.upper()] = (nama, int(harga))
                except:
                    pass
    return barang     

def simpan_barang(barang):
    path = os.path.join(BASE_DIR, "barang.txt")
    with open(path, "w") as f :
        for kode in sorted(barang.keys()):
            nama, harga = barang[kode]
            f.write(f"{kode}, {nama}, {harga}\n")

#=================================================
#  Fungsi Transaksi
#=================================================
def simpan_transaksi(username, keranjang, total_awal, diskon, ppn, total_akhir, bayar, kembali):
    path = os.path.join(BASE_DIR, "transaksi.txt")
    with open(path, "a") as f:
        f.write("=== TRANSAKSI ===\n")
        f.write(f"Tanggal   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Kasir     : {username}\n")
        for item, harga, qty in keranjang:
            f.write(f"{item} - {harga} x {qty} = Rp{harga*qty}\n")
        f.write(f"Total awal    : Rp{total_awal}\n")
        f.write(f"Diskon        :-Rp{diskon}\n")
        f.write(f" PPN          :+Rp{ppn}\n")
        f.write(f"Total akhir   : Rp{total_akhir}\n")
        f.write(f"Bayar         : Rp{bayar}\n")
        f.write(f"Kembali       : Rp{kembali}\n")
        f.write("===========================\n\n")

#====================================================
# PROSES LOGIN (langsung transaksi setelah login)
#====================================================
def login():
    akun = load_akun()

    print("\n=== LOGIN KASIR ===")
    while True :
        username = input("Username :")
        pasword  = input("Pasword  :")

        if username in akun and akun[username] == pasword:
                print("\n ✅ login berhasil!\n")
                transaksi(username) 
                break
        else:
            print("❌ username / pasword salah.\n")

#=====================================================
# REGRISTASI AKUN
#=====================================================
def registrasi():
    print("\n=== REGISTRASI AKUN BARU ===")
    username = input("Buat username :")
    pasword  = input("Buat pasword  :")

    akun = load_akun()

    if username in akun :
        print("❌ Username sudah terdaftar!")
        return
    
    simpan_akun(username, pasword)
    print("✅ Registrasi berhasil!\n")

#========================================================
#TRANSAKSI UTAMA (langsung tampilkan daftar barang)
#========================================================
def transaksi(username):
    barang = load_barang()
    keranjang = []

    print("=========================")
    print(f"Selamat datang, {username}")
    print("=========================")

    while True:
        print("\n=== DAFTAR BARANG ===")
        print("Kode\tNama\tHarga")
        print("------------------------------")
        for kode, (nama, harga) in barang.items():
            print(f"{kode}\t{nama}\tRp{harga}")

        print("\nMasukan barang (enter untuk checkout)")
        kode = input("Kode barang :").strip().upper()

        if kode == "" :
            break

        if kode not in barang:
            print("❌ kode tidak ditemukann!")
            continue

        try:
            qty = int(input("jumlah    :"))
        except:
            print("❌ jumlah harus angka!")
            continue
            
        nama, harga = barang[kode]
        keranjang.append((nama,harga, qty))
        print(f"✅ Ditambahkan: {nama} x {qty}")

    if not keranjang:
        print("\nKeranjang kosong, transaksi dibatalkan.")
        return
    
    total_awal = sum(harga * qty for _, harga, qty in keranjang)

    # Diskon otomatis
    if total_awal > 200000:
        diskon = int(0.20 * total_awal)
    elif total_awal > 100000:
        diskon = int(0.15 * total_awal)
    elif total_awal > 50000:
        diskon = int(0.10 * total_awal)
    else:
        diskon = 0
    
    total_setelah_diskon = total_awal - diskon 
    ppn = int(0.11 * total_setelah_diskon)
    total_akhir = total_setelah_diskon + ppn

    print("\n=== TOTAL ===")
    print(f"Total awal  : Rp{total_awal}")
    print(f"Diskon      : Rp{diskon}")
    print(f"PPN 11%     : Rp{ppn}")
    print(f"Total akhir : Rp{total_akhir}")

    while True:
        try:
            bayar = int(input("Bayar       : Rp"))
            if bayar <  total_akhir:
                print("❌ Uang kurang!")
            else:
                break
        except:
            print("❌ Masukan angka!")

    kembali = bayar - total_akhir

    print(f"Kembali     : Rp{kembali}")
    print(f"✅ Transaksi selesai dan dicatat!")

    simpan_transaksi(username, keranjang, total_awal, diskon, ppn, total_akhir, bayar, kembali)

#==============================================
# MENU AWAL(Login/ Regoster/ Exit)
#==============================================
def menu_awal():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        pilih = input("Pilih menu :")

        if pilih == "1":
            login()
        elif pilih == "2":
            registrasi()
        elif pilih == "3":
            print("Keluar program... ")
            break
        else:
            print("❌ Pilihan tidak ada !")
        
#==============================================
# MAIN (Jalan dari menu awal)
#==============================================
if __name__=="__main__":
    menu_awal()