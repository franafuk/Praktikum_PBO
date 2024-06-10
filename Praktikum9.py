#Elemen Kompetensi 1
import math

class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def volume(self, sisi):
        return sisi ** 3

class Balok(BangunRuang):
    def volume(self, panjang, lebar, tinggi):
        return panjang * lebar * tinggi

class Tabung(BangunRuang):
    def volume(self, jari_jari, tinggi):
        return math.pi * jari_jari ** 2 * tinggi

# Fungsi main
def main():
    # Membuat objek dari kelas Kubus, Balok, dan Tabung
    kubus = Kubus()
    balok = Balok()
    tabung = Tabung()

    # Menampilkan informasi mahasiswa
    print("=====================")
    print("Nama: Francisco")
    print("NIM: 064002300044")
    print("=====================")

    # Menghitung dan menampilkan volume bangun ruang
    print("volume kubus dengan sisi 5 adalah:", kubus.volume(5), "cm^3")
    print("volume balok dengan panjang 4, lebar 3, dan tinggi 6 adalah:", balok.volume(4, 3, 6), "cm^3")
    print("volume tabung dengan jari-jari 2 dan tinggi 8 adalah:", tabung.volume(2, 8), "cm^3")

if __name__ == "__main__":
    main()

#Elemen Kompetensi 2
class p9e2:
    @staticmethod
    def methodTambah(x, y):
        return x + y

myNum1 = p9e2.methodTambah(8, 5)
myNum2 = p9e2.methodTambah(4.5, 6.5)
print("int:", myNum1)
print("float:", myNum2)
