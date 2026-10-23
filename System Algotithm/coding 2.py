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
