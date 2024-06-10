import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
import mysql.connector

class FormulirDataDiri(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplikasi Input Data')
        self.layout = QVBoxLayout()

        self.nama_input = QLineEdit()
        self.nama_input.setPlaceholderText('Nama')

        self.nim_input = QLineEdit()
        self.nim_input.setPlaceholderText('NIM')

        self.hobi_input = QLineEdit()
        self.hobi_input.setPlaceholderText('Hobi')

        self.submit_button = QPushButton('Kirim')
        self.submit_button.setStyleSheet('background-color: #82E0AA')
        self.submit_button.clicked.connect(self.tampilkanData)

        self.reset_button = QPushButton('Reset')
        self.reset_button.setStyleSheet('background-color: #E9F5AA')
        self.reset_button.clicked.connect(self.resetInput)

        self.result_label = QLabel('')

        self.layout.addWidget(self.result_label)
        self.layout.addWidget(QLabel('Masukan detail anda'))
        self.layout.addWidget(self.nama_input)
        self.layout.addWidget(self.nim_input)
        self.layout.addWidget(self.hobi_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.reset_button)
        self.setLayout(self.layout)

    def tampilkanData(self):
        name = self.nama_input.text()
        nim = self.nim_input.text()
        hobby = self.hobi_input.text()

        if not name and not nim and not hobby:
            self.showPopup('Semua field tidak boleh kosong!')
        elif not name and not nim:
            self.showPopup('Nama dan NIM tidak boleh kosong!')
        elif not name and not hobby:
            self.showPopup('Nama dan hobi tidak boleh kosong!')
        elif not nim and not hobby:
            self.showPopup('NIM dan hobi tidak boleh kosong!')
        elif not name:
            self.showPopup('Nama belum diisi!')
        elif not nim:
            self.showPopup('NIM belum diisi!')
        elif not hobby:
            self.showPopup('Hobi belum diisi!')
        elif not nim.isdigit() or len(nim) < 12:
            self.showPopup('NIM harus berupa angka dan minimal 12 digit!')
        else:
            self.result_label.setText(f'Nama: {name}\nNIM: {nim}\nHobi: {hobby}')
            self.save_to_db(name, nim, hobby)

    def save_to_db(self, name, nim, hobby):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='trisakti23',
                user='root',
                password=''
            )

            cursor = connection.cursor()
            insert_query = """INSERT INTO users (name, nim, hobby) VALUES (%s, %s, %s)"""
            record = (name, nim, hobby)
            cursor.execute(insert_query, record)
            connection.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan ke database!")
        except mysql.connector.Error as error:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data ke database: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def resetInput(self):
        self.nama_input.clear()
        self.nim_input.clear()
        self.hobi_input.clear()
        self.result_label.clear()  # Clear the result label

    def showPopup(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle('Peringatan')
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = FormulirDataDiri()
    form.show()
    sys.exit(app.exec())