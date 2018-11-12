import sys
import pymysql
from PyQt5 import QtWidgets, QtGui

class Instockwindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()

        self.initGUI()

        self.window.setWindowTitle("Yaksha SRePS Pharmacy")
        self.window.setGeometry(400,100, 500,550)
        self.window.setStyleSheet("border:3px solid #4e4e4e; background-color:#6e6e6e")
        self.window.setWindowIcon(QtGui.QIcon("C:/Users/Yaksha/Desktop/Yaksha Solution/GUI/Final Demo/yaksha.jpg"))

        self.window.show()
        sys.exit(self.app.exec())

    def initGUI(self):

        self.label = QtWidgets.QLabel(self.window)
        self.label.setGeometry(0,50,600,50)
        self.label.setText("Add In-Stock Data")
        self.label.setStyleSheet("font: bold 20px; color: white; background-color: black; padding-left: 150px");

        self.productid1 = QtWidgets.QLabel(self.window)
        self.productid1.setGeometry(80, 150, 250, 40)
        self.productid1.setText("Product ID")
        self.productid1.setStyleSheet("font: bold 16px; border: none")
        self.productid = QtWidgets.QTextEdit(self.window)
        self.productid.setGeometry(200,150, 250,40)
        self.productid.setStyleSheet("font: bold 16px")

        self.category = QtWidgets.QLabel(self.window)
        self.category.setGeometry(80, 200, 250, 40)
        self.category.setText("Category")
        self.category.setStyleSheet("font: bold 16px; border: none")
        self.category = QtWidgets.QTextEdit(self.window)
        self.category.setGeometry(200, 200, 250, 40)
        self.category.setStyleSheet("font: bold 16px")

        self.name1 = QtWidgets.QLabel(self.window)
        self.name1.setGeometry(80, 250, 250, 40)
        self.name1.setText("Item Name")
        self.name1.setStyleSheet("font: bold 16px; border: none")
        self.name = QtWidgets.QTextEdit(self.window)
        self.name.setGeometry(200,250, 250,40)
        self.name.setStyleSheet("font: bold 16px")

        self.brand1 = QtWidgets.QLabel(self.window)
        self.brand1.setText("Brand")
        self.brand1.setStyleSheet("font: bold 16px; border: none")
        self.brand1.setGeometry(80,300,250,40)
        self.brand = QtWidgets.QTextEdit(self.window)
        self.brand.setGeometry(200, 300, 250, 40)
        self.brand.setStyleSheet("font: bold 16px")

        self.Quantity1 = QtWidgets.QLabel(self.window)
        self.Quantity1.setText("Quantity")
        self.Quantity1.setStyleSheet("font: bold 16px; border: none")
        self.Quantity1.setGeometry(80, 350, 250, 40)
        self.quantity = QtWidgets.QTextEdit(self.window)
        self.quantity.setGeometry(200,350, 250, 40)
        self.quantity.setStyleSheet("font: bold 16px")

        self.price1 = QtWidgets.QLabel(self.window)
        self.price1.setText("Price RM")
        self.price1.setStyleSheet("font: bold 16px; border: none")
        self.price1.setGeometry(80, 400, 250, 40)
        self.price = QtWidgets.QTextEdit(self.window)
        self.price.setGeometry(200, 400, 250, 40)
        self.price.setStyleSheet("font: bold 16px")

        self.addbtn = QtWidgets.QPushButton("Add", self.window)
        self.addbtn.setGeometry(50,475,150,50)
        self.addbtn.setStyleSheet("background-color: silver; font: bold 16px")
        self.addbtn.clicked.connect(self.Adddata)


        self.exitbtn = QtWidgets.QPushButton("Exit", self.window)
        self.exitbtn.setGeometry(300, 475, 150, 50)
        self.exitbtn.setStyleSheet("background-color: silver; font: bold 16px")
        self.exitbtn.clicked.connect(self.closeapp)

    def closeapp(self):
        sys.exit()

    def Adddata(self):
        pid = self.productid.text()
        iname = self.name.text()
        brand = self.brand.text()
        quantity = self.quantity.text()

        db = pymysql.connect("localhost", "root", "", "pharmacy")
        cursor = db.cursor()

        sql = "INSERT INTO stock (pID, pname, brand, quantity, price)"
        sql1 = sql + "VALUES ('"+pid+", "+iname+", "+brand+", "+quantity+"')"

        cursor.excute(sql1)
        db.commit()
        db.close()


main = Instockwindow()
