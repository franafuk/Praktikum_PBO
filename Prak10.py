from bangun_datar import Persegi, Segitiga, Lingkaran, PersegiPanjang, JajarGenjang

# Buat objek dari setiap bangun datar
persegi = Persegi("persegi", 7)
segitiga = Segitiga("segitiga", 8, 6)
lingkaran = Lingkaran("lingkaran", 10)
persegi_panjang = PersegiPanjang("persegi panjang", 7, 4)
jajar_genjang = JajarGenjang("jajar genjang", 8, 6)

# Tampilkan informasi mahasiswa
print("=====================")
print("Nama : Francisco")
print("NIM : 064002300044")
print("=====================")

# Hitung dan tampilkan luas setiap bangun datar
print("luas persegi :", persegi.hitung_luas())
print("luas segitiga :", segitiga.hitung_luas())
print("luas lingkaran :", lingkaran.hitung_luas())
print("luas persegi panjang :", persegi_panjang.hitung_luas())
print("luas jajar genjang :", jajar_genjang.hitung_luas())

