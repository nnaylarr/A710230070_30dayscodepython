import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.celsius_label = QLabel('Celsius:', self)
        self.celsius_input = QLineEdit(self)

        self.convert_button = QPushButton('Convert to Fahrenheit', self)
        self.convert_button.clicked.connect(self.convert_temperature)

        self.result_label = QLabel('Fahrenheit:', self)

        layout.addWidget(self.celsius_label)
        layout.addWidget(self.celsius_input)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle('Temperature Converter')
        self.setGeometry(300, 300, 300, 200)

    def convert_temperature(self):
        try:
            celsius = float(self.celsius_input.text())
            fahrenheit = (celsius * 9/5) + 32
            self.result_label.setText(f'Fahrenheit: {fahrenheit:.2f}')
        except ValueError:
            self.result_label.setText('Invalid input! Please enter a number.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec_())
