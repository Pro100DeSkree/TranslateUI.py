# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ASKWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ASKDialogWin(object):
    def setupUi(self, ASKDialogWin):
        ASKDialogWin.setObjectName("ASKDialogWin")
        ASKDialogWin.resize(376, 104)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ASKDialogWin)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 2, 291, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.all_line_word = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.all_line_word.setContentsMargins(0, 0, 0, 0)
        self.all_line_word.setObjectName("all_line_word")
        self.line_ask_word = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_ask_word.setReadOnly(True)
        self.line_ask_word.setObjectName("line_ask_word")
        self.all_line_word.addWidget(self.line_ask_word)
        self.line_ask_tord_trans = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_ask_tord_trans.setObjectName("line_ask_tord_trans")
        self.all_line_word.addWidget(self.line_ask_tord_trans)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(ASKDialogWin)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(7, 57, 361, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.AllButton = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.AllButton.setContentsMargins(0, 0, 0, 0)
        self.AllButton.setObjectName("AllButton")
        self.pb_cancellation = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pb_cancellation.setObjectName("pb_cancellation")
        self.AllButton.addWidget(self.pb_cancellation)
        self.pb_verify = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pb_verify.setObjectName("pb_verify")
        self.AllButton.addWidget(self.pb_verify)
        self.pb_next_words = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pb_next_words.setObjectName("pb_next_words")
        self.AllButton.addWidget(self.pb_next_words)

        self.retranslateUi(ASKDialogWin)
        QtCore.QMetaObject.connectSlotsByName(ASKDialogWin)

    def retranslateUi(self, ASKDialogWin):
        _translate = QtCore.QCoreApplication.translate
        ASKDialogWin.setWindowTitle(_translate("ASKDialogWin", "Dialog"))
        self.line_ask_tord_trans.setPlaceholderText(_translate("ASKDialogWin", "Translate"))
        self.pb_cancellation.setText(_translate("ASKDialogWin", "Хз"))
        self.pb_verify.setText(_translate("ASKDialogWin", "Проверить"))
        self.pb_next_words.setText(_translate("ASKDialogWin", "Следующий"))
