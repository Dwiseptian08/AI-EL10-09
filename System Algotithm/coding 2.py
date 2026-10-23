# Memeriksa apakah tujuan dapat dicapai
    if distances[destination] == float("inf"):
        return None, float("inf")

    # Menyusun jalur dari tujuan ke titik awal
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[destination]


# Program utama
print("=== SISTEM PENCARIAN JALUR TERPENDEK ===")
print("Lokasi tersedia:", ", ".join(graph.keys()))

start = input("Masukkan lokasi awal: ").upper()
destination = input("Masukkan lokasi tujuan: ").upper()

if start not in graph or destination not in graph:
    print("Error: Lokasi tidak tersedia.")

else:
    path, distance = shortest_path(
        graph, start, destination
    )

    if path is None:
        print("Tidak ditemukan jalur menuju tujuan.")

    else:
        print("\n=== HASIL PERHITUNGAN ===")
        print("Jalur terpendek:", " -> ".join(path))
        print("Total jarak:", distance)
        print("Sistem selesai.")
