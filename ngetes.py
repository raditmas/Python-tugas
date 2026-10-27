# Variabel global

# Definisi fungsi
def sum(arg1, arg2):
    """Menambahkan variabel dan mengembalikan hasilnya."""
    total = arg1 + arg2
    print("Di dalam fungsi nilai total :", total )
    return total

# Pemanggilan fungsi sum
hasil = sum(10, 20)

print("Di luar fungsi, nilai total :", hasil )
