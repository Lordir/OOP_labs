from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize
from PyQt6 import QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Стоимость кофе")
        self.output_value = 0
        self.flag1 = False
        self.flag2 = False
        self.flag3 = ""
        self.number = 1

        self.text1 = QtWidgets.QLabel(self)
        self.text1.setText("Выберите тип кофе:")
        self.text1.move(20, 10)
        self.text1.adjustSize()

        self.text2 = QtWidgets.QLabel(self)
        self.text2.setText("Итого:")
        self.text2.move(530, 10)
        self.text2.adjustSize()

        self.widget = QtWidgets.QComboBox(self)
        self.widget.addItems(["Латте", "Американо", "Капучино"])
        self.widget.move(20, 30)
        self.widget.currentTextChanged.connect(self.get_data3)

        self.widget2 = QtWidgets.QCheckBox(self)
        self.widget2.setText("Добавить сахар")
        self.widget2.move(140, 25)
        self.widget2.adjustSize()
        self.widget2.stateChanged.connect(self.get_data)

        self.widget3 = QtWidgets.QCheckBox(self)
        self.widget3.setText("Добавить сливки")
        self.widget3.move(140, 45)
        self.widget3.adjustSize()
        self.widget3.stateChanged.connect(self.get_data2)

        self.widget4 = QtWidgets.QLineEdit(self)
        self.widget4.setMaxLength(2)
        self.widget4.setPlaceholderText("Количество чашек:")
        self.widget4.move(270, 35)
        self.widget4.adjustSize()
        self.widget4.textChanged.connect(self.get_data4)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("=")
        self.button.move(400, 30)
        self.button.clicked.connect(lambda: self.clicked_button())

        self.output_text = QtWidgets.QLabel(self)

        self.setFixedSize(QSize(900, 300))

    def get_data(self):
        self.widget2_checked = self.widget2.isChecked()
        if self.widget2_checked:
            if not self.flag1:
                self.output_value += 5
                self.flag1 = True
        else:
            self.output_value -= 5
            self.flag1 = False

    def get_data2(self):
        self.widget3_checked = self.widget3.isChecked()
        if self.widget3_checked:
            if not self.flag2:
                self.output_value += 10
                self.flag2 = True
        else:
            self.output_value -= 10
            self.flag2 = False

    def get_data3(self, s):
        if self.flag3 == "Латте":
            self.output_value -= 250
        elif self.flag3 == "Капучино":
            self.output_value -= 200
        elif self.flag3 == "Американо":
            self.output_value -= 150
        if s == "Латте":
            self.output_value += 250
            self.flag3 = "Латте"
        elif s == "Капучино":
            self.output_value += 200
            self.flag3 = "Капучино"
        elif s == "Американо":
            self.output_value += 150
            self.flag3 = "Американо"

    def get_data4(self, s):
        try:
            n = int(s)
            if n > 0:
                self.number = n
        except:
            pass


    def clicked_button(self):
        self.output_text.setText(str(self.output_value * self.number))
        self.output_text.move(550, 30)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
