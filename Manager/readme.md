# Multi-Agent System (MAS)

## 1. Introduction

Multi-Agent System (MAS) adalah sistem yang terdiri dari beberapa agen yang bekerja sama untuk menyelesaikan suatu tugas. Setiap agen memiliki peran dan tanggung jawab yang berbeda.

Program ini menggunakan Python untuk membuat simulasi sistem multi-agent yang dapat menyusun laporan berdasarkan topik yang dimasukkan oleh pengguna.

Terdapat empat komponen utama:
- **Researcher Agent:** Mengumpulkan informasi berdasarkan topik.
- **Analyst Agent:** Menganalisis informasi yang telah dikumpulkan.
- **Writer Agent:** Menyusun informasi dan analisis menjadi laporan.
- **Coordinator Agent:** Mengatur urutan kerja seluruh agen.

## 2. Requirement

Persyaratan untuk menjalankan program:
- Python 3.9 atau lebih baru.
- Text editor atau IDE, seperti Visual Studio Code.
- Terminal atau Command Prompt.
- Tidak memerlukan library tambahan karena menggunakan pustaka standar Python.

## 3. How to Use

1. Pastikan Python sudah terinstal di komputer.
2. Simpan kode program dengan nama `multi_agent.py`.
3. Buka terminal pada folder tempat file disimpan.
4. Jalankan program dengan perintah:

   ```bash
   python multi_agent.py
   ```

5. Masukkan topik yang ingin dibahas ketika program meminta input.
6. Tunggu hingga seluruh agen menyelesaikan tugasnya dan laporan ditampilkan.

## 4. Result
![Uploading image.png…]()

Program menghasilkan laporan berdasarkan topik yang dimasukkan oleh pengguna.

Contoh input:

```text
Internet of Things
```

Hasil yang ditampilkan meliputi:
- Informasi mengenai topik.
- Hasil analisis informasi.
- Kesimpulan yang disusun menjadi laporan akhir.

Program ini menunjukkan bagaimana beberapa agen dengan peran berbeda dapat bekerja secara berurutan untuk menyelesaikan suatu tugas.

**Catatan:** Program ini merupakan simulasi multi-agent berbasis aturan Python. Researcher belum melakukan pencarian internet dan agen belum menggunakan model AI atau LLM sungguhan.






# Expert System

## 1. Introduction

Expert System atau sistem pakar adalah sistem komputer yang menggunakan pengetahuan dan aturan tertentu untuk membantu menyelesaikan masalah atau mengambil keputusan pada bidang tertentu.

Program ini merupakan sistem pakar sederhana untuk melakukan diagnosis awal kerusakan laptop berdasarkan gejala yang dialami pengguna.

Sistem menggunakan aturan IF-THEN untuk mencocokkan gejala dengan kemungkinan masalah.

Komponen utamanya:
- **Knowledge Base:** Menyimpan pengetahuan mengenai gejala dan kemungkinan kerusakan.
- **Rule Base:** Menyimpan aturan IF-THEN untuk menentukan hasil diagnosis.
- **Inference Engine:** Mencocokkan jawaban pengguna dengan aturan yang tersedia.
- **User Interface:** Menerima jawaban pengguna dan menampilkan hasil diagnosis.

## 2. Requirement

Persyaratan untuk menjalankan program:
- Python 3.9 atau lebih baru.
- Text editor atau IDE, seperti Visual Studio Code.
- Terminal atau Command Prompt.
- Tidak memerlukan library tambahan.

## 3. How to Use

1. Pastikan Python sudah terinstal.
2. Simpan kode program dengan nama `expert_system.py`.
3. Buka terminal pada folder tempat file disimpan.
4. Jalankan program menggunakan perintah:

   ```bash
   python expert_system.py
   ```

5. Jawab setiap pertanyaan mengenai kondisi laptop dengan memasukkan `ya` atau `tidak`.
6. Setelah semua pertanyaan dijawab, sistem akan menampilkan kemungkinan kerusakan dan saran penanganan.

## 4. Result

Program menghasilkan dugaan awal kerusakan laptop berdasarkan jawaban pengguna.

Contoh input:

```text
Laptop tidak mau menyala? ya
Lampu indikator charger mati? ya
Laptop menyala tetapi layar hitam? tidak
Laptop cepat panas? tidak
Laptop terasa sangat lambat? tidak
Baterai cepat habis? tidak
```

Contoh hasil:

```text
HASIL DIAGNOSIS

Diagnosis: Kemungkinan masalah adaptor
atau sumber listrik.

Saran: Periksa stopkontak, adaptor,
dan kabel daya.
```

Program ini membantu pengguna memahami kemungkinan penyebab masalah berdasarkan gejala yang dipilih. Hasil diagnosis hanya berupa perkiraan awal dan tidak menggantikan pemeriksaan teknisi.





# Search Algorithm

## 1. Introduction

Search Algorithm adalah algoritma yang digunakan untuk mencari data tertentu di dalam sekumpulan data. Program ini dibuat menggunakan bahasa pemrograman Python dan menerapkan dua metode pencarian, yaitu **Linear Search** dan **Binary Search**.

- **Linear Search:** Mencari data dengan memeriksa setiap elemen secara berurutan hingga data ditemukan.
- **Binary Search:** Mencari data dengan membagi area pencarian menjadi dua bagian secara berulang. Algoritma ini membutuhkan data yang sudah terurut.

Program ini bertujuan untuk memahami cara kerja kedua algoritma pencarian serta mengetahui perbedaan metode pencarian data.

## 2. Requirement

Untuk menjalankan program ini, diperlukan:

- Python 3.x
- Text editor atau IDE, seperti Visual Studio Code atau PyCharm.
- Terminal atau Command Prompt.

**Dependencies:** Tidak memerlukan library tambahan karena program hanya menggunakan fitur bawaan Python.

## 3. How to Use

Ikuti langkah-langkah berikut:

1. Pastikan Python sudah terinstal di komputer.
2. Simpan kode program dengan nama `search_algorithm.py`.
3. Buka terminal atau Command Prompt pada folder tempat file disimpan.
4. Jalankan program menggunakan perintah berikut:

   ```bash
   python search_algorithm.py
   ```

5. Program akan menampilkan daftar angka yang tersedia.
6. Masukkan angka yang ingin dicari.
7. Program akan menjalankan Linear Search dan Binary Search, kemudian menampilkan hasil pencarian beserta indeks data jika ditemukan.

**Catatan:** Binary Search hanya dapat digunakan dengan benar jika data sudah terurut.

## 4. Result

Program akan menampilkan hasil pencarian menggunakan kedua algoritma berdasarkan angka yang dimasukkan oleh pengguna.

Contoh output:

```text
=== SEARCH ALGORITHM ===
Data: [10, 20, 30, 40, 50, 60, 70]
Masukkan angka yang dicari: 50

=== HASIL PENCARIAN ===
Linear Search: Data ditemukan pada indeks 4
Binary Search: Data ditemukan pada indeks 4
```

Jika angka yang dimasukkan tidak tersedia di dalam daftar, program akan menampilkan pesan bahwa data tidak ditemukan.

### Conclusion

Program ini menunjukkan bahwa Linear Search melakukan pencarian secara berurutan, sedangkan Binary Search mempersempit area pencarian dengan membagi data menjadi dua bagian. Binary Search umumnya lebih efisien untuk data berukuran besar yang sudah terurut.


asi navigasi, pencarian rute, dan optimasi jalur. Algoritma Dijkstra mengasumsikan seluruh bobot jarak bernilai non-negatif.
