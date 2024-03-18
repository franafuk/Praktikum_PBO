def hitung_keliling(sisi_a, sisi_b, sisi_c):
    return sisi_a + sisi_b + sisi_c

def hitung_luas(alas, tinggi):
    return 0.5 * alas * tinggi

def main():
    print("PROGRAM MENGHITUNG KELILING & LUAS SEGITIGA")
    print("1. keliling")
    print("2. luas")
    
    pilihan = input("Silakan pilih angka untuk menghitung (1/2): ")

    if pilihan == "1":
        sisi_a = float(input("Masukkan sisi 1: "))
        sisi_b = float(input("Masukkan sisi 2: "))
        sisi_c = float(input("Masukkan sisi 3: "))

        if sisi_a + sisi_b > sisi_c and sisi_a + sisi_c > sisi_b and sisi_b + sisi_c > sisi_a:
            keliling = hitung_keliling(sisi_a, sisi_b, sisi_c)
            print("\nKeliling segitiga:", keliling, "cm")
        else:
            print("\nSisi-sisi yang dimasukkan tidak membentuk segitiga.")

    elif pilihan == "2":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = hitung_luas(alas, tinggi)
        print("\nLuas segitiga:", luas, "cm^2")

    else:
        print("\nPilihan tidak valid. Silakan pilih 1 untuk 'keliling' atau 2 untuk 'luas'.")

    print("Terima kasih telah menggunakan program ini!")


if __name__ == "__main__":
    main()
