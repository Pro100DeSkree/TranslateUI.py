from PyQt5 import QtWidgets, QtCore          # Импортируем Qt5
from TranslateUI import Ui_TranslateAPP      # Импорт UI файла
from googletrans import Translator           # Импортируем гугл переводчик
import sys                                   # Импортируем модуль system


class mywindow(QtWidgets.QMainWindow):
    # Settings
    def __init__(self):
        super(mywindow, self).__init__()

        self.translator = Translator()
        self.ui = Ui_TranslateAPP()
        self.ui.setupUi(self)
        self.ui.LineTranslate_1.setMaxLength(34)                       # Ограничение символов в поле ввода 1
        self.ui.LineTranslate_2.setMaxLength(34)                       # Ограничение символов в поле ввода 2
        self.ui.Translate.clicked.connect(self.CheckLangBoxes)         # При нажатии кнопки "Перевод" вызываем функцию
        self.ui.ASK_Button.clicked.connect(self.ASKClicked)            # При нажатии кнопки "Спросить" вызываем функцию
        self.ui.LangSwitcher.clicked.connect(self.LangSwitch)
        self.ui.ASK_CheckBox.stateChanged.connect(self.Check_Answer)   # Подключение ЧекБокса "Спаршивать переодически"
        self.ui.TimeSpinBox.valueChanged.connect(self.spinboxChanged)  # Подключение SpinBox "Интервал между вопросами"
        self.ui.Languages_1.addItems(["English", "Russian", "Ukraine"])     # Список языков в QComboBox1
        self.ui.Languages_2.addItems(["English", "Russian", "Ukraine"])     # Список языков в QComboBox2
        self.ui.Languages_2.setCurrentIndex(1)

    # Function
    def translate(self, lang1, lang2):                                      # Функция реагирования на клик
        word = self.ui.LineTranslate_1.text()                               # Вывод содержимого поля 1
        try:
            translate = self.translator.translate(word, src=lang1, dest=lang2)  # Перевод
            self.ui.LineTranslate_2.setText(translate.text)                     # Вывод перевода
        except TypeError:
            self.ui.LineTranslate_1.setPlaceholderText("Введите слово!!!")

    def CheckLangBoxes(self):                                   # Функция чтения с ComboBox и передачей в translate()
        lang1 = self.ui.Languages_1.currentText()               # Получаем значение с ComboBox
        lang2 = self.ui.Languages_2.currentText()               # Получаем значение с ComboBox

        if lang1 == "English":
            lang1_1 = 'en'
        elif lang1 == "Russian":
            lang1_1 = 'ru'
        else:
            lang1_1 = 'uk'

        if lang2 == "English":
            lang1_2 = 'en'
        elif lang2 == "Russian":
            lang1_2 = 'ru'
        else:
            lang1_2 = 'uk'

        self.translate(lang1_1, lang1_2)                        # Вызываем функцию с параметрами языков

    def ASKClicked(self):
        print("Clicked ASK")

    def Check_Answer(self, state):
        if state == QtCore.Qt.Checked:
            print("BoxEnable")
        else:
            print("BoxDisable")

    def spinboxChanged(self, value):
        print('New value of spinbox is:', value)

    def keyPressEvent(self, event):                             # Функция чтения клавишь Return & Enter
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:   # Проверяем нажатие клавишь
            self.CheckLangBoxes()                               # Вызываем функцию      #       Return & Enter

    def LangSwitch(self, index1):                               # Функция смены языков местами
        idxLang1 = self.ui.Languages_1.findText(self.ui.Languages_1.currentText())  # Получаем индекс активного языка
        idxLang2 = self.ui.Languages_2.findText(self.ui.Languages_2.currentText())  # Получаем индекс активного языка

        self.ui.Languages_1.setCurrentIndex(idxLang2)                               # Меняем языки местами по индексу
        self.ui.Languages_2.setCurrentIndex(idxLang1)                               # Меняем языки местами по индексу


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
