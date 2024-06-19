import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi dengan Tombol")
        
        self.button = QPushButton("Klik Saya", self)
        self.button.move(100, 100)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
