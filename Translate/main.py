from PyQt5 import QtWidgets, QtCore               # Импортируем Qt5
from PyQt5.Qt import *
from TranslateUI import Ui_TranslateAPP           # Импорт Главного интерфейса
from ASKWin import Ui_ASKDialogWin                # Импорт Диалогового интерфейса(ASK)
from TranslationTable import Ui_TranslationTable  # Импорт Диалогового интерфейса(Таблица)
from googletrans import Translator                # Импортируем гугл переводчик
from fuzzywuzzy import process as fuzz_p          # Импортируем модуль нечёткого сравнения
from fuzzywuzzy import fuzz                       # Импортируем модуль нечёткого сравнения
from threading import Thread                      # Импортируем модуль многопоточности
from time import sleep                            # Импортируем модуль сна
import random as rd                               # Импортируем модуль рандом
import sys                                        # Импортируем модуль system
import http.client as httplib                     # Импортируем модуль (Хз что за моуль) для порверки подключения к сети


# Диалоговое окно ТАБЛИЦА
class DialogWitTable(QDialog):
    def __init__(self):
        # Setup
        super(DialogWitTable, self).__init__()
        self.TableUI = Ui_TranslationTable()            #
        self.TableUI.setupUi(self)                      #
        self.table_dict = self.TableUI.table_dict       # Скорачтваем надпись(Для удобства)
        self.TableUI.pb_ok_del.clicked.connect(self.write_bd_dict)      # Подключаем кнопку "ок"(удалить, закрыть)
        self.TableUI.pb_cancel.clicked.connect(self.cencel)             # Подключаем кнопку "Отмена"(Омена, закрыть)
        self.dict_w = []            # Объявляем список
        self.reedin_dict()          # Вызываем функцию чтения с БД

    def reedin_dict(self):
        with open('BD_Word.txt', mode="r") as BD_Word:   # Открываем файл на чтение
            for line in BD_Word.readlines():             # Читаем файл построчно
                self.dict_w.append(line)                 # Записываем слова в список
        self.write_table()

    def write_table(self):
        self.TableUI.table_dict.setRowCount(len(self.dict_w))   # Создаём кол-во стр. в соотвецтвии с ко-ом стр. словаря

        for i in range(len(self.dict_w)):              # Заполнение таблицы
            dict_string = self.dict_w[i]               # Получаем конкретную строку из спика
            word = dict_string.partition(' --> ')[-3]  # Убераем вторую половину слова (Перевод)
            word1 = dict_string.partition(' --> ')[2]  # Убираем первую(левую) чась
            word1 = word1[:-1]                         # Убираем из слова "\n"

            pb_delete = QPushButton('DEL {}'.format(i), self)       #
            text = pb_delete.text()                                 #
            pb_delete.clicked.connect(lambda ch, text=text: self.delete_line(text))     # Подключаем кнопку DEL

            # Центрируем елементы в таблице
            word = QtWidgets.QTableWidgetItem(str(word))
            word1 = QtWidgets.QTableWidgetItem(str(word1))
            item = QtWidgets.QTableWidgetItem(str("-->"))
            word.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            word1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

            # Добавляем елементы в таблицу
            self.table_dict.setItem(i, 0, word)
            self.table_dict.setItem(i, 1, item)
            self.table_dict.setItem(i, 2, word1)
            self.table_dict.setCellWidget(i, 3, pb_delete)
        self.table_dict.resizeColumnsToContents()           # Ресайзим(Подстраиваем размер таблицы под елементы)

    def delete_line(self, line):            # Функция удаления елементов
        line = line.partition("DEL ")[2]    # Фильтруем строку получая индекс кнопки(А значит и строки елемента)
        self.dict_w.pop(int(line))          # Удаляем елемент по индексу

    def write_bd_dict(self):                            # Функция записи БД
        with open("BD_Word.txt", 'w') as BD_Word:       # Открываем файл на дозапись
            for i in self.dict_w:                       # Проходим по каждому елементу в списке и записываем его в БД
                BD_Word.write(i)               # Записываем в словарь
        self.close()

    def cencel(self):           # Функция отмены удаления
        self.dict_w.clear()     # Очищаем словарь
        self.close()            # закрываем диалоговое окно

    def keyPressEvent(self, event):              # Функция чтения клавишь
        if event.key() == QtCore.Qt.Key_Escape:  # Проверяем что нажато
            self.cencel()                        # Вызываем функцию отмены и закрытия окна


