class Praktikan:
    def __init__(self, nama):
        self.nama = nama

    @staticmethod
    def get_nim():
        return "064002300044"

    @staticmethod
    def get_nilai():
        return 100

    def display_info(self):
        print("-----DATA PRIBADI-----")
        print("nama :", self.nama)
        print("NIM :", self.get_nim())
        print("Nilai :", self.get_nilai())

class Teman:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def get_nim(self):
        return self.nim

    def get_nilai(self):
        return self.nilai

    def display_info(self):
   
        print("nama :", self.nama)
        print("NIM :", self.get_nim())
        print("Nilai :", self.get_nilai())

# Fungsi untuk menyimpan output dari program
def save_output(praktikan, teman1, teman2, teman3):
    praktikan.display_info()
    print("\n-----Data {}-----".format("Teman1"))
    teman1.display_info() 
    print("\n-----Data {}-----".format("Teman2"))  # Menambahkan spasi tambahan di sini
    teman2.display_info()
    print("\n-----Data {}-----".format("Teman3"))
    teman3.display_info()

# Pembuatan objek praktikan dan teman
praktikan = Praktikan("francisco")
teman1 = Teman("akmal", "064002300045", 99)
teman2 = Teman("mike", "064002300036", 95)
teman3 = Teman("nalen", "064002300043", 80)

# Menyimpan dan menampilkan output dari program
save_output(praktikan, teman1, teman2, teman3)
