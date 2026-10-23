
# Search Algorithm
# Implementasi Linear Search dan Binary Search

def linear_search(data, target):
    """
    Mencari data satu per satu dari awal.
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target):
    """
    Mencari data dengan membagi area pencarian menjadi dua.
    Data harus sudah terurut.
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Data yang akan dicari
data = [10, 20, 30, 40, 50, 60, 70]

print("=== SEARCH ALGORITHM ===")
print("Data:", data)

target = int(input("Masukkan angka yang dicari: "))

# Linear Search
result_linear = linear_search(data, target)

# Binary Search
result_binary = binary_search(data, target)

print("\n=== HASIL PENCARIAN ===")

if result_linear != -1:
    print("Linear Search: Data ditemukan pada indeks",
          result_linear)
else:
    print("Linear Search: Data tidak ditemukan")

if result_binary != -1:
    print("Binary Search: Data ditemukan pada indeks",
          result_binary)
else:
    print("Binary Search: Data tidak ditemukan")
