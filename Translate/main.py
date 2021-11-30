from PyQt5 import QtWidgets, QtCore
from TranslateUI import Ui_TranslateAPP  # импорт UI файла
import googletrans                       # Импортируем гугл переводчик
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_TranslateAPP()
        self.ui.setupUi(self)

        self.ui.LineTranslate_1.setMaxLength(34)                       # Ограничение символов в поле ввода 1
        self.ui.LineTranslate_2.setMaxLength(34)                       # Ограничение символов в поле ввода 2
        self.ui.Translate.clicked.connect(self.TranslateClicked)       # Подключение клик сигнала к def TranslateClicked
        self.ui.ASK_Button.clicked.connect(self.ASKClicked)            # Подключение клик сигнала к def ASKClicked
        self.ui.ASK_CheckBox.stateChanged.connect(self.Check_Answer)   # Подключение "клик" сигнала к def Check_Answer
        self.ui.TimeSpinBox.valueChanged.connect(self.spinboxChanged)  # Подключение спинбокса к def spinboxChanged

    def TranslateClicked(self):                                        # Функция реагирования на клик
        print(self.ui.LineTranslate_1.text())                          # Вывод содержимого поля 1

    def ASKClicked(self):
        print("Clicked ASK")

    def Check_Answer(self, state):
        if state == QtCore.Qt.Checked:
            print("BoxEnable")
        else:
            print("BoxDisable")

    def spinboxChanged(self, value):
        print('New value of spinbox is:', value)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
