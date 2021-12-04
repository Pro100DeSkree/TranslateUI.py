from PyQt5 import QtWidgets, QtCore          # Импортируем Qt5
from PyQt5.QtWidgets import *
from TranslateUI import Ui_TranslateAPP      # Импорт Главного интерфейса
from ASKWin import Ui_ASKDialogWin           # Импорт Диалогового интерфейса(ASK)
from googletrans import Translator           # Импортируем гугл переводчик
import sys                                   # Импортируем модуль system
import http.client as httplib


class dialog_win(QDialog):
    def __init__(self):
        super(dialog_win, self).__init__()

        self.ASKui = Ui_ASKDialogWin()
        self.ASKui.setupUi(self)
        self.ASKui.ASKWord.setText("Тут дол. быть слово")

        with open('BD_Word.txt', mode="rt") as BD_Word:
            for line in BD_Word.readlines():
                print(line)


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
        self.GrayLang()
        self.CheckInternet()
        # self.ui.ByDeSkree.setText("By DeSkree")

    # Function
    def translate(self, lang1, lang2):                                      # Функция реагирования на клик
        ConnOrDisconn = self.CheckInternet()

        if ConnOrDisconn == "Connected":
            word = self.ui.LineTranslate_1.text()                                   # Вывод содержимого поля 1
            try:
                translate = self.translator.translate(word, src=lang1, dest=lang2)  # Перевод
                translateText = translate.text                                      # Получаем слово с перевода
                self.ui.LineTranslate_2.setText(translateText)                      # Вывод перевода

                CheckWord = {}

                with open("BD_Word.txt", "r") as BD_Word:       # Открываем файл на чтение
                    for line in BD_Word:
                        key, *value = line.split()
                        CheckWord[key] = value
                    print(CheckWord.items())
                with open("BD_Word.txt", "a") as BD_Word:
                    Words = {word: translateText}               # Создаём список с переведёнными словами
                    print(Words, file=BD_Word)                  # Запись переведённых слов в файл

            except TypeError:
                self.ui.LineTranslate_1.setPlaceholderText("Введите слово!!!")
        else:
            self.CheckInternet()

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

        self.GrayLang(lang1)
        self.translate(lang1_1, lang1_2)                        # Вызываем функцию с параметрами языков

    def ASKClicked(self):
        self.cust = dialog_win()
        if self.cust.exec_():
            print('get')
        print("Clicked ASK")

    def Check_Answer(self, state):
        if state == QtCore.Qt.Checked:
            print("BoxEnable")
        else:
            print("BoxDisable")

    def spinboxChanged(self, value):
        print('New value of spinbox is:', value)
        if value == 21:
            print("Нужно дополнительное условие")

    def keyPressEvent(self, event):                             # Функция чтения клавишь Return & Enter
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:   # Проверяем нажатие клавишь
            self.CheckLangBoxes()                               # Вызываем функцию      #       Return & Enter

    def LangSwitch(self):                               # Функция смены языков местами
        idxLang1 = self.ui.Languages_1.findText(self.ui.Languages_1.currentText())  # Получаем индекс активного языка
        idxLang2 = self.ui.Languages_2.findText(self.ui.Languages_2.currentText())  # Получаем индекс активного языка

        self.ui.Languages_1.setCurrentIndex(idxLang2)                               # Меняем языки местами по индексу
        self.ui.Languages_2.setCurrentIndex(idxLang1)                               # Меняем языки местами по индексу

    def GrayLang(self, lang1="English"):                # Функция делает неактивными язык в ComboBox (Запускаеться 1раз)
        model = self.ui.Languages_2.model()  # QStandardItemModel, метод model.item возвращает объекты QStandardItem
        model.item(0).setEnabled(True)
        model.item(1).setEnabled(True)
        model.item(2).setEnabled(True)
        idxLang1 = self.ui.Languages_1.findText(lang1)  # Получаем индекс активного языка
        model.item(idxLang1).setEnabled(False)          # Указываем какие элементы сделать невыбираемыми

    def CheckInternet(self):
        conn = httplib.HTTPConnection("www.google.com")
        try:
            conn.request("HEAD", "/")
            self.ui.LineTranslate_1.setEnabled(True)
            return "Connected"
        except:
            while False:
                self.ui.LineTranslate_1.setEnabled(False)
                # self.CheckInternet()
            print("Disconnected")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
# Made by DeSkreeツ
# :)
