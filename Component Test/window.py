import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
"""
def window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()

    window.setWindowTitle("Hegain Punde")
    window.setGeometry(50,50,500,500)

    window.show()
    sys.exc_info(app.exec_())

window()"""

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Shortcut Column'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())