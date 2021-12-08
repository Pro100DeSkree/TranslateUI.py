from PyQt5 import QtWidgets, QtCore, Qt          # Импортируем Qt5
from PyQt5.QtWidgets import *
from TranslateUI import Ui_TranslateAPP      # Импорт Главного интерфейса
from ASKWin import Ui_ASKDialogWin           # Импорт Диалогового интерфейса(ASK)
from googletrans import Translator           # Импортируем гугл переводчик
from fuzzywuzzy import process as fuzz_p     # Импортируем модуль нечёткого сравнения
from fuzzywuzzy import fuzz
from threading import Thread          # Подключаем потоки
import random as rd                          # Импортируем модуль рандом
import sys                                   # Импортируем модуль system
import http.client as httplib




class mywindow(QtWidgets.QMainWindow):
    # Settings
    def __init__(self):
        super(mywindow, self).__init__()

        self.translator = Translator()
        self.ui = Ui_TranslateAPP()
        self.ui.setupUi(self)
        self.ui.LineTranslate_1.setMaxLength(34)                       # Ограничение символов в поле ввода 1
        self.ui.LineTranslate_2.setMaxLength(34)                       # Ограничение символов в поле ввода 2
        self.ui.PB_Translate.clicked.connect(self.CheckLangBoxes)      # При нажатии кнопки "Перевод" вызываем функцию
        self.ui.PB_ASK.clicked.connect(self.ASKClicked)                # При нажатии кнопки "Спросить" вызываем функцию
        self.ui.PB_LangSwitcher.clicked.connect(self.LangSwitch)
        self.ui.CB_Languages_1.addItems(["English", "Russian", "Ukraine"])     # Список языков в QComboBox1
        self.ui.CB_Languages_2.addItems(["English", "Russian", "Ukraine"])     # Список языков в QComboBox2
        self.ui.CB_Languages_2.setCurrentIndex(1)
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

                if lang1 != 'uk' and lang2 != 'uk':
                    if word != translateText:
                        self.Write(word, translateText)

            except TypeError:
                self.ui.LineTranslate_1.setPlaceholderText("Введите слово!!!")
        else:
            self.CheckInternet()

    def CheckLangBoxes(self):                                   # Функция чтения с ComboBox и передачей в translate()
        lang1 = self.ui.CB_Languages_1.currentText()            # Получаем значение с ComboBox
        lang2 = self.ui.CB_Languages_2.currentText()            # Получаем значение с ComboBox

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

    def keyPressEvent(self, event):                     # Функция чтения клавишь Return & Enter
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:   # Проверяем нажатие клавишь
            self.CheckLangBoxes()                               # Вызываем функцию      #       Return & Enter

    def LangSwitch(self):                               # Функция смены языков местами
        # Получаем индекс активного языка
        idxLang1 = self.ui.CB_Languages_1.findText(self.ui.CB_Languages_1.currentText())
        idxLang2 = self.ui.CB_Languages_2.findText(self.ui.CB_Languages_2.currentText())

        self.ui.CB_Languages_1.setCurrentIndex(idxLang2)                               # Меняем языки местами по индексу
        self.ui.CB_Languages_2.setCurrentIndex(idxLang1)                               # Меняем языки местами по индексу

    # ФУНКЦИЯ GrayLang РАБОТАЕТ КРИВО!!!(Срабатывает только при нажатии "Перевести" или Enter)
    def GrayLang(self, lang1="English"):      # Функция делает неактивными язык в ComboBox (Запускаеться 1раз)
        model = self.ui.CB_Languages_2.model()   # QStandardItemModel, метод model.item возвращает объекты QStandardItem
        model.item(0).setEnabled(True)
        model.item(1).setEnabled(True)
        model.item(2).setEnabled(True)
        idxLang1 = self.ui.CB_Languages_1.findText(lang1)  # Получаем индекс активного языка
        model.item(idxLang1).setEnabled(False)          # Указываем какие элементы сделать невыбираемыми

    # ФУНКЦИЯ CheckInternet РАБОТАЕТ КРИВО!!!(Проблемы с обратным подключением и ещё...)
    def CheckInternet(self):                            # Функция проверки подключения к инету
        conn = httplib.HTTPConnection("www.google.com")
        try:
            conn.request("HEAD", "/")
            self.ui.LineTranslate_1.setEnabled(True)
            return "Connected"
        except:
            self.ui.LineTranslate_1.setEnabled(False)

    def Write(self, word, translateText):               # Функция чтения\записи переведённых слов
        list = []
        WriteWord = word + " --> " + translateText + "\n"   # Склеиваем слова для записи (Перевести --> Перевод \n)

        with open("BD_Word.txt", "r") as BD_Word:       # Открываем файл на чтение
            for i in BD_Word:                           # Читаем файл построчно
                list.append(i)                          # Записываем каждую строку в список

        with open("BD_Word.txt", 'a') as BD_Word:       # Открываем файл на дозапись
            FuzzCoef = fuzz_p.extractOne(WriteWord, list)   # Выполняем нечёткое сравнение слов
            if FuzzCoef[1] < 100:                       # Если не нашлось похожих слов то записываем
                BD_Word.write(WriteWord)                # Записываем слово в словарь

    # Нужно доработать эту функцию либо удалить к ххх
    def mousePressEvent(self, event):
        button = event.button()
        self.GrayLang()
        if button == Qt.Qt.RightButton:
            print("Right button click!")

        elif button == Qt.Qt.LeftButton:
            print("Left button click!")

        # return Qt.QPushButton.mousePressEvent(self, event)


class dialog_win(QDialog):
    def __init__(self):
        # Setup
        super(dialog_win, self).__init__()

        self.ASKui = Ui_ASKDialogWin()
        self.ASKui.setupUi(self)

        list = []

        with open('BD_Word.txt', mode="r") as BD_Word:  # Открываем файл на чтение
            for line in BD_Word.readlines():            # Читаем файл построчно
                list.append(line)                       # Записываем слова в список

        RandWord = list[rd.randint(0, len(list))]       # Выбераем рандомное слово из списка
        Word = RandWord.partition(' --> ')[-3]          # Убераем вторую половину слова (Перевод)
        self.Word1 = RandWord.partition(' --> ')[2]     # Убираем первую чась
        self.Word1 = self.Word1[:-1]                    # Убираем из слова "\n"
        self.ASKui.LineASKWord.setText(Word)                # Вписываем слово в QEditLine

    def CheckTransWord(self):                           # Проверка правельности перевода
        Translate = self.ASKui.LineASKWordTrans.text()      # Записываем в переменную перевод который вписали в QEditLine
        FuzzCoef = fuzz.token_sort_ratio(self.Word1, Translate)     # Выполняем нечёткое сравнение слов
        try:                                            # Отлов ошибки пустой QEditLine
            if FuzzCoef >= 90:                          # Если коэф. схожести слов >= 90
                print("Слово совпадает")
            else:                                       # Иначе ...
                print("Слово не совпадает")
        except TypeError:
            self.ASKui.LineASKWordTrans.setPlaceholderText("Введите перевод!!!")    # Если стройка ввода была пустой

    def keyPressEvent(self, event):                             # Функция чтения клавишь Return & Enter
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:   # Проверяем нажатие клавишь
            self.CheckTransWord()                               # Вызов функции проверки перевода


if __name__ == "__main__":
    th = Thread(target=remind, args=())  # Создаём новый поток
    th.start()  # И запускаем его
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())


# Made by DeSkreeツ
# :)
