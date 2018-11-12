import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot #library to add button

class App(QtWidgets.QWidget):

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

        buttonReply = QtWidgets.QMessageBox.question(self, 'dei sunni', 'nee periya pundaiya', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            print('aama sunni')
        else:
            print ('Ille sunni')

        self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())