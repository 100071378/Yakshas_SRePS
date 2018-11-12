import sys
import pymysql

from PyQt5 import QtWidgets, QtGui

class LoginWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()

        self.imagePath = "C:/Users/Yaksha/Desktop/Yaksha Solution/GUI/Final Demo/anonyman.png"

        self.initGUI()

        self.window.setWindowTitle("Create an Account")
        self.window.setGeometry(400,100, 400,600)
        self.window.setStyleSheet("border:3px solid #4e4e4e; background-color:#6e6e6e")
        self.window.show()
        sys.exit(self.app.exec())

    def initGUI(self):

        self.label = QtWidgets.QLabel(self.window)
        self.label.setGeometry(90,10,230,230)
        self.image = QtGui.QImage(self.imagePath)
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmap)

        self.uname = QtWidgets.QTextEdit(self.window)
        self.uname.setGeometry(80,260, 250,40)
        self.uname.setPlaceholderText("Username")

        self.email = QtWidgets.QTextEdit(self.window)
        self.email.setGeometry(80,310, 250, 40)
        self.email.setPlaceholderText("Email")

        self.fname = QtWidgets.QTextEdit(self.window)
        self.fname.setGeometry(80, 360, 250, 40)
        self.fname.setPlaceholderText("Full Name")

        self.password = QtWidgets.QTextEdit(self.window)
        self.password.setGeometry(80,410, 250, 40)
        self.password.setPlaceholderText("Password")

        self.signupbtn = QtWidgets.QPushButton("Sign up", self.window)
        self.signupbtn.setGeometry(60,500,120,30)
        self.signupbtn.setStyleSheet("background-color: white")
        self.signupbtn.clicked.connect(self.signup)


        self.exitbtn = QtWidgets.QPushButton("Exit", self.window)
        self.exitbtn.setGeometry(220, 500, 120, 30)
        self.exitbtn.setStyleSheet("background-color: white")
        self.exitbtn.clicked.connect(self.closeapp)

    def closeapp(self):
        sys.exit()

    def signup(self):
        uname = str(self.uname.text())
        password = str(self.password.text())
        name = str(self.fname.text())
        email = str(self.email.text())

        db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")
        cursor = db.cursor()

        sql = """INSERT INTO user (username, password, name, email) VALUES ('%s', '%s', '%s', '%s')""" % (''.join(uname), ''.join(password), ''.join(name), ''.join(email))


        cursor.excute(sql)
        db.commit()
        db.close()

main = LoginWindow()
