# -*- coding: utf-8 -*-

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def addsignup(self):

        db = pymysql.connect("localhost", "root", "", "pharmacy")
        cursor = db.cursor()
        print('db opened')


        usname = str(self.uname.text())
        print (usname)
        email = str(self.email.text())
        print(email)
        pword = str(self.pword.text())
        print(pword)
        name = str(self.name.text())
        print(name)

        sqlinsert = """INSERT INTO user (username, password, name, email) VALUES 
        ('%s', '%s', '%s', '%s')""" % (usname, pword, name, email)

        try:
            cursor.execute(sqlinsert)
            print('Data inserted successfuly!')
            db.commit()
        except:
            db.rollback()

        db.close()
        print('db closed')



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 524)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 54, 538, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 9, 90, 33))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(280, 460, 75, 27))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.exitbtn.setFont(font)
        self.exitbtn.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);")
        self.exitbtn.setObjectName("exitbtn")
        self.exitbtn.clicked.connect(self.closeapp)

        #username
        self.uname = QtWidgets.QLineEdit(self.centralwidget)
        self.uname.setGeometry(QtCore.QRect(170, 329, 251, 20))
        self.uname.setObjectName("uname")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 329, 74, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.signbtn = QtWidgets.QPushButton(self.centralwidget)
        self.signbtn.setGeometry(QtCore.QRect(90, 460, 75, 27))
        self.signbtn.clicked.connect(self.addsignup)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signbtn.setFont(font)
        self.signbtn.setMouseTracking(False)
        self.signbtn.setStyleSheet("background-color: rgb(76, 76, 76);\n" "color: rgb(255, 255, 255);")
        self.signbtn.setObjectName("signbtn")

        #email
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 356, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        #full name
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 383, 76, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # password
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 410, 74, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(170, 356, 251, 20))
        self.email.setObjectName("email")

        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(170, 383, 251, 20))
        self.name.setObjectName("name")

        self.pword = QtWidgets.QLineEdit(self.centralwidget)
        self.pword.setGeometry(QtCore.QRect(170, 410, 251, 20))
        self.pword.setObjectName("pword")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(125, 80, 200, 200))
        self.imagePath = "C:/Users/Hp User/PycharmProjects/New/images/anonyman.png"
        self.image = QtGui.QImage(self.imagePath)
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        self.label_7.setPixmap(self.pixmap)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yaksha SRePs"))
        self.label_5.setText(_translate("MainWindow", "Sign up"))
        self.exitbtn.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.signbtn.setText(_translate("MainWindow", "Sign up"))
        self.label_3.setText(_translate("MainWindow", "Email"))
        self.label_4.setText(_translate("MainWindow", "Full Name"))
        self.label_6.setText(_translate("MainWindow", "Password"))


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

