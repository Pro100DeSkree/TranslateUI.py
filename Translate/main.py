from PyQt5 import QtWidgets, QtCore, Qt      # Импортируем Qt5
from PyQt5.QtWidgets import *
from TranslateUI import Ui_TranslateAPP      # Импорт Главного интерфейса
from ASKWin import Ui_ASKDialogWin           # Импорт Диалогового интерфейса(ASK)
from googletrans import Translator           # Импортируем гугл переводчик
from fuzzywuzzy import process as fuzz_p     # Импортируем модуль нечёткого сравнения
from fuzzywuzzy import fuzz                  # Импортируем модуль нечёткого сравнения
from threading import Thread                 # Импортируем модуль многопоточности
import random as rd                          # Импортируем модуль рандом
import sys                                   # Импортируем модуль system
import http.client as httplib                # Импортируем модуль (Хз что за моуль) для порверки подключения к сети
from time import sleep                       # Импортируем модуль сна


class MainWindow(QtWidgets.QMainWindow):
    # Settings
    def __init__(self):
        super(MainWindow, self).__init__()

        self.translator = Translator()
        self.ui = Ui_TranslateAPP()
        self.ui.setupUi(self)
        self.ui.line_translate_1.setMaxLength(34)                       # Ограничение символов в поле ввода 1
        self.ui.line_translate_2.setMaxLength(34)                       # Ограничение символов в поле ввода 2
        self.ui.pb_translate.clicked.connect(self.check_lang_boxes)     # При нажатии кнопки "Перевод" вызываем функцию
        self.ui.pb_ask.clicked.connect(self.ASKClicked)                 # При нажатии кнопки "Спросить" вызываем функцию
        self.ui.pb_lang_switcher.clicked.connect(self.lang_switch)             # Кнопка смены языка
        self.ui.cb_languages_1.addItems(["English", "Russian", "Ukraine"])     # Задаём список языков в QComboBox1
        self.ui.cb_languages_2.addItems(["English", "Russian", "Ukraine"])     # Задаём список языков в QComboBox2
        self.ui.cb_languages_2.setCurrentIndex(1)                              # Устанавливаем язык в ComboBox
        th_ch_internet = Thread(target=self.thread_internet_check, args=(), daemon=True)  # Создаём новый поток
        th_ch_gray_lang = Thread(target=self.gray_lang, args=(), daemon=True)             # Создаём ещё один новый поток
        th_ch_gray_lang.start()                     # Запускаем поток проверки ComboBox-ов на смену языков
        th_ch_internet.start()                      # Запускаме поток проверки подключения к интернету

    # Function
    def translate(self, lang1, lang2):                                          # Функция реагирования на клик
        word = self.ui.line_translate_1.text()                                  # Вывод содержимого поля 1
        try:
            translate = self.translator.translate(word, src=lang1, dest=lang2)  # Перевод
            translate_text = translate.text                                     # Получаем слово с перевода
            self.ui.line_translate_2.setText(translate_text)                    # Вывод перевода

            if lang1 != 'uk' and lang2 != 'uk':
                if word != translate_text:
                    self.write_w(word, translate_text)

        except TypeError:
            self.ui.line_translate_1.setPlaceholderText("Введите слово!!!")

    def check_lang_boxes(self):                                    # Функция чтения с ComboBox и передачей в translate()
        lang1 = self.ui.cb_languages_1.currentText()               # Получаем значение с ComboBox
        lang2 = self.ui.cb_languages_2.currentText()               # Получаем значение с ComboBox

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

        self.translate(lang1_1, lang1_2)           # Вызываем функцию с параметрами языков

    @staticmethod
    def ask_clicked():
        cust = DialogWinASK()                      # Вызов класса диалогового окна
        if cust.exec_():                           # Честно, хз что это и зачем))) Пусть будет))
            print('get')

    def keyPressEvent(self, event):                # Функция чтения клавишь Return & Enter
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:   # Проверяем нажатие клавишь
            self.check_lang_boxes()                      # Вызываем функцию             #       Return & Enter

    def lang_switch(self):                               # Функция смены языков местами
        # Получаем индекс активного языка
        idx_lang1 = self.ui.cb_languages_1.findText(self.ui.cb_languages_1.currentText())
        idx_lang2 = self.ui.cb_languages_2.findText(self.ui.cb_languages_2.currentText())

        self.ui.cb_languages_1.setCurrentIndex(idx_lang2)    # Меняем языки местами по индексу
        self.ui.cb_languages_2.setCurrentIndex(idx_lang1)    # Меняем языки местами по индексу

    @staticmethod
    def write_w(word, translate_text):                       # Функция чтения\записи переведённых слов
        list_words = []
        write_word = word + " --> " + translate_text + "\n"  # Склеиваем слова для записи (Перевести --> Перевод \n)

        with open("BD_Word.txt", "r") as BD_Word:       # Открываем файл на чтение
            for i in BD_Word:                           # Читаем файл построчно
                list_words.append(i)                    # Записываем каждую строку в список

        with open("BD_Word.txt", 'a') as BD_Word:       # Открываем файл на дозапись
            fuzz_coef = fuzz_p.extractOne(write_word, list_words)   # Выполняем нечёткое сравнение слов
            if fuzz_coef[1] < 100:                       # Если не нашлось похожих слов то записываем
                BD_Word.write(write_word)                # Записываем слово в словарь

    # Нужно доработать эту функцию либо удалить к ххх
    def mousePressEvent(self, event):
        button = event.button()
        self.GrayLang()
        if button == Qt.Qt.RightButton:
            print("Right button click!")

        elif button == Qt.Qt.LeftButton:
            print("Left button click!")
        # return Qt.QPushButton.mousePressEvent(self, event)

    # МНОГОПОТОЧНЫЕ ФУНКИИ
    # Функция проверки интернета     !!!ЕСТЬ БАГ!!! При восстановлении подключения иногда УИ может зависнуть намертво
    def thread_internet_check(self):
        while True:
            sleep(1)
            conn = httplib.HTTPConnection("www.google.com")
            try:
                conn.request("HEAD", "/")
                self.ui.line_translate_1.setEnabled(True)   # Обратное включение строки ввода "Translatable"
                print("Есть инте")                          # Принт для дебага (Того самого {Строка 114 описано})
            except None:
                self.ui.line_translate_1.setEnabled(False)  # Отключение строки ввода "Translatable"
                print("Нету инета")                         # Принт для дебага (Того самого {Строка 114 описано})

    # Функция проверки переключателя языков(ComboBox) Написано колхозно как по мне НО РАБОТАЕТ))
    def gray_lang(self):
        idx_lang1_1 = 0                         # Инициализируем переменную для подальшего использования в сравнении
        model = self.ui.cb_languages_2.model()  # Получаем объект QStandardItem
        model.item(0).setEnabled(False)         # По стоку выключаем первый предмет из ComboBox(Первым есть "English")
        while True:
            sleep(1)                            # Сон на одну сек
            # Получаем индекс активного языка
            idx_lang1 = self.ui.cb_languages_1.findText(self.ui.cb_languages_1.currentText())
            idx_lang2 = self.ui.cb_languages_2.findText(self.ui.cb_languages_2.currentText())
            if idx_lang1 != idx_lang1_1:
                # QStandardItemModel, метод model.item возвращает объекты QStandardItem
                model = self.ui.cb_languages_2.model()
                model.item(0).setEnabled(True)           # Включаем все предметы (подготавливаем их)
                model.item(1).setEnabled(True)           # Включаем все предметы (подготавливаем их)
                model.item(2).setEnabled(True)           # Включаем все предметы (подготавливаем их)
                model.item(idx_lang1).setEnabled(False)  # Указываем какие элементы сделать неактивными
                if idx_lang1 == idx_lang2:
                    self.ui.cb_languages_2.setCurrentIndex(idx_lang1_1)  #
                idx_lang1_1 = idx_lang1


