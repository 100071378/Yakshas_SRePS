import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Shortcut(QMainWindow):
    def __init__(self, parent=None):
        super(Shortcut, self).__init__(parent)

        #creates a box layout#
        layout = QHBoxLayout()


        #This is the implementation of the menu tab
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("save")
        file.addAction("quit")

        edit = bar.addMenu('Edit')
        search = bar.addMenu('Search')
        tool = bar.addMenu('Tools')
        help= bar.addMenu('Help')

        #Code for drop down in menu tab#
        exitButton = QAction(QIcon('exit.png'), 'Exitter', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exits this shit')
        exitButton.triggered.connect(self.close)
        file.addAction(exitButton)

        #the code for the side dock of shortcut#
        self.items = QDockWidget("List of Shortcuts", self)
        self.items.setFeatures(QDockWidget.NoDockWidgetFeatures)

            #butttons in the shortcut menu#
        _help = QPushButton("Help!")
        _addRecord = QPushButton("Add Record")
        _editRecord = QPushButton("Edit Record")
        _deleteRecord = QPushButton("Delete Record")
        _stockStatus = QPushButton("Stock Status")
        _itemSummary = QPushButton("Item Summary")
        _switchForm = QPushButton(" Switch Form")
        _export = QPushButton("Export Report")
        _lockScreen = QPushButton("Lock Screen")

        
        ###
        #b1 = QtWidgets.QPushButton("Add Record", self)
        #b1.setToolTip('Hehe u fat')
        #b1.move(480, 200)
        #b2 = QtWidgets.QPushButton("Edit Record", self)
        #b3 = QtWidgets.QPushButton("Delete Record", self)
        #b4 = QtWidgets.QPushButton(" Fuck Me!", self)
        ###


        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.items.setFixedWidth(150)
        #self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)
        self.setMinimumSize(600,400)
        self.setWindowTitle("Shortcut Window")

        self.table_widget = TabWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


        #codes for tabs in the window#
class TabWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #init tab
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)

        #add in tabs
        self.tabs.addTab(self.tab1, "Oru Punde")
        self.tabs.addTab(self.tab2, "Rendu Punde")

        #create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pbutton1 = QPushButton("Click mayire")
        self.tab1.layout.addWidget(self.pbutton1)
        self.tab1.setLayout(self.tab1.layout)

        #add tab to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print('\n')
        for currenttab in self.tableWidget.selectedItems():
            print(currenttab.row(), currenttab.column(), currenttab.text())



def main():
    app = QApplication(sys.argv)
    ex = Shortcut()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()