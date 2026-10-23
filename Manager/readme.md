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





# System Algorithm: Shortest Path Using Dijkstra

## 1. Introduction

System Algorithm merupakan implementasi algoritma untuk menyelesaikan masalah secara sistematis melalui serangkaian langkah logis.

Program ini menggunakan algoritma Dijkstra untuk mencari jalur terpendek antara dua lokasi pada sebuah graf berbobot.

Setiap lokasi direpresentasikan sebagai simpul (node), sedangkan hubungan antarlokasi direpresentasikan sebagai sisi (edge) yang memiliki nilai jarak.

Algoritma Dijkstra bekerja dengan mencari jalur yang memiliki total bobot terkecil dari lokasi awal menuju lokasi tujuan.

## 2. Requirement

Persyaratan untuk menjalankan program:
- Python 3.9 atau lebih baru.
- Text editor atau IDE, seperti Visual Studio Code.
- Terminal atau Command Prompt.
- Menggunakan library bawaan Python `heapq` untuk mengelola antrean prioritas.
- Tidak memerlukan instalasi library tambahan.

## 3. How to Use

1. Pastikan Python sudah terinstal.
2. Simpan kode program dengan nama `system_algorithm.py`.
3. Buka terminal pada folder tempat file disimpan.
4. Jalankan program dengan perintah:

   ```bash
   python system_algorithm.py
   ```

5. Masukkan lokasi awal dan lokasi tujuan.
6. Gunakan lokasi yang tersedia, yaitu A, B, C, D, atau E.
7. Program akan menghitung dan menampilkan jalur terpendek beserta total jaraknya.

## 4. Result

Program menghasilkan jalur dengan total bobot paling kecil berdasarkan graf yang telah ditentukan.

Contoh input:

```text
Masukkan lokasi awal: A
Masukkan lokasi tujuan: E
```

Contoh output:

```text
HASIL PERHITUNGAN

Jalur terpendek: A -> C -> B -> D -> E
Total jarak: 10
Sistem selesai.
```

Hasil tersebut menunjukkan bahwa jalur A → C → B → D → E memiliki total jarak 10 satuan berdasarkan bobot pada graf.

Program ini dapat diterapkan sebagai dasar simulasi navigasi, pencarian rute, dan optimasi jalur. Algoritma Dijkstra mengasumsikan seluruh bobot jarak bernilai non-negatif.
