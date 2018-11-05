import sys
import pymysql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from shit import Ui_MainWindow
#from InsertFTable import Window
from Tableview import Ui_MainWindow
from AddSales import Ui_AddSalesRecord
#from Addinstock import Instockwindow

class Shortcut(QMainWindow):
    def __init__(self, parent=None):
        super(Shortcut, self).__init__(parent)

        #creates a box layout#
        layout = QVBoxLayout(self)
        layout1 = QVBoxLayout(self)

        #This is the implementation of the menu tab
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("Save")

        edit = bar.addMenu('Edit')
        search = bar.addMenu('Search')
        tool = bar.addMenu('Tools')
        help= bar.addMenu('Help')

        #Code for drop down in menu tab#
        exitButton = QAction(QIcon('exit.png'), 'Quit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exits the Application')
        exitButton.triggered.connect(self.close)
        file.addAction(exitButton)

        #the code for the side dock of shortcut#
        self.items = QDockWidget("    List of Shortcuts", self)
        self.items.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockedButton = QWidget(self)
        self.items.setWidget(self.dockedButton)

        self.items.setFloating(False)
        self.items.setFixedWidth(140)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)

        # code for buttons in docked area
        _help = QPushButton("(Ctrl+F1) Help!")
        _help.clicked.connect(self.OpenHelp)
        s_help = QShortcut(QKeySequence("Ctrl+F1"),self)
        s_help.activated.connect(self.OpenHelp)

        _addRecord = QPushButton("(Ctrl+A) Add Record")
        _addRecord.clicked.connect(self.OpenAdd)
        s_add = QShortcut(QKeySequence("Ctrl+A"), self)
        s_add.activated.connect(self.OpenAdd)

        _editRecord = QPushButton("(Ctrl+E) Edit Record")
        # _editRecord.clicked.connect(self.OpenIns)
        # s_edit = QShortcut(QKeySequence("Ctrl+E"), self)
        # s_edit.activated.connect(self.OpenIns)

        _deleteRecord = QPushButton("(Ctrl+D) Delete Record")
        _stockStatus = QPushButton("(Ctrl+S) Stock Status")
        _itemSummary = QPushButton("(Ctrl+I) Item Summary")
        _switchForm = QPushButton("(Ctrl+F) Switch Form")

        _export = QPushButton("(Ctrl+X) Export Report")
        _export.clicked.connect(self.CSV)
        s_export = QShortcut(QKeySequence("Ctrl+X"), self)
        s_export.activated.connect(self.CSV)

        _lockScreen = QPushButton("(Ctrl+L) Lock Screen")
        _desc = QLabel()
        _desc.setText("Shortcut Keys to be\n used with 'Ctrl' Key")
        _desc.setAlignment(Qt.AlignHCenter)

        self.dockedButton.setLayout(layout)
        self.dockedButton.layout().addWidget(_help)
        self.dockedButton.layout().addWidget(_addRecord)
        self.dockedButton.layout().addWidget(_editRecord)
        self.dockedButton.layout().addWidget(_deleteRecord)
        self.dockedButton.layout().addWidget(_stockStatus)
        self.dockedButton.layout().addWidget(_itemSummary)
        self.dockedButton.layout().addWidget(_switchForm)
        self.dockedButton.layout().addWidget(_export)
        self.dockedButton.layout().addWidget(_lockScreen)
        #self.dockedButton.layout().addWidget(_desc)

        self.item = QDockWidget()
        self.item.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockedLeft = QWidget(self)
        self.item.setWidget(self.dockedLeft)

        self.item.setFloating(False)
        self.item.setFixedWidth(100)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.item)
        self.setLayout(layout1)

        # code for buttons in docked area
        addbtn = QPushButton('')
        addbtn.setIcon(QIcon('add.png'))
        addbtn.setIconSize(QSize(75,75))
        addbtn.clicked.connect(self.OpenAdd)


        editbtn = QPushButton('')
        editbtn.setIcon(QIcon('edit.png'))
        editbtn.setIconSize(QSize(75, 75))
        editbtn.clicked.connect(exit)

        deletebtn = QPushButton('')
        deletebtn.setIcon(QIcon('delete.png'))
        deletebtn.setIconSize(QSize(75, 75))
        deletebtn.clicked.connect(exit)

        self.dockedLeft.setLayout(layout1)
        self.dockedLeft.layout().addWidget(addbtn)
        self.dockedLeft.layout().addWidget(editbtn)
        self.dockedLeft.layout().addWidget(deletebtn)

        self.setMinimumSize(600,400)
        self.setWindowTitle("Shortcut Window")
        self.setWindowIcon(QIcon('yaksha.jpg'))

        self.table_widget = TabWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

    def OpenHelp(self):
        self.hwindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.hwindow)
        self.hwindow.show()
    def OpenAdd(self):
        self.awindow = QMainWindow()
        self.ui = Ui_AddSalesRecord()
        self.ui.setupUi(self.awindow)
        self.awindow.show()

    # def OpenIns(self):
    #     self.iwindow = QMainWindow()
    #     self.ui = Instockwindow()
    #     self.ui.setupUi(self.iwindow)
    #     self.iwindow.show()

    def CSV(self):
        db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")
        cursor = db.cursor()

        sql = "SELECT * FROM product"
        cursor.execute(sql)

        file = open("sales.csv", "w")

        for row in cursor:
            file.write(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + '\n')
        file.close()
        cursor.close()
        db.close()

        #codes for tabs in the window#

class TabWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #init tab
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = Dialog()
        self.tabs.resize(300,200)

        #add in tabs
        self.tabs.addTab(self.tab1, "Product Details")
        self.tabs.addTab(self.tab2, "Restock Recommendation")

        #create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pbutton1 = QPushButton("Click Here!")
        self.pbutton1.setToolTip("Close")
        self.pbutton1.clicked.connect(self.OpenProdDet)
        self.textbox = QLineEdit(self)
        self.textbox.setFixedHeight(400)
        self.tab1.layout.addWidget(self.textbox)
        self.tab1.layout.addWidget(self.pbutton1)
        self.tab1.setLayout(self.tab1.layout)


        #add tab to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def OpenProdDet(self):
        self.pwindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.pwindow)
        self.pwindow.show()

    @pyqtSlot()
    def on_click(self):
        print('\n')
        for currenttab in self.tableWidget.selectedItems():
            print(currenttab.row(), currenttab.column(), currenttab.text())

class Dialog(QDialog):


    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(exit)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)

        self.createTableHeader()
        mainLayout.addWidget(self.tableWidget)

        self.createTable()
        mainLayout.addWidget(self.tableWidget)

        self.totalTable()
        mainLayout.addWidget(self.tableWidget)


        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Re-Stock Recommendation")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Sales Order")
        layout = QFormLayout()
        layout.addRow(QLabel("Company:"), QLineEdit())
        QLineEdit().setText("Family Aid Pharmacy Inc.")
        layout.addRow(QLabel("Category:"), QComboBox())
        layout.addRow(QLabel("Order ID:"), QSpinBox())
        self.formGroupBox.setLayout(layout)



    def createTable(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.item = self.tableWidget.setItem(0, 0, QTableWidgetItem("10"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("252"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Vitamin C"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("RM 12.50"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("RM 125"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("15"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("189"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("Panadol Soluble"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("RM 10"))
        self.tableWidget.setItem(1, 4, QTableWidgetItem("RM 150"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("7"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("162"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("Yoko Yoko"))
        self.tableWidget.setItem(2, 3, QTableWidgetItem("RM 12"))
        self.tableWidget.setItem(2, 4, QTableWidgetItem("RM 84"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("25"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("144"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("Fungus Removal 9000"))
        self.tableWidget.setItem(3, 3, QTableWidgetItem("RM 12.5"))
        self.tableWidget.setItem(3, 4, QTableWidgetItem("RM 312.5"))

        col_header = ['Qty','Stock No.','Description', 'Unit Price','Total']
        self.tableWidget.setHorizontalHeaderLabels(col_header)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.tableWidget.verticalHeader().setVisible(False)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    def createTableHeader(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(6)

        self.tableWidget.setItem(0, 1, QTableWidgetItem("NIL"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("NIL"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("NIL"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("On Process"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("CLK Logistics"))
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Checked"))

        col_header = ['Cash','Charge', 'C.O.D', 'PAID OUT', 'Ship VIA', 'TERMS']
        self.tableWidget.setHorizontalHeaderLabels(col_header)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setFixedHeight(50)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    def totalTable(self):

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("47"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("671.5"))

        self.tableWidget.setVerticalHeaderLabels(['Net Total RM '])
        self.tableWidget.setHorizontalHeaderLabels(['Unit Price','Total'])
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnWidth(1, 80)

        self.tableWidget.setFixedHeight(65)
        self.tableWidget.setFixedWidth(260)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class DBConnect():

    db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")
    cursor = db.cursor()

    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    sql = """SELECT * FROM product WHERE category = '%s'""" % ('Skin care')

    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            name = row[3]

            print('Name: %s' % (name))

        # db.commit()
    except:
        print('Error! unable to fetch data')
        # db.rollback()

    db.close()


def main():
    app = QApplication(sys.argv)
    ex = Shortcut()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()