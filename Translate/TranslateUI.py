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
        TranslateAPP.resize(547, 148)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TranslateAPP.sizePolicy().hasHeightForWidth())
        TranslateAPP.setSizePolicy(sizePolicy)
        TranslateAPP.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(TranslateAPP)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(3, 79, 540, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.ButtonGroup = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.ButtonGroup.setContentsMargins(0, 0, 0, 0)
        self.ButtonGroup.setObjectName("ButtonGroup")
        self.LanguagesBox = QtWidgets.QGridLayout()
        self.LanguagesBox.setObjectName("LanguagesBox")
        self.CB_Languages_2 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.CB_Languages_2.setObjectName("CB_Languages_2")
        self.LanguagesBox.addWidget(self.CB_Languages_2, 1, 2, 1, 1)
        self.CB_Languages_1 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.CB_Languages_1.setObjectName("CB_Languages_1")
        self.LanguagesBox.addWidget(self.CB_Languages_1, 1, 0, 1, 1)
        self.PB_LangSwitcher = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.PB_LangSwitcher.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.PB_LangSwitcher.setFont(font)
        self.PB_LangSwitcher.setIconSize(QtCore.QSize(16, 16))
        self.PB_LangSwitcher.setObjectName("PB_LangSwitcher")
        self.LanguagesBox.addWidget(self.PB_LangSwitcher, 1, 1, 1, 1)
        self.ButtonGroup.addLayout(self.LanguagesBox, 0, 1, 1, 1)
        self.PB_ASK = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.PB_ASK.setMaximumSize(QtCore.QSize(120, 16777215))
        self.PB_ASK.setObjectName("PB_ASK")
        self.ButtonGroup.addWidget(self.PB_ASK, 0, 0, 1, 1)
        self.PB_Translate = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.PB_Translate.setMaximumSize(QtCore.QSize(120, 16777215))
        self.PB_Translate.setObjectName("PB_Translate")
        self.ButtonGroup.addWidget(self.PB_Translate, 0, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(4, 3, 540, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.AllLineTranslate = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.AllLineTranslate.setContentsMargins(0, 0, 0, 0)
        self.AllLineTranslate.setObjectName("AllLineTranslate")
        self.GroupTranslate_1 = QtWidgets.QGridLayout()
        self.GroupTranslate_1.setObjectName("GroupTranslate_1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GroupTranslate_1.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GroupTranslate_1.addItem(spacerItem1, 0, 2, 1, 1)
        self.LineTranslate_1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.LineTranslate_1.setText("")
        self.LineTranslate_1.setObjectName("LineTranslate_1")
        self.GroupTranslate_1.addWidget(self.LineTranslate_1, 1, 0, 1, 3)
        self.LabelTranslate_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.LabelTranslate_1.setObjectName("LabelTranslate_1")
        self.GroupTranslate_1.addWidget(self.LabelTranslate_1, 0, 1, 1, 1)
        self.AllLineTranslate.addLayout(self.GroupTranslate_1)
        self.GroupTranslate_2 = QtWidgets.QGridLayout()
        self.GroupTranslate_2.setObjectName("GroupTranslate_2")
        self.LineTranslate_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.LineTranslate_2.setText("")
        self.LineTranslate_2.setReadOnly(True)
        self.LineTranslate_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.LineTranslate_2.setObjectName("LineTranslate_2")
        self.GroupTranslate_2.addWidget(self.LineTranslate_2, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GroupTranslate_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.LabelTranslate_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.LabelTranslate_2.setObjectName("LabelTranslate_2")
        self.GroupTranslate_2.addWidget(self.LabelTranslate_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GroupTranslate_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.AllLineTranslate.addLayout(self.GroupTranslate_2)
        self.ByDeSkree = QtWidgets.QLabel(self.centralwidget)
        self.ByDeSkree.setGeometry(QtCore.QRect(407, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ByDeSkree.setFont(font)
        self.ByDeSkree.setText("")
        self.ByDeSkree.setObjectName("ByDeSkree")
        TranslateAPP.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TranslateAPP)
        self.statusbar.setObjectName("statusbar")
        TranslateAPP.setStatusBar(self.statusbar)

        self.retranslateUi(TranslateAPP)
        QtCore.QMetaObject.connectSlotsByName(TranslateAPP)

    def retranslateUi(self, TranslateAPP):
        _translate = QtCore.QCoreApplication.translate
        TranslateAPP.setWindowTitle(_translate("TranslateAPP", "Translate"))
        self.PB_LangSwitcher.setText(_translate("TranslateAPP", "↔"))
        self.PB_ASK.setText(_translate("TranslateAPP", "Спросить"))
        self.PB_Translate.setText(_translate("TranslateAPP", "Перевести"))
        self.LineTranslate_1.setPlaceholderText(_translate("TranslateAPP", "Translatable"))
        self.LabelTranslate_1.setText(_translate("TranslateAPP", "Перевести"))
        self.LineTranslate_2.setPlaceholderText(_translate("TranslateAPP", "Translated"))
        self.LabelTranslate_2.setText(_translate("TranslateAPP", "Перевод"))