# Диалоговое окно ВОПРОС
class DialogWinASK(QDialog):
    def __init__(self):
        # Setup
        super(DialogWinASK, self).__init__()
        self.ASKui = Ui_ASKDialogWin()
        self.ASKui.setupUi(self)
        self.setWindowIcon(QIcon('ICON-ASK-win.png'))

        self.ASKui.lb_indicator.setAlignment(Qt.AlignCenter)
        self.ASKui.pb_verify.clicked.connect(self.check_trans_word)
        self.ASKui.pb_show.clicked.connect(self.show_word)
        self.list_words = []

        with open('BD_Word.txt', mode="r") as BD_Word:  # Открываем файл на чтение
            for line in BD_Word.readlines():  # Читаем файл построчно
                self.list_words.append(line)  # Записываем слова в список

        self.rand_translate_words()

    def rand_translate_words(self):
        try:
            rand_word = self.list_words[rd.randint(0, len(self.list_words))]       # Выбераем рандомное слово из списка
            word = rand_word.partition(' --> ')[-3]            # Убераем вторую половину слова (Перевод)
            word1 = rand_word.partition(' --> ')[2]         # Убираем первую чась
            self.word1 = word1[:-1]                              # Убираем из слова "\n"
            self.ASKui.line_ask_word.setText(word)             # Вписываем слово в QEditLine
        except IndexError:
            print("ERROR: Сработал IndexError при выборе случайного слова для вопроса")
            self.rand_translate_words()

    def check_trans_word(self):                            # Проверка правельности перевода
        translate = self.ASKui.line_ask_tord_trans.text()  # Записываем в переменную перевод который вписали в QEditLine
        fuzz_coef = fuzz.token_sort_ratio(self.word1, translate)     # Выполняем нечёткое сравнение слов
        print("Из списка", self.word1, " Сравниваеться с введённым", translate)
        print(fuzz_coef)
        try:                                               # Отлов ошибки пустой QEditLine
            if fuzz_coef >= 90:                            # Если коэф. схожести слов >= 90
                self.ASKui.lb_indicator.setText("Верно")
                self.ASKui.lb_indicator.setStyleSheet("QLabel { color: %s}" % 'green')
                sleep(2)
                self.ASKui.line_ask_tord_trans.setText("")  # Очищаем строку ввода перевода
                self.rand_translate_words()                 # Вызываем функцию для выбора случайного слова
            else:                                           # Иначе ...
                self.ASKui.lb_indicator.setText("Неверно")
                self.ASKui.lb_indicator.setStyleSheet("QLabel { color: %s}" % 'red')
        except TypeError:
            self.ASKui.line_ask_tord_trans.setPlaceholderText("Введите перевод!!!")     # Если стройка ввода была пустой

    def show_word(self):
        self.ASKui.line_ask_tord_trans.setText(self.word1)
        self.ASKui.lb_indicator.setText("Подсказка")
        self.ASKui.lb_indicator.setStyleSheet("QLabel { color: %s}" % 'yellow')

    def keyPressEvent(self, event):                             # Функция чтения клавишь
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:   # Проверяем что нажато
            self.check_trans_word()                             # Вызов функции проверки перевода
        elif event.key() == QtCore.Qt.Key_Escape:               # Проверяем что нажато
            self.close()                                        # Если ESC то закрываем окошко


