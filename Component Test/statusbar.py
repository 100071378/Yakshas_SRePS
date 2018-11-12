import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot #library to add button

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Shortcut Column status'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title) #title of th console window
        self.setGeometry(self.left, self.top, self.width, self.height) #parameter of the console window

        # code that implements the status
        self.statusBar().showMessage('Im the status of this window.')

        #creating textbox
        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.move(200, 20)
        self.textbox.resize(280, 40)


        """ below is the coding for buttons"""
        button = QtWidgets.QPushButton('CLICK HERE!', self)
        button.setToolTip('Hehe u fat')
        button.move(280,400)

        # connect the button to the on_click function
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Poda Punde!')

        #textbox print what you typed
        textboxValue = self.textbox.text()
        QtWidgets.QMessageBox.question(self, 'The thing you typed',"Intha punde: " + textboxValue, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())