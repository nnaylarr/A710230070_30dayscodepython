import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

class DiaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Aplikasi Catatan Harian')
        self.setGeometry(100, 100, 600, 400)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.text_edit)
        
        self.button_layout = QHBoxLayout()
        
        self.add_button = QPushButton('Tambah Catatan', self)
        self.add_button.clicked.connect(self.add_note)
        self.button_layout.addWidget(self.add_button)
        
        self.delete_button = QPushButton('Hapus Catatan', self)
        self.delete_button.clicked.connect(self.delete_note)
        self.button_layout.addWidget(self.delete_button)
        
        self.layout.addLayout(self.button_layout)
        
        self.note_list = QListWidget(self)
        self.note_list.itemClicked.connect(self.load_note)
        self.layout.addWidget(self.note_list)
        
        self.notes = {}
    
    def add_note(self):
        note_content = self.text_edit.toPlainText()
        if note_content:
            note_title = note_content.split('\n', 1)[0]  # Ambil baris pertama sebagai judul
            self.notes[note_title] = note_content
            self.note_list.addItem(note_title)
            self.text_edit.clear()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Catatan tidak boleh kosong!')
    
    def delete_note(self):
        selected_items = self.note_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            note_title = item.text()
            del self.notes[note_title]
            self.note_list.takeItem(self.note_list.row(item))
    
    def load_note(self, item):
        note_title = item.text()
        self.text_edit.setPlainText(self.notes[note_title])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    diary_app = DiaryApp()
    diary_app.show()
    sys.exit(app.exec_())