# Основное окно
class MainWindow(QtWidgets.QMainWindow):
    # Settings
    def __init__(self):
        super(MainWindow, self).__init__()

        self.translator = Translator()
        self.ui = Ui_TranslateAPP()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('IconApp.png'))

        self.frame_geometry = None  # !!!

        self.ui.cb_rand_ask.setChecked(True)                            # По умолчанию флаг включён
        self.ui.pb_translate.clicked.connect(self.check_lang_boxes)     # При нажатии кнопки "Перевод" вызываем функцию
        self.ui.pb_ask.clicked.connect(self.ask_translate_words)        # При нажатии кнопки "Спросить" вызываем функцию
        self.ui.tab_app.tabBarClicked.connect(self.set_window_size)
        self.ui.pb_del_translate.clicked.connect(self.table_view)
        self.ui.pb_lang_switcher.clicked.connect(self.lang_switch)             # Кнопка смены языка
        self.ui.cb_languages_1.addItems(["English", "Russian", "Ukraine"])     # Задаём список языков в QComboBox1
        self.ui.cb_languages_2.addItems(["English", "Russian", "Ukraine"])     # Задаём список языков в QComboBox2
        self.ui.cb_languages_2.setCurrentIndex(1)                              # Устанавливаем язык в ComboBox
        th_ch_internet = Thread(target=self.thread_internet_check, args=(), daemon=True)  # Создаём новый поток
        th_ch_gray_lang = Thread(target=self.thread_gray_lang, args=(), daemon=True)      # Создаём новый поток
        th_rand_ask = Thread(target=self.thread_random_ask, args=(), daemon=True)         # Создаём новый поток 
        th_rand_ask.start()                  # Запускаем поток роботы с вопросами (Функция thread_random_ask)
        th_ch_gray_lang.start()              # Запускаем поток проверки ComboBox-ов на смену языков
        th_ch_internet.start()               # Запускаме поток проверки подключения к интернету

    # Function
    def translate(self, lang1, lang2):                                          # Функция реагирования на клик
        word = self.ui.line_translate_1.text()                                  # Вывод содержимого поля 1
        if word == "lol":
            print("Сработал lol")
        elif word == "kek":
            print("Сработал kek")
        else:
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

    def set_window_size(self, index):
        if index == 0:
            self.ui.tab_app.setMaximumSize(661, 151)
            pos_size_win = self.pos_win()
            pos_x = int(pos_size_win[0])
            pos_y = int(pos_size_win[1])
            size_x = int(pos_size_win[2])
            size_y = int(pos_size_win[3])
            # print(size_x, "\n", size_y, "\n")
            # print(pos_x, "\n", pos_y, "\n\n")
            application.setGeometry(pos_x + 4, pos_y + 26, 661, 175)
        elif index == 1:
            self.ui.tab_app.setMaximumSize(661, 341)
            pos_size_win = self.pos_win()
            pos_x = int(pos_size_win[0])
            pos_y = int(pos_size_win[1])
            size_x = int(pos_size_win[2])
            size_y = int(pos_size_win[3])
            # print(size_x, "\n", size_y, "\n")
            # print(pos_x, "\n", pos_y, "\n\n")
            application.setGeometry(pos_x + 4, pos_y + 26, 661, 364)
        elif index == 2:
            print("3")
            pass

    def pos_win(self):
        if self.frame_geometry != self.frameGeometry():
            self.frame_geometry = self.frameGeometry()
            self.frame_geometry = str(self.frame_geometry)
            # Достаём все 4-ре значения
            frame_geometry = self.frame_geometry.partition('(')[2]
            frame_geometry = frame_geometry.partition(')')[-3]
            # Достаём позицыю окна(Х)
            frame_pos_x = frame_geometry.partition(',')[-3]
            # Достаём позицыю окна(Y)
            frame_geometry = frame_geometry.partition(' ')[2]
            frame_pos_y = frame_geometry.partition(',')[-3]
            # Достаём размер окна(X)
            frame_geometry = frame_geometry.partition(' ')[2]
            frame_geometry_x = frame_geometry.partition(',')[-3]
            # Достаём размер окна(Y)
            frame_geometry = frame_geometry.partition(' ')[2]
            frame_geometry_y = frame_geometry.partition(',')[-3]

            return [frame_pos_x, frame_pos_y, frame_geometry_x, frame_geometry_y]


    @staticmethod
    def ask_translate_words():
        cust = DialogWinASK()                      # Вызов класса диалогового окна
        if cust.exec_():                           # Честно, хз что это и зачем))) Пусть будет))
            print('get')

    def keyPressEvent(self, event):                # Функция чтения клавишь Return & Enter
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:   # Проверяем нажатие клавишь
            self.check_lang_boxes()                # Вызываем функцию                   #       Return & Enter

    def lang_switch(self):                         # Функция смены языков местами
        # Получаем индекс активного языка
        idx_lang1 = self.ui.cb_languages_1.findText(self.ui.cb_languages_1.currentText())
        idx_lang2 = self.ui.cb_languages_2.findText(self.ui.cb_languages_2.currentText())

        self.ui.cb_languages_1.setCurrentIndex(idx_lang2)    # Меняем языки местами по индексу
        self.ui.cb_languages_2.setCurrentIndex(idx_lang1)    # Меняем языки местами по индексу

    def write_w(self, word, translate_text):                 # Функция чтения\записи переведённых слов
        list_words = self.reed_bd_word()
        write_word = word + " --> " + translate_text + "\n"  # Склеиваем слова для записи (Перевести --> Перевод \n)

        if list_words:
            fuzz_coef = fuzz_p.extractOne(write_word, list_words)  # Выполняем нечёткое сравнение слов
            if fuzz_coef[1] < 100:                                 # Если не нашлось похожих слов то записываем
                self.addit_rec_bd_word(write_word)                 # Передаём данные в функцию записи
        else:
            self.addit_rec_bd_word(write_word)                     # Передаём данные в функцию записи

    def reed_bd_word(self):
        list_words = []

        with open("BD_Word.txt", "r") as BD_Word:        # Открываем файл на чтение
            for i in BD_Word:                            # Читаем файл построчно
                list_words.append(i)                     # Записываем каждую строку в список

        return list_words

    def addit_rec_bd_word(self, write_word):
        with open("BD_Word.txt", 'a') as BD_Word:   # Открываем файл на дозапись
            BD_Word.write(write_word)               # Записываем слово в словарь

    def spin_boxes_value(self):
        ask_time_min = self.ui.sb_time_min.value()
        ask_time_max = self.ui.sb_time_max.value()
        return [ask_time_min, ask_time_max]

    @staticmethod
    def table_view():
        cust = DialogWitTable()
        if cust.exec_():
            print('get')

