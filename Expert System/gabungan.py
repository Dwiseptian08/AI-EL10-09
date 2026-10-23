def diagnosis_laptop():
    print("=" * 45)
    print(" SISTEM PAKAR DIAGNOSIS KERUSAKAN LAPTOP")
    print("=" * 45)

    print("\nJawab pertanyaan berikut dengan ya atau tidak.")

    # Mengumpulkan gejala
    power = input("Laptop tidak mau menyala? (ya/tidak): ").lower()
    charger = input("Lampu indikator charger mati? (ya/tidak): ").lower()
    layar = input("Laptop menyala tetapi layar hitam? (ya/tidak): ").lower()
    panas = input("Laptop cepat panas? (ya/tidak): ").lower()
    lambat = input("Laptop terasa sangat lambat? (ya/tidak): ").lower()
    baterai = input("Baterai cepat habis? (ya/tidak): ").lower()

    print("\n" + "=" * 45)
    print("HASIL DIAGNOSIS")
    print("=" * 45)

    # Basis aturan (Rule Base)
    if power == "ya" and charger == "ya":
        print("Diagnosis: Kemungkinan masalah adaptor atau sumber listrik.")
        print("Saran: Periksa stopkontak, adaptor, dan kabel daya.")

    elif power == "ya" and charger == "tidak":
        print("Diagnosis: Kemungkinan masalah baterai atau rangkaian daya.")
        print("Saran: Periksa adaptor, baterai, dan konektor daya.")

    elif layar == "ya":
        print("Diagnosis: Kemungkinan masalah layar atau RAM.")
        print("Saran: Periksa koneksi layar dan RAM melalui teknisi.")

    elif panas == "ya":
        print("Diagnosis: Kemungkinan sistem pendingin bermasalah.")
        print("Saran: Periksa kipas dan ventilasi laptop.")

    elif lambat == "ya":
        print("Diagnosis: Kemungkinan beban aplikasi tinggi atau penyimpanan lambat.")
        print("Saran: Periksa Task Manager dan kondisi penyimpanan.")

    elif baterai == "ya":
        print("Diagnosis: Kemungkinan kapasitas baterai menurun.")
        print("Saran: Periksa kesehatan baterai.")

    else:
        print("Diagnosis belum dapat ditentukan.")
        print("Diperlukan pemeriksaan lebih lanjut.")

    print("\nCatatan: Hasil ini hanya perkiraan awal.")
    print("Untuk kerusakan serius, hubungi teknisi.")
    print("=" * 45)


# Menjalankan sistem pakar
if __name__ == "__main__":
    diagnosis_laptop()
