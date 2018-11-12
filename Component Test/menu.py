import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.title = "Menu Punde"
        self.left = 10
        self.top = 20
        self.width = 640
        self.height = 240
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('exit.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        #menu coding below
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        #exit button programming
        exitButton = QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Exitter', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exits this shit')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        #sidemenu shortcut button
        b1 = QtWidgets.QPushButton("Add Record",self)
        b1.setToolTip('Hehe u fat')
        b1.move(480, 200)
        b2 = QtWidgets.QPushButton("Edit Record",self)
        b3 = QtWidgets.QPushButton("Delete Record",self)
        b4 = QtWidgets.QPushButton(" Fuck Me!",self)

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())