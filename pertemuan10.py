print(" PROGRAM OPERASI MATRIKS 3x3 Penjumlahan") 
print(" ---------------------------------------------------------")
print(" Nama  : Ilham Raditya Wibowo")
print(" NIM   : 17250028")
print(" Kelas : 17-1A-01")
print(" ---------------------------------------------------------")
# -----------------------------
# MERGE SORT
# -----------------------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Rekursi
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Penggabungan dua bagian (merge)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Sisa elemen kiri
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Sisa elemen kanan
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# -----------------------------
# QUICK SORT
# -----------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# -----------------------------
# BINARY SEARCH
# -----------------------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return f"Angka {target} ditemukan pada indeks {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return f"Angka {target} TIDAK ditemukan dalam list"


# ---------------------------------------------------
# UJI DATA
# ---------------------------------------------------

# Data untuk sorting
data = [25, 20, 15, 3, 7, 2, 1]

# MERGE SORT
data_merge = data.copy()
merge_sort(data_merge)

# QUICK SORT
data_quick = quick_sort(data)

# BINARY SEARCH
data_bs = [3, 6, 9, 13, 16, 26, 38, 58]

hasil_13 = binary_search(data_bs, 13)
hasil_16 = binary_search(data_bs, 16)
hasil_10 = binary_search(data_bs, 10)

# Cetak hasil
print("=== HASIL MERGE SORT ===")
print(data_merge)

print("\n=== HASIL QUICK SORT ===")
print(data_quick)

print("\n=== BINARY SEARCH ===")
print(hasil_13)
print(hasil_16)
print(hasil_10)