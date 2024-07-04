import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import QTimer, QTime

class PengingatBelajar(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_reminder)
        self.start_time = QTime.currentTime()
        self.timer.start(7200000)  # 2 jam dalam milidetik

    def initUI(self):
        self.setWindowTitle('Pengingat Belajar 2 Jam')

        layout = QVBoxLayout()

        self.label = QLabel('Pengingat belajar aktif. Anda akan diingatkan setiap 2 jam.', self)
        layout.addWidget(self.label)

        self.btn_check_time = QPushButton('Waktu Belajar Terakhir', self)
        self.btn_check_time.clicked.connect(self.check_time)
        layout.addWidget(self.btn_check_time)

        self.setLayout(layout)

    def show_reminder(self):
        QMessageBox.information(self, 'Pengingat', 'Sudah 2 jam! Saatnya belajar!')
        self.start_time = QTime.currentTime()

    def check_time(self):
        elapsed_time = QTime.currentTime().secsTo(self.start_time) / 3600.0
        QMessageBox.information(self, 'Waktu Belajar Terakhir', f'Waktu belajar terakhir adalah {elapsed_time:.2f} jam yang lalu.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PengingatBelajar()
    ex.show()
    sys.exit(app.exec_())
