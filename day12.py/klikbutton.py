import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Simple App')
        self.setGeometry(100, 100, 300, 200)
        
        btn = QPushButton('Click Me', self)
        btn.move(100, 80)
        btn.clicked.connect(self.showMessage)
        self.show()
        
    def showMessage(self):
        QMessageBox.information(self, 'Message', 'You clicked the button!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
