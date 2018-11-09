# -*- coding: utf-8 -*-
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def login(self):

        db = pymysql.connect("localhost", "root", "", "pharmacy")
        cursor = db.cursor()
        print('db opened')

        usname = str(self.uname.text())
        pword = str(self.pword.text())

        sql = """SELECT * FROM user WHERE username = '%s' AND password = '%s'""", (usname, pword)

        try:
            result = cursor.execute(sql)
            print('result executed')
            db.commit()

            if len(result.fetchall()) > 0:
                print('Logged In Successful')
            else:
                print('Invalid username or password')

        except:
            db.rollback()

        db.close()
        print('db closed')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 500)
        MainWindow.setStyleSheet("background-color: rgb(126, 167, 164);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.logbtn = QtWidgets.QPushButton(self.centralwidget)
        self.logbtn.setGeometry(QtCore.QRect(90, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.logbtn.setFont(font)
        self.logbtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logbtn.setObjectName("logbtn")
        self.logbtn.clicked.connect(self.login)

        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(265, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exitbtn.setFont(font)
        self.exitbtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exitbtn.setObjectName("exitbtn")
        self.exitbtn.clicked.connect(self.closeapp)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 381, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 250, 215))
        self.label_2.setText("")
        self.imagePath = "C:/Users/Hp User/PycharmProjects/New/images/yaksha.jpg"
        self.image = QtGui.QImage(self.imagePath)
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        self.label_2.setPixmap(self.pixmap)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 310, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 350, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.uname = QtWidgets.QLineEdit(self.centralwidget)
        self.uname.setGeometry(QtCore.QRect(185, 310, 185, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.uname.setFont(font)
        self.uname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname.setObjectName("uname")

        self.pword = QtWidgets.QLineEdit(self.centralwidget)
        self.pword.setGeometry(QtCore.QRect(185, 350, 185, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pword.setFont(font)
        self.pword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pword.setObjectName("pword")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 450, 250, 20))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yaksha SRePs"))
        self.logbtn.setText(_translate("MainWindow", "Log In"))
        self.exitbtn.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Please Log In to Yaksha SRePs"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Your trusted pharmarcutical sales managin partner"))

    def closeapp(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

