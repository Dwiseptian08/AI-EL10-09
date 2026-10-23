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