# -----------------------------------------------МНОГОПОТОЧНЫЕ ФУНКИИ-----------------------------------------------
    # Функция проверки интернета     !!!ЕСТЬ БАГ!!! При восстановлении подключения иногда УИ может зависнуть намертво
    def thread_internet_check(self):
        while True:
            sleep(1)
            conn = httplib.HTTPConnection("www.google.com")
            try:
                conn.request("HEAD", "/")
                self.ui.line_translate_1.setEnabled(True)   # Обратное включение строки ввода "Translatable"
                # print("Есть инте")                          # Принт для дебага (Того самого {Строка 114 описано})
            except None:
                self.ui.line_translate_1.setEnabled(False)  # Отключение строки ввода "Translatable"
                print("Нету инета")                         # Принт для дебага (Того самого {Строка 114 описано})

    # Функция проверки переключателя языков(ComboBox) Написано колхозно как по мне, НО РАБОТАЕТ))
    def thread_gray_lang(self):
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

    # Нужно как то переделать это всё (При истичению таймера и открытии окна лезит куча "Ошибок" Не критично но....)
    def thread_random_ask(self):
        while True:
            global flag
            if self.ui.cb_rand_ask.isChecked():
                spin_box_min_max = self.spin_boxes_value()          # Получаем значения из спинбоксов
                time_interval_ask = rd.randint(spin_box_min_max[0], spin_box_min_max[1])
                time_interval_ask = time_interval_ask * 60          # Переводим значение с мин в сек
                for i in range(time_interval_ask):                  # Таймер сделан через for для прирывания sleep
                    time_interval = time_interval_ask - i           # От основного времени отнимаем i(Обратный отсчёт)
                    self.ui.lb_timer.setText(str(time_interval))    # Переводим в str и изменяем значение Qlabel
                    sleep(1)
                    flag = self.ui.cb_rand_ask.isChecked()          # Получаем значение QCheckBox (ЧБ)
                    if flag != 1:                                   # Если чекбокс выключен то прирываем for
                        self.ui.lb_timer.setText("--")              # Сбрасываем счётчик "таймера"
                        break                                       # Прирываем цыкл for
                if flag:                    # Если ЧБ true то запускаем окно
                    cust = DialogWinASK()
                    if cust.exec_():
                        print('get')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

# Made by DeSkreeツ
# :)
