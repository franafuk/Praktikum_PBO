import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

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
        nama = self.nama_input.text()
        nim = self.nim_input.text()
        hobi = self.hobi_input.text()

        if not nama and not nim and not hobi:
            self.showPopup('Semua field tidak boleh kosong!')
        elif not nama and not nim:
            self.showPopup('Nama dan NIM tidak boleh kosong!')
        elif not nama and not hobi:
            self.showPopup('Nama dan hobi tidak boleh kosong!')
        elif not nim and not hobi:
            self.showPopup('NIM dan hobi tidak boleh kosong!')
        elif not nama:
            self.showPopup('Nama belum diisi!')
        elif not nim:
            self.showPopup('NIM belum diisi!')
        elif not hobi:
            self.showPopup('Hobi belum diisi!')
        elif not nim.isdigit() or len(nim) < 12:
            self.showPopup('NIM harus berupa angka dan minimal 12 digit!')
        else:
            self.result_label.setText(f'Nama: {nama}\nNIM: {nim}\nHobi: {hobi}')

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