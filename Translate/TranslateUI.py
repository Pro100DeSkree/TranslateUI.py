# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TranslateUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TranslateAPP(object):
    def setupUi(self, TranslateAPP):
        TranslateAPP.setObjectName("TranslateAPP")
        TranslateAPP.resize(603, 392)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TranslateAPP.sizePolicy().hasHeightForWidth())
        TranslateAPP.setSizePolicy(sizePolicy)
        TranslateAPP.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(TranslateAPP)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_app = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_app.setGeometry(QtCore.QRect(0, -1, 601, 371))
        self.tab_app.setObjectName("tab_app")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.main_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(2, 3, 591, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.all_line_translate = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.all_line_translate.setContentsMargins(0, 0, 0, 0)
        self.all_line_translate.setObjectName("all_line_translate")
        self.group_translate_1 = QtWidgets.QGridLayout()
        self.group_translate_1.setObjectName("group_translate_1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.group_translate_1.addItem(spacerItem, 0, 2, 1, 1)
        self.label_translate_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_translate_1.setObjectName("label_translate_1")
        self.group_translate_1.addWidget(self.label_translate_1, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.group_translate_1.addItem(spacerItem1, 0, 0, 1, 1)
        self.te_translate_1 = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.te_translate_1.setObjectName("te_translate_1")
        self.group_translate_1.addWidget(self.te_translate_1, 1, 0, 1, 3)
        self.all_line_translate.addLayout(self.group_translate_1)
        self.group_translate_2 = QtWidgets.QGridLayout()
        self.group_translate_2.setObjectName("group_translate_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.group_translate_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_translate_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_translate_2.setObjectName("label_translate_2")
        self.group_translate_2.addWidget(self.label_translate_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.group_translate_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.te_translate_2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.te_translate_2.setObjectName("te_translate_2")
        self.group_translate_2.addWidget(self.te_translate_2, 1, 0, 1, 3)
        self.all_line_translate.addLayout(self.group_translate_2)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.main_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(27, 290, 540, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.button_group = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.button_group.setContentsMargins(0, 0, 0, 0)
        self.button_group.setObjectName("button_group")
        self.languages_box = QtWidgets.QGridLayout()
        self.languages_box.setObjectName("languages_box")
        self.cb_languages_2 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cb_languages_2.setObjectName("cb_languages_2")
        self.languages_box.addWidget(self.cb_languages_2, 1, 2, 1, 1)
        self.cb_languages_1 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cb_languages_1.setObjectName("cb_languages_1")
        self.languages_box.addWidget(self.cb_languages_1, 1, 0, 1, 1)
        self.pb_lang_switcher = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pb_lang_switcher.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.pb_lang_switcher.setFont(font)
        self.pb_lang_switcher.setIconSize(QtCore.QSize(16, 16))
        self.pb_lang_switcher.setObjectName("pb_lang_switcher")
        self.languages_box.addWidget(self.pb_lang_switcher, 1, 1, 1, 1)
        self.button_group.addLayout(self.languages_box, 0, 1, 1, 1)
        self.pb_ask = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pb_ask.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pb_ask.setObjectName("pb_ask")
        self.button_group.addWidget(self.pb_ask, 0, 0, 1, 1)
        self.pb_translate = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pb_translate.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pb_translate.setObjectName("pb_translate")
        self.button_group.addWidget(self.pb_translate, 0, 2, 1, 1)
        self.tab_app.addTab(self.main_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.settings_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 239, 90))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sb_time_min = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sb_time_min.setMinimum(1)
        self.sb_time_min.setMaximum(60)
        self.sb_time_min.setObjectName("sb_time_min")
        self.gridLayout.addWidget(self.sb_time_min, 2, 1, 1, 1)
        self.sb_time_max = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sb_time_max.setMinimum(10)
        self.sb_time_max.setMaximum(60)
        self.sb_time_max.setObjectName("sb_time_max")
        self.gridLayout.addWidget(self.sb_time_max, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)
        self.cb_rand_ask = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_rand_ask.setFont(font)
        self.cb_rand_ask.setObjectName("cb_rand_ask")
        self.gridLayout.addWidget(self.cb_rand_ask, 3, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 4)
        self.lb_timer = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb_timer.setText("")
        self.lb_timer.setObjectName("lb_timer")
        self.gridLayout.addWidget(self.lb_timer, 1, 4, 1, 1)
        self.pb_del_translate = QtWidgets.QPushButton(self.settings_tab)
        self.pb_del_translate.setGeometry(QtCore.QRect(260, 10, 88, 34))
        self.pb_del_translate.setObjectName("pb_del_translate")
        self.tab_app.addTab(self.settings_tab, "")
        TranslateAPP.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TranslateAPP)
        self.statusbar.setObjectName("statusbar")
        TranslateAPP.setStatusBar(self.statusbar)

        self.retranslateUi(TranslateAPP)
        self.tab_app.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TranslateAPP)

    def retranslateUi(self, TranslateAPP):
        _translate = QtCore.QCoreApplication.translate
        TranslateAPP.setWindowTitle(_translate("TranslateAPP", "Translate"))
        self.label_translate_1.setText(_translate("TranslateAPP", "Перевести"))
        self.te_translate_1.setPlaceholderText(_translate("TranslateAPP", "Translatable"))
        self.label_translate_2.setText(_translate("TranslateAPP", "Перевод"))
        self.te_translate_2.setPlaceholderText(_translate("TranslateAPP", "Translated"))
        self.pb_lang_switcher.setText(_translate("TranslateAPP", "↔"))
        self.pb_ask.setText(_translate("TranslateAPP", "Спросить"))
        self.pb_translate.setText(_translate("TranslateAPP", "Перевести"))
        self.tab_app.setTabText(self.tab_app.indexOf(self.main_tab), _translate("TranslateAPP", "Переводчик"))
        self.label.setText(_translate("TranslateAPP", "От"))
        self.label_2.setText(_translate("TranslateAPP", "До"))
        self.label_4.setText(_translate("TranslateAPP", "Мин"))
        self.cb_rand_ask.setText(_translate("TranslateAPP", "Переодически спрашивать"))
        self.label_3.setText(_translate("TranslateAPP", "Случайное время вопроса:"))
        self.pb_del_translate.setText(_translate("TranslateAPP", "Удаление"))
        self.tab_app.setTabText(self.tab_app.indexOf(self.settings_tab), _translate("TranslateAPP", "Налаштуйкы"))
