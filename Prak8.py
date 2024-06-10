class GolonganKampus:
    def __init__(self, golongan, gaji):
        self.golongan = golongan
        self.gaji = gaji

    def info(self):
        return f"Golongan: {self.golongan}, Gaji: {self.gaji}"

class Dosen(GolonganKampus):
    def __init__(self, gaji):
        super().__init__("DOSEN", gaji)

class Staff(GolonganKampus):
    def __init__(self, gaji):
        super().__init__("STAFF", gaji)

class Lainnya(GolonganKampus):
    def __init__(self, gaji):
        super().__init__("LAINNYA", gaji)

# Penggunaan
dosen = Dosen(10000000)
staff = Staff(7000000)
lainnya = Lainnya(5000000)

print(
    "=============================\n"
    "||Nama: Francisco           ||\n"
    "||NIM: 064002300044         ||\n"
    "=============================\n"
)
print(dosen.info())
print(staff.info())
print(lainnya.info())
