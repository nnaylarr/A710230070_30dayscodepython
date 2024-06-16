import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox

class PemesananMakananApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Pemesanan Makanan')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Layout untuk input makanan
        self.foodLayout = QHBoxLayout()
        self.foodLabel = QLabel('Pilih Makanan:')
        self.foodComboBox = QComboBox()
        self.foodComboBox.addItems(['Nasi Goreng - Rp 15000', 'Mie Goreng - Rp 12000', 'Ayam Bakar - Rp 20000'])
        
        self.foodLayout.addWidget(self.foodLabel)
        self.foodLayout.addWidget(self.foodComboBox)
        
        # Layout untuk input jumlah
        self.quantityLayout = QHBoxLayout()
        self.quantityLabel = QLabel('Jumlah:')
        self.quantityInput = QLineEdit()
        
        self.quantityLayout.addWidget(self.quantityLabel)
        self.quantityLayout.addWidget(self.quantityInput)
        
        # Tombol pemesanan
        self.orderButton = QPushButton('Pesan')
        self.orderButton.clicked.connect(self.calculateTotal)
        
        # Tambahkan widget ke layout utama
        self.layout.addLayout(self.foodLayout)
        self.layout.addLayout(self.quantityLayout)
        self.layout.addWidget(self.orderButton)
        
        self.setLayout(self.layout)
        
    def calculateTotal(self):
        food = self.foodComboBox.currentText()
        quantity_text = self.quantityInput.text()
        
        if quantity_text.isdigit():
            quantity = int(quantity_text)
            if food == 'Nasi Goreng - Rp 25000':
                price = 25000
            elif food == 'Mie Goreng - Rp 23000':
                price = 23000
            elif food == 'Ayam Bakar - Rp 20000':
                price = 20000
            else:
                price = 0

            total = price * quantity
            QMessageBox.information(self, 'Total Harga', f'Total harga untuk {quantity} {food.split(" - ")[0]} adalah: Rp {total}', QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Peringatan', 'Jumlah harus berupa angka!', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PemesananMakananApp()
    ex.show()
    sys.exit(app.exec_())
