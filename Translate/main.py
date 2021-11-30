from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QCheckBox
from TranslateUI import Ui_MainWindow  # импорт UI файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.LineTranslate_1.setMaxLength(34)                  # Ограничение символов в поле ввода 1
        self.ui.LineTranslate_2.setMaxLength(34)                  # Ограничение символов в поле ввода 2
        self.ui.Translate.clicked.connect(self.TranslateClicked)  # Подключение клик сигнала к слоту TranslateClicked
        self.ui.ASK_Button.clicked.connect(self.ASKClicked)       # Подключение клик сигнала к слоту ASKClicked
        self.ui.ASK_CheckBox.stateChanged.connect(self.Check_Answer)

    def Check_Answer(self, state):

        if state == QtCore.Qt.Checked:
            print("Ух ты! Вы любите программирование.")
        else:
            print("О нет! – Вы не любите программировать.")

    def ASKClicked(self):
        print("Clicked ASK")

    def TranslateClicked(self):                                   # Функция реагирования на клик
        print(self.ui.LineTranslate_1.text())                     # Вывод содержимого поля 1


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
