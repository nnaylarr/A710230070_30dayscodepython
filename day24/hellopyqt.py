from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "Hello PyQt5"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.initWindow()

    def initWindow(self):
        self.label = QLabel("Welcome to PyQt5", self)
        self.label.adjustSize()  
        self.label.move(100, 100)  
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
app = QApplication([])
window = MainWindow()
app.exec_()