class DialogWinASK(QDialog):
    def __init__(self):
        # Setup
        super(DialogWinASK, self).__init__()

        self.ASKui = Ui_ASKDialogWin()
        self.ASKui.setupUi(self)

        list_words = []

        with open('BD_Word.txt', mode="r") as BD_Word:  # Открываем файл на чтение
            for line in BD_Word.readlines():            # Читаем файл построчно
                list_words.append(line)                 # Записываем слова в список

        rand_word = list_words[rd.randint(0, len(list_words))]       # Выбераем рандомное слово из списка
        word = rand_word.partition(' --> ')[-3]            # Убераем вторую половину слова (Перевод)
        self.word1 = rand_word.partition(' --> ')[2]       # Убираем первую чась
        self.word1 = self.word1[:-1]                       # Убираем из слова "\n"
        self.ASKui.line_ask_word.setText(word)             # Вписываем слово в QEditLine

    def check_trans_word(self):                            # Проверка правельности перевода
        translate = self.ASKui.line_ask_tord_trans.text()  # Записываем в переменную перевод который вписали в QEditLine
        fuzz_coef = fuzz.token_sort_ratio(self.word1, translate)     # Выполняем нечёткое сравнение слов
        try:                                               # Отлов ошибки пустой QEditLine
            if fuzz_coef >= 90:                            # Если коэф. схожести слов >= 90
                print("Слово совпадает")
            else:                                          # Иначе ...
                print("Слово не совпадает")
        except TypeError:
            self.ASKui.line_ask_tord_trans.setPlaceholderText("Введите перевод!!!")     # Если стройка ввода была пустой

    def keyPressEvent(self, event):                             # Функция чтения клавишь Return & Enter
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:   # Проверяем нажатие клавишь
            self.check_trans_word()                             # Вызов функции проверки перевода


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

# Made by DeSkreeツ
# :)
