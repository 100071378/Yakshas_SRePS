# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from InsertFTable import Ui_MainWindow

class Ui_AddSalesRecord(object):
    def setupUi(self, AddSalesRecord):
        AddSalesRecord.setObjectName("AddSalesRecord")
        AddSalesRecord.resize(480, 621)
        self.centralwidget = QtWidgets.QWidget(AddSalesRecord)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(319, 40, 131, 31))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 10, 10), QtCore.QTime(1, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 210, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 180, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 180, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 280, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(344, 552, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 550, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 550, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 330, 441, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 280, 51, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.InsertData)
        AddSalesRecord.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddSalesRecord)
        self.statusbar.setObjectName("statusbar")
        AddSalesRecord.setStatusBar(self.statusbar)

        self.retranslateUi(AddSalesRecord)
        QtCore.QMetaObject.connectSlotsByName(AddSalesRecord)



    def InsertData(self):
        self.iwindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.iwindow)
        self.iwindow.show()
        # Retrieve text from QLineEdit
        a = self.lineEdit_2.text()
        b = self.lineEdit_3.text()
        c = self.lineEdit_6.text()
        d = self.lineEdit_4.text()
        e = self.lineEdit_5.text()

        # Create a empty row at bottom of table
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        # Add text to the row
        self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(a))
        self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(b))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(c))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(d))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(e))

    def retranslateUi(self, AddSalesRecord):
        _translate = QtCore.QCoreApplication.translate
        AddSalesRecord.setWindowTitle(_translate("AddSalesRecord", "Add Sales Record"))
        self.lineEdit.setText(_translate("AddSalesRecord", "200"))
        self.label.setText(_translate("AddSalesRecord", "Sales ID"))
        self.lineEdit_2.setText(_translate("AddSalesRecord", "189"))
        self.lineEdit_3.setText(_translate("AddSalesRecord", "Maximus Scelories"))
        self.lineEdit_4.setText(_translate("AddSalesRecord", "15"))
        self.lineEdit_5.setText(_translate("AddSalesRecord", "17.50"))
        self.label_2.setText(_translate("AddSalesRecord", "Product ID"))
        self.label_3.setText(_translate("AddSalesRecord", "Product Description"))
        self.label_4.setText(_translate("AddSalesRecord", "Quantity"))
        self.label_5.setText(_translate("AddSalesRecord", "Unit Price (RM)"))
        self.lineEdit_6.setText(_translate("AddSalesRecord", "Tateyama"))
        self.label_6.setText(_translate("AddSalesRecord", "Brand"))
        self.pushButton.setText(_translate("AddSalesRecord", "View Product"))
        self.pushButton_2.setText(_translate("AddSalesRecord", "Confirm"))
        self.pushButton_3.setText(_translate("AddSalesRecord", "Cancel"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("AddSalesRecord", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("AddSalesRecord", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("AddSalesRecord", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AddSalesRecord", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AddSalesRecord", "Product Desc"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AddSalesRecord", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AddSalesRecord", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AddSalesRecord", "Unit Price"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("AddSalesRecord", "192"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("AddSalesRecord", "Skin care"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("AddSalesRecord", "Actimmune"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("AddSalesRecord", "12"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("AddSalesRecord", "13.5"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("AddSalesRecord", "182"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("AddSalesRecord", "Hygiene"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("AddSalesRecord", "Garnier"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("AddSalesRecord", "55"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("AddSalesRecord", "25.3"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("AddSalesRecord", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddSalesRecord = QtWidgets.QMainWindow()
    ui = Ui_AddSalesRecord()
    ui.setupUi(AddSalesRecord)
    AddSalesRecord.show()
    sys.exit(app.exec_())

