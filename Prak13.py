import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        self.layout = QVBoxLayout()

        # Create labels for displaying data
        self.name_label = QLabel("Nama: ")
        self.nim_label = QLabel("NIM: ")
        self.hobi_label = QLabel("Hobi: ")

        # Add the labels to the layout
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.nim_label)
        self.layout.addWidget(self.hobi_label)

        # Create input fields
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Masukkan Nama")
        self.nim_input = QLineEdit(self)
        self.nim_input.setPlaceholderText("Masukkan NIM")
        self.hobi_input = QLineEdit(self)
        self.hobi_input.setPlaceholderText("Masukkan Hobi")

        # Add input fields to the layout
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.nim_input)
        self.layout.addWidget(self.hobi_input)

        # Create a button to update labels
        self.update_button = QPushButton("Tampilkan Data", self)
        self.update_button.clicked.connect(self.update_labels)

        # Add button to the layout
        self.layout.addWidget(self.update_button)

        # Set the layout for the main window
        self.setLayout(self.layout)

    def update_labels(self):
        # Update labels with input data
        self.name_label.setText(f"Nama: {self.name_input.text()}")
        self.nim_label.setText(f"NIM: {self.nim_input.text()}")
        self.hobi_label.setText(f"Hobi: {self.hobi_input.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.setWindowTitle("Input Data Mahasiswa")
    window.resize(300, 200)
    window.show()

    # Run the application
    sys.exit(app.exec())
