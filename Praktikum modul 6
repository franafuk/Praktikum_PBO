print("===============")
print("Nama: Francisco")
print("Nim: 064002300044")
print("===============")
import math

class BangunRuang:
    def __init__(self, nama):
        self.nama = nama

class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__("Kubus")
        self.sisi = sisi

    def hitung_luas(self):
        return 6 * self.sisi ** 2

    def hitung_volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__("Balok")
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_luas(self):
        return 2 * ((self.panjang * self.lebar) + (self.panjang * self.tinggi) + (self.lebar * self.tinggi))

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, jari_jari):
        super().__init__("Bola")
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return 4 * math.pi * self.jari_jari ** 2

    def hitung_volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Silinder(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__("Silinder")
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)

    def hitung_volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

class PrismaSegitiga(BangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi_prisma):
        super().__init__("Prisma Segitiga")
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_prisma = tinggi_prisma

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi_alas + (self.alas * self.tinggi_prisma) + (self.tinggi_alas * self.tinggi_prisma)

    def hitung_volume(self):
        return 0.5 * self.alas * self.tinggi_alas * self.tinggi_prisma

def main():
    # Membuat objek dari lima bangun ruang berbeda
    kubus = Kubus(5)
    balok = Balok(6, 5, 2)
    bola = Bola(7)
    silinder = Silinder(5, 4)
    prisma_segitiga = PrismaSegitiga(6, 8, 12)

    # Menampilkan luas dan volume dari masing-masing bangun ruang
    print("Luas", kubus.nama, ":", kubus.hitung_luas())
    print("Volume", kubus.nama, ":", kubus.hitung_volume())

    print("Luas", balok.nama, ":", balok.hitung_luas())
    print("Volume", balok.nama, ":", balok.hitung_volume())

    print("Luas", bola.nama, ":", bola.hitung_luas())
    print("Volume", bola.nama, ":", bola.hitung_volume())

    print("Luas", silinder.nama, ":", silinder.hitung_luas())
    print("Volume", silinder.nama, ":", silinder.hitung_volume())

    print("Luas", prisma_segitiga.nama, ":", prisma_segitiga.hitung_luas())
    print("Volume", prisma_segitiga.nama, ":", prisma_segitiga.hitung_volume())

if __name__ == "__main__":
    main()
