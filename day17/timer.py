import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTimeEdit
from PyQt5.QtCore import QTimer, QTime

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.time_display = QLabel('00:00:00', self)
        self.time_display.setStyleSheet("font-size: 40px;")
        self.layout.addWidget(self.time_display)
        
        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat("HH:mm:ss")
        self.layout.addWidget(self.time_edit)
      
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop_timer)
        self.layout.addWidget(self.stop_button)
        
        self.setLayout(self.layout)
        self.setWindowTitle('Timer App')
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = QTime(0, 0, 0)
        
    def start_timer(self):
        self.remaining_time = self.time_edit.time()
        self.time_display.setText(self.remaining_time.toString("HH:mm:ss"))
        self.timer.start(1000) 
    
    def stop_timer(self):
        self.timer.stop()
    
    def update_timer(self):
        if self.remaining_time == QTime(0, 0, 0):
            self.timer.stop()
            return
        self.remaining_time = self.remaining_time.addSecs(-1)
        self.time_display.setText(self.remaining_time.toString("HH:mm:ss"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())
