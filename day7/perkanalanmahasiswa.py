import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class IntroductionApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Perkenalan Nama dan NIM')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Layout untuk input
        self.nameLabel = QLabel('Nama:')
        self.nameInput = QLineEdit()
        self.nimLabel = QLabel('NIM:')
        self.nimInput = QLineEdit()
        
        # Tambahkan widget ke layout utama
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.nameInput)
        self.layout.addWidget(self.nimLabel)
        self.layout.addWidget(self.nimInput)
        
        # Tombol perkenalan
        self.introButton = QPushButton('Perkenalkan')
        self.introButton.clicked.connect(self.showIntroduction)
        
        self.layout.addWidget(self.introButton)
        
        self.setLayout(self.layout)
        
    def showIntroduction(self):
        name = self.nameInput.text()
        nim = self.nimInput.text()
        if name and nim:
            intro = f'Halo, nama saya {name} dan NIM saya {nim}.'
            QMessageBox.information(self, 'Perkenalan', intro, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Peringatan', 'Nama dan NIM tidak boleh kosong!', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = IntroductionApp()
    ex.show()
    sys.exit(app.exec_())
