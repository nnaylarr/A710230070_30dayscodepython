import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class AplikasiInputTeks(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contoh PyQt dengan Input Teks')
        
        # Membuat layout
        layout = QVBoxLayout()
        
        # Membuat label
        self.label = QLabel('Masukkan teks di bawah:', self)
        
        # Membuat input teks
        self.input_teks = QLineEdit(self)
        
        # Membuat tombol
        self.tombol = QPushButton('Tampilkan Teks', self)
        self.tombol.clicked.connect(self.tampilkanTeks)
        
        # Menambahkan widget ke layout
        layout.addWidget(self.label)
        layout.addWidget(self.input_teks)
        layout.addWidget(self.tombol)
        
        # Mengatur layout pada jendela
        self.setLayout(layout)
        
        # Menentukan ukuran jendela
        self.setGeometry(300, 300, 400, 200)

    def tampilkanTeks(self):
        teks_input = self.input_teks.text()
        self.label.setText(f'Teks yang dimasukkan: {teks_input}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AplikasiInputTeks()
    ex.show()
    sys.exit(app.exec_())
