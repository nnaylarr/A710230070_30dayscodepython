import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

class JournalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        
        self.initMenuBar()
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Jurnal')
        self.show()
    
    def initMenuBar(self):
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('File')
        
        newAct = QAction(QIcon('new.png'), 'New', self)
        newAct.setShortcut('Ctrl+N')
        newAct.triggered.connect(self.newFile)
        fileMenu.addAction(newAct)
        
        openAct = QAction(QIcon('open.png'), 'Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.triggered.connect(self.openFile)
        fileMenu.addAction(openAct)
        
        saveAct = QAction(QIcon('save.png'), 'Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAct)
        
        saveAsAct = QAction(QIcon('saveas.png'), 'Save As', self)
        saveAsAct.triggered.connect(self.saveFileAs)
        fileMenu.addAction(saveAsAct)
        
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(self.close)
        fileMenu.addAction(exitAct)
    
    def newFile(self):
        self.textEdit.clear()
    
    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())
    
    def saveFile(self):
        if not hasattr(self, 'currentFile') or not self.currentFile:
            self.saveFileAs()
        else:
            with open(self.currentFile, 'w') as file:
                file.write(self.textEdit.toPlainText())
    
    def saveFileAs(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            self.currentFile = fileName
            self.saveFile()

def main():
    app = QApplication(sys.argv)
    journal = JournalApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
