# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TranslationTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TranslationTable(object):
    def setupUi(self, TranslationTable):
        TranslationTable.setObjectName("TranslationTable")
        TranslationTable.resize(447, 370)
        self.verticalLayoutWidget = QtWidgets.QWidget(TranslationTable)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(2, 5, 441, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_dict = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_dict.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_dict.setLineWidth(1)
        self.table_dict.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_dict.setAlternatingRowColors(False)
        self.table_dict.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.table_dict.setTextElideMode(QtCore.Qt.ElideRight)
        self.table_dict.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_dict.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_dict.setShowGrid(True)
        self.table_dict.setColumnCount(4)
        self.table_dict.setObjectName("table_dict")
        self.table_dict.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_dict.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dict.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dict.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dict.setHorizontalHeaderItem(3, item)
        self.table_dict.horizontalHeader().setVisible(True)
        self.table_dict.horizontalHeader().setCascadingSectionResizes(False)
        self.table_dict.horizontalHeader().setDefaultSectionSize(100)
        self.table_dict.horizontalHeader().setHighlightSections(True)
        self.table_dict.horizontalHeader().setMinimumSectionSize(50)
        self.table_dict.horizontalHeader().setSortIndicatorShown(False)
        self.table_dict.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout.addWidget(self.table_dict)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_ok_del = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_ok_del.setObjectName("pb_ok_del")
        self.horizontalLayout_2.addWidget(self.pb_ok_del)
        self.pb_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_cancel.setObjectName("pb_cancel")
        self.horizontalLayout_2.addWidget(self.pb_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(TranslationTable)
        QtCore.QMetaObject.connectSlotsByName(TranslationTable)

    def retranslateUi(self, TranslationTable):
        _translate = QtCore.QCoreApplication.translate
        TranslationTable.setWindowTitle(_translate("TranslationTable", "Dialog"))
        item = self.table_dict.horizontalHeaderItem(0)
        item.setText(_translate("TranslationTable", "Переводимае"))
        item = self.table_dict.horizontalHeaderItem(1)
        item.setText(_translate("TranslationTable", " --> "))
        item = self.table_dict.horizontalHeaderItem(2)
        item.setText(_translate("TranslationTable", "Перевод"))
        item = self.table_dict.horizontalHeaderItem(3)
        item.setText(_translate("TranslationTable", "DELETE"))
        self.pb_ok_del.setText(_translate("TranslationTable", "Ок"))
        self.pb_cancel.setText(_translate("TranslationTable", "Отмена"))

# Made by DeSkreeツ
# :)
