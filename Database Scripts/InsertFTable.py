# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Insertfromtable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Window(object):

    def InsertData(self):

        db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")
        cursor = db.cursor()

        for row in range(3):
            ProductID = str(self.tableWidget.item(row, 0).text())
            Category = str(self.tableWidget.item(row, 1).text())
            Brand = str(self.tableWidget.item(row, 2).text())
            Name = str(self.tableWidget.item(row, 3).text())
            StockNo = str(self.tableWidget.item(row, 4).text())
            Price = str(self.tableWidget.item(row, 5).text())

            sql = """INSERT INTO product (prodID, category, brand, name, instockNo, Price) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % (''.join(ProductID), ''.join(Category), ''.join(Brand), ''.join(Name), ''.join(StockNo), ''.join(Price))
            cursor.execute(sql)
            print('Data inserted successfuly!')
            db.commit()

        db.close()

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(692, 430)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 621, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.btndataInsert = QtWidgets.QPushButton(self.centralwidget)
        self.btndataInsert.setGeometry(QtCore.QRect(290, 250, 75, 23))
        self.btndataInsert.setObjectName("btndataInsert")

        self.btndataInsert.clicked.connect(self.InsertData)

        Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)


    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Window"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Window", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Window", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Window", "3"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Window", "Stock Number"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Window", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Window", "Category"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Window", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Window", "Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Window", "Price"))
        self.btndataInsert.setText(_translate("Window", "Insert Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Windows = QtWidgets.QMainWindow()
    ui = Window()
    ui.setupUi(Windows)
    Windows.show()
    sys.exit(app.exec_())

