from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize
from PyQt6 import QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget = QtWidgets.QComboBox(self)
        self.widget.addItems(["Россия", "Америка", "Германия"])
        self.widget.move(20, 10)
        self.widget.currentTextChanged.connect(self.combo_box)

        self.output_text1 = QtWidgets.QLabel(self)

        self.widget2 = QtWidgets.QCheckBox(self)
        self.widget2.setText("Подписаться на рассылку")
        self.widget2.move(200, 10)
        self.widget2.adjustSize()
        self.widget2.stateChanged.connect(self.check_box)

        self.output_text2 = QtWidgets.QLabel(self)

        self.widget3 = QtWidgets.QLineEdit(self)
        self.widget3.setMaxLength(10)
        self.widget3.setPlaceholderText("Введите число:")
        self.widget3.move(400, 10)
        self.widget3.adjustSize()
        self.widget3.textChanged.connect(self.line_edit)

        self.output_text3 = QtWidgets.QLabel(self)

        self.setFixedSize(QSize(900, 300))

    def combo_box(self, s):
        self.output_text1.setText(f'Ваш выбор - {s}')
        self.output_text1.move(20, 40)
        self.output_text1.adjustSize()

    def check_box(self):
        if self.widget2.isChecked():
            self.output_text2.setText('Вы подписались на рассылку')
            self.output_text2.move(200, 40)
            self.output_text2.adjustSize()
        else:
            self.output_text2.setText('')

    def line_edit(self, s):
        try:
            n = int(s)
            text = str(bin(n))
            self.output_text3.setText(f'В двоичной системе - {text[2:]}')
            self.output_text3.move(400, 40)
            self.output_text3.adjustSize()

        except:
            pass


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
