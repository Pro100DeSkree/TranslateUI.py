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
        TranslateAPP.resize(546, 189)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TranslateAPP.sizePolicy().hasHeightForWidth())
        TranslateAPP.setSizePolicy(sizePolicy)
        TranslateAPP.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(TranslateAPP)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(4, 80, 540, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.ButtonGroup = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.ButtonGroup.setContentsMargins(0, 0, 0, 0)
        self.ButtonGroup.setObjectName("ButtonGroup")
        self.LanguagesBox = QtWidgets.QGridLayout()
        self.LanguagesBox.setObjectName("LanguagesBox")
        self.Languages_2 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.Languages_2.setObjectName("Languages_2")
        self.LanguagesBox.addWidget(self.Languages_2, 1, 2, 1, 1)
        self.Languages_1 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.Languages_1.setObjectName("Languages_1")
        self.LanguagesBox.addWidget(self.Languages_1, 1, 0, 1, 1)
        self.Arrow = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Arrow.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Arrow.setReadOnly(True)
        self.Arrow.setObjectName("Arrow")
        self.LanguagesBox.addWidget(self.Arrow, 1, 1, 1, 1)
        self.ButtonGroup.addLayout(self.LanguagesBox, 0, 1, 1, 1)
        self.ASK_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ASK_Button.setObjectName("ASK_Button")
        self.ButtonGroup.addWidget(self.ASK_Button, 0, 0, 1, 1)
        self.Translate = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.Translate.setObjectName("Translate")
        self.ButtonGroup.addWidget(self.Translate, 0, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(4, 0, 540, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.AllLineTranslate = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.AllLineTranslate.setContentsMargins(0, 0, 0, 0)
        self.AllLineTranslate.setObjectName("AllLineTranslate")
        self.GroupTranslate_1 = QtWidgets.QGridLayout()
        self.GroupTranslate_1.setObjectName("GroupTranslate_1")
        self.LineTranslate_1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.LineTranslate_1.setText("")
        self.LineTranslate_1.setObjectName("LineTranslate_1")
        self.GroupTranslate_1.addWidget(self.LineTranslate_1, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GroupTranslate_1.addItem(spacerItem, 0, 0, 1, 1)
        self.LabelTranslate_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.LabelTranslate_1.setObjectName("LabelTranslate_1")
        self.GroupTranslate_1.addWidget(self.LabelTranslate_1, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GroupTranslate_1.addItem(spacerItem1, 0, 2, 1, 1)
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
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(123, 120, 263, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TimeSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeSpinBox.sizePolicy().hasHeightForWidth())
        self.TimeSpinBox.setSizePolicy(sizePolicy)
        self.TimeSpinBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.TimeSpinBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.TimeSpinBox.setBaseSize(QtCore.QSize(0, 0))
        self.TimeSpinBox.setMaximum(60)
        self.TimeSpinBox.setObjectName("TimeSpinBox")
        self.horizontalLayout.addWidget(self.TimeSpinBox)
        self.ASK_CheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.ASK_CheckBox.setObjectName("ASK_CheckBox")
        self.horizontalLayout.addWidget(self.ASK_CheckBox)
        TranslateAPP.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TranslateAPP)
        self.statusbar.setObjectName("statusbar")
        TranslateAPP.setStatusBar(self.statusbar)

        self.retranslateUi(TranslateAPP)
        QtCore.QMetaObject.connectSlotsByName(TranslateAPP)

    def retranslateUi(self, TranslateAPP):
        _translate = QtCore.QCoreApplication.translate
        TranslateAPP.setWindowTitle(_translate("TranslateAPP", "Translate"))
        self.Arrow.setText(_translate("TranslateAPP", "➡➡➡"))
        self.ASK_Button.setText(_translate("TranslateAPP", "Спросить"))
        self.Translate.setText(_translate("TranslateAPP", "Перевести"))
        self.LineTranslate_1.setPlaceholderText(_translate("TranslateAPP", "Translatable"))
        self.LabelTranslate_1.setText(_translate("TranslateAPP", "Перевести"))
        self.LineTranslate_2.setPlaceholderText(_translate("TranslateAPP", "Translated"))
        self.LabelTranslate_2.setText(_translate("TranslateAPP", "Перевод"))
        self.ASK_CheckBox.setText(_translate("TranslateAPP", "Спрашивать переодически"))
