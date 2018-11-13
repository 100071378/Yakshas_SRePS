# -*- coding: utf-8 -*-
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

        def addstock(self):

                db = pymysql.connect("localhost", "root", "", "pharmacy")
                cursor = db.cursor()
                print('db opened')

                pid = str(self.pID.text())
                print(pid)

                name = str(self.pname.text())
                print(name)

                brand = str(self.brand.text())
                print(brand)

                quantity = str(self.qnty.text())
                print(quantity)

                price = str(self.price.text())
                print(price)

                sql = """INSERT INTO stock (pID, pname, brand, quantity, price) VALUES 
                ('%s', '%s', '%s', '%s', '%s')""" % (pid, name, brand, quantity, price)

                try:
                        cursor.execute(sql)
                        print('Data inserted successfuly!')
                        db.commit()
                except:
                        db.rollback()

                db.close()
                print('db closed')


        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(450, 450)
                MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(100, 40, 251, 51))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(24)
                font.setBold(True)
                font.setWeight(75)

                self.label.setFont(font)
                self.label.setStyleSheet("")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(70, 130, 71, 16))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("")
                self.label_2.setObjectName("label_2")

                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(70, 170, 91, 16))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("")
                self.label_3.setObjectName("label_3")

                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(70, 210, 47, 13))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("")
                self.label_4.setObjectName("label_4")

                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(70, 250, 61, 16))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("")
                self.label_5.setObjectName("label_5")

                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(70, 290, 47, 13))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("")
                self.label_6.setObjectName("label_6")

                self.pID = QtWidgets.QLineEdit(self.centralwidget)
                self.pID.setGeometry(QtCore.QRect(200, 130, 171, 20))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.pID.setFont(font)
                self.pID.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.pID.setObjectName("pID")

                self.pname = QtWidgets.QLineEdit(self.centralwidget)
                self.pname.setGeometry(QtCore.QRect(200, 170, 171, 20))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.pname.setFont(font)
                self.pname.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.pname.setObjectName("pname")

                self.brand = QtWidgets.QLineEdit(self.centralwidget)
                self.brand.setGeometry(QtCore.QRect(200, 210, 171, 20))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.brand.setFont(font)
                self.brand.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.brand.setObjectName("brand")

                self.qnty = QtWidgets.QLineEdit(self.centralwidget)
                self.qnty.setGeometry(QtCore.QRect(200, 250, 171, 20))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.qnty.setFont(font)
                self.qnty.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.qnty.setObjectName("qnty")

                self.price = QtWidgets.QLineEdit(self.centralwidget)
                self.price.setGeometry(QtCore.QRect(200, 290, 171, 20))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.price.setFont(font)
                self.price.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.price.setObjectName("price")

                self.addbtn = QtWidgets.QPushButton(self.centralwidget)
                self.addbtn.setGeometry(QtCore.QRect(100, 350, 75, 23))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.addbtn.setFont(font)
                self.addbtn.setStyleSheet("background-color: rgb(150, 150, 150);")
                self.addbtn.setObjectName("addbtn")
                self.addbtn.clicked.connect(self.addstock)

                self.backbtn = QtWidgets.QPushButton(self.centralwidget)
                self.backbtn.setGeometry(QtCore.QRect(250, 350, 75, 23))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.backbtn.setFont(font)
                self.backbtn.setStyleSheet("background-color: rgb(145, 145, 145);")
                self.backbtn.setObjectName("backbtn")
                self.backbtn.clicked.connect(self.exit)

                self.line = QtWidgets.QFrame(self.centralwidget)
                self.line.setGeometry(QtCore.QRect(60, 90, 331, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.line.setFont(font)
                self.line.setLineWidth(2)
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")

                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def exit(self):
                sys.exit()

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Yaksha SRePs"))
                self.label.setText(_translate("MainWindow", "Add In-stock Data"))
                self.label_2.setText(_translate("MainWindow", "Product ID"))
                self.label_3.setText(_translate("MainWindow", "Product Name"))
                self.label_4.setText(_translate("MainWindow", "Brand"))
                self.label_5.setText(_translate("MainWindow", "Quantity"))
                self.label_6.setText(_translate("MainWindow", "Price"))
                self.addbtn.setText(_translate("MainWindow", "Add"))
                self.backbtn.setText(_translate("MainWindow", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

