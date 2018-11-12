import sys
import pymysql
import random
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

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.CompanygroupBox_2)

        # self.createTableHeader()
        # mainLayout.addWidget(self.tableWidget)
        #
        # self.createTable()
        # mainLayout.addWidget(self.tableWidget)
        #
        # self.totalTable()
        # mainLayout.addWidget(self.tableWidget)


        # mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Re-Stock Recommendation")

    def createFormGroupBox(self):

        self.verticalTabWidgetPage1 = QWidget()
        self.verticalTabWidgetPage1.setObjectName("verticalTabWidgetPage1")
        self.verticalLayout = QVBoxLayout(self.verticalTabWidgetPage1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CompanygroupBox_2 = QGroupBox(self.verticalTabWidgetPage1)
        self.CompanygroupBox_2.setMinimumSize(QSize(619, 0))
        self.CompanygroupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.CompanygroupBox_2.setObjectName("CompanygroupBox_2")
        self.CompanygroupBox_2.setTitle("Company Details")
        self.companylabel_5 = QLabel(self.CompanygroupBox_2)
        self.companylabel_5.setGeometry(QRect(20, 30, 72, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.companylabel_5.setFont(font)
        self.companylabel_5.setObjectName("companylabel_5")
        self.companylabel_5.setText("Company : ")
        self.companylabel_6 = QLabel(self.CompanygroupBox_2)
        self.companylabel_6.setGeometry(QRect(20, 70, 73, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.companylabel_6.setFont(font)
        self.companylabel_6.setObjectName("companylabel_6")
        self.companylabel_6.setText("Category : ")
        self.comboBox_2 = QComboBox(self.CompanygroupBox_2)
        self.comboBox_2.setGeometry(QRect(100, 70, 116, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Skin Care")
        self.comboBox_2.addItem("Eye Drop")
        self.comboBox_2.addItem("Hygiene Products")
        self.comboBox_2.addItem("Healthcare")
        self.comboBox_2.addItem("Medicine")
        self.comboBox_2.addItem("Intimacy")
        self.comboBox_2.addItem("Medical Equipment")
        self.comboBox_2.addItem("Others")
        self.comboBox_3 = QComboBox(self.CompanygroupBox_2)
        self.comboBox_3.setGeometry(QRect(100, 30, 166, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("Malaysian Pharmaceutical Inc")
        self.comboBox_3.addItem("UNipharma FZC Malaysia Bhd")
        self.comboBox_3.addItem("Eiro Chemo - Pharma")
        self.comboBox_3.addItem("Borneo Pharmacy Supplies")
        self.comboBox_3.addItem("All Health Medical Supplies")
        self.comboBox_3.addItem("Apex Pharmacy Marketing")
        self.dateEdit = QDateEdit(self.CompanygroupBox_2)
        self.dateEdit.setGeometry(QRect(460, 70, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2018, 12, 11))
        self.dateEdit.setObjectName("dateEdit")
        self.spinBox = QSpinBox(self.CompanygroupBox_2)
        self.spinBox.setGeometry(QRect(460, 30, 42, 22))
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.companylabel_3 = QLabel(self.CompanygroupBox_2)
        self.companylabel_3.setText("Order ID :")
        self.companylabel_3.setGeometry(QRect(380, 30, 71, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.companylabel_3.setFont(font)
        self.companylabel_3.setObjectName("companylabel_3")
        self.companylabel_4 = QLabel(self.CompanygroupBox_2)
        self.companylabel_4.setGeometry(QRect(400, 70, 71, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.companylabel_4.setFont(font)
        self.companylabel_4.setObjectName("companylabel_4")
        self.companylabel_4.setText("Date :")

        self.tableWidget = QTableWidget(self.CompanygroupBox_2)
        self.tableWidget.setGeometry(QRect(0, 120, 471, 55))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Cash")
        item = QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("C.O.D")
        item = QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Paid Out")
        item = QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Shipped VIA")
        item = QTableWidgetItem()

        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.orderrecomview = QTableWidget(self.CompanygroupBox_2)
        self.orderrecomview.setGeometry(QRect(0, 180, 611, 211))
        self.orderrecomview.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.orderrecomview.setDragEnabled(True)
        self.orderrecomview.setRowCount(10)
        self.orderrecomview.setObjectName("orderrecomview")
        self.orderrecomview.setColumnCount(6)
        item = QTableWidgetItem()

        self.orderrecomview.setHorizontalHeaderItem(0, item)
        item = self.orderrecomview.horizontalHeaderItem(0)
        item.setText("Qty")
        item = QTableWidgetItem()

        self.orderrecomview.setHorizontalHeaderItem(1, item)
        item = self.orderrecomview.horizontalHeaderItem(1)
        item.setText("Stock No.")
        item = QTableWidgetItem()

        self.orderrecomview.setHorizontalHeaderItem(2, item)
        item = self.orderrecomview.horizontalHeaderItem(2)
        item.setText("Name")
        item = QTableWidgetItem()

        self.orderrecomview.setHorizontalHeaderItem(3, item)
        item = self.orderrecomview.horizontalHeaderItem(3)
        item.setText("Brand")
        item = QTableWidgetItem()

        self.orderrecomview.setHorizontalHeaderItem(4, item)
        item = self.orderrecomview.horizontalHeaderItem(4)
        item.setText("Unit Price")
        item = QTableWidgetItem()

        self.orderrecomview.setHorizontalHeaderItem(5, item)
        item = self.orderrecomview.horizontalHeaderItem(5)
        item.setText("Total Price")
        self.orderrecomview.verticalHeader().setVisible(False)

        self.buttonBox = QDialogButtonBox(self.CompanygroupBox_2)
        self.buttonBox.setGeometry(QRect(430, 410, 161, 23))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.LoadData)
        self.buttonBox.rejected.connect(self.reject)

    def LoadData(self):

        var = self.comboBox_2.currentText()
        print(var)

        if var == 'Hygiene Products':
            var = 'hygiene'
        elif var == 'Medical Equipment':
            var = 'medical equip'
        # elif var == 'Other':
        #     db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")
        #     cursor = db.cursor()
        #     sql = """SELECT instockNo, name, brand, Price FROM product WHERE category = '%s'"""%('skin care')
        #     cursor.execute(sql)
        #     data = cursor.fetchall()
        #
        #     self.orderrecomview.setRowCount(0)
        #
        #     for row_number, row_data in enumerate(data):
        #         self.orderrecomview.insertRow(row_number)
        #         for column_number, data in enumerate(row_data):
        #             self.orderrecomview.setItem(row_number, column_number + 1, QTableWidgetItem(str(data)))
        #
        #     db.close()

        db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")
        cursor = db.cursor()
        pcursor = db.cursor()
        # x stock no naem brand unit price x
        sql = """SELECT instockNo, name, brand, Price FROM product WHERE category = '%s' """ % (var)
        cursor.execute(sql)

        data = cursor.fetchall()

        self.orderrecomview.setRowCount(0)

        for row_number, row_data in enumerate(data):
            rnd = random.randint(1, 101)
            self.orderrecomview.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.orderrecomview.setItem(row_number, column_number+1, QTableWidgetItem(str(data)))
                self.orderrecomview.setItem(row_number, 0, QTableWidgetItem(str(rnd)))
                # Quantt = self.orderrecomview.itemAt(row_number, 4).text()
                # print(Quantt)
                # self.orderrecomview.setItem(row_number,5,QTableWidgetItem(TotalP))

        db.close()

    # @pyqtSlot()
    # def on_click(self):
    #     print(self.comboBox_2.currentText())


        # self.verticalLayout.addWidget(self.CompanygroupBox_2)
        # self.restocktab.addTab(self.verticalTabWidgetPage1, "")
    #     self.formGroupBox = QGroupBox("Sales Order")
    #     layout = QFormLayout()
    #     layout.addRow(QLabel("Company:"), QLineEdit())
    #     QLineEdit().setText("Family Aid Pharmacy Inc.")
    #     layout.addRow(QLabel("Category:"), QComboBox())
    #     layout.addRow(QLabel("Order ID:"), QSpinBox())
    #     self.formGroupBox.setLayout(layout)
    #
    #
    #
    # def createTable(self):
    #
    #     self.tableWidget = QTableWidget()
    #     self.tableWidget.setRowCount(5)
    #     self.tableWidget.setColumnCount(5)
    #     self.item = self.tableWidget.setItem(0, 0, QTableWidgetItem("10"))
    #     self.tableWidget.setItem(0, 1, QTableWidgetItem("252"))
    #     self.tableWidget.setItem(0,2, QTableWidgetItem("Vitamin C"))
    #     self.tableWidget.setItem(0, 3, QTableWidgetItem("RM 12.50"))
    #     self.tableWidget.setItem(0, 4, QTableWidgetItem("RM 125"))
    #     self.tableWidget.setItem(1, 0, QTableWidgetItem("15"))
    #     self.tableWidget.setItem(1, 1, QTableWidgetItem("189"))
    #     self.tableWidget.setItem(1, 2, QTableWidgetItem("Panadol Soluble"))
    #     self.tableWidget.setItem(1, 3, QTableWidgetItem("RM 10"))
    #     self.tableWidget.setItem(1, 4, QTableWidgetItem("RM 150"))
    #     self.tableWidget.setItem(2, 0, QTableWidgetItem("7"))
    #     self.tableWidget.setItem(2, 1, QTableWidgetItem("162"))
    #     self.tableWidget.setItem(2, 2, QTableWidgetItem("Yoko Yoko"))
    #     self.tableWidget.setItem(2, 3, QTableWidgetItem("RM 12"))
    #     self.tableWidget.setItem(2, 4, QTableWidgetItem("RM 84"))
    #     self.tableWidget.setItem(3, 0, QTableWidgetItem("25"))
    #     self.tableWidget.setItem(3, 1, QTableWidgetItem("144"))
    #     self.tableWidget.setItem(3, 2, QTableWidgetItem("Fungus Removal 9000"))
    #     self.tableWidget.setItem(3, 3, QTableWidgetItem("RM 12.5"))
    #     self.tableWidget.setItem(3, 4, QTableWidgetItem("RM 312.5"))
    #
    #     col_header = ['Qty','Stock No.','Description', 'Unit Price','Total']
    #     self.tableWidget.setHorizontalHeaderLabels(col_header)
    #     self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
    #     self.tableWidget.setColumnWidth(1,100)
    #     self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
    #
    #     self.tableWidget.verticalHeader().setVisible(False)
    #
    #     # table selection change
    #     self.tableWidget.doubleClicked.connect(self.on_click)
    #
    # def createTableHeader(self):
    #
    #     self.tableWidget = QTableWidget()
    #     self.tableWidget.setRowCount(1)
    #     self.tableWidget.setColumnCount(6)
    #
    #     self.tableWidget.setItem(0, 1, QTableWidgetItem("NIL"))
    #     self.tableWidget.setItem(0, 2, QTableWidgetItem("NIL"))
    #     self.tableWidget.setItem(0, 3, QTableWidgetItem("NIL"))
    #     self.tableWidget.setItem(0, 4, QTableWidgetItem("On Process"))
    #     self.tableWidget.setItem(0, 5, QTableWidgetItem("CLK Logistics"))
    #     self.tableWidget.setItem(0, 0, QTableWidgetItem("Checked"))
    #
    #     col_header = ['Cash','Charge', 'C.O.D', 'PAID OUT', 'Ship VIA', 'TERMS']
    #     self.tableWidget.setHorizontalHeaderLabels(col_header)
    #     self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
    #     self.tableWidget.setColumnWidth(1, 100)
    #     self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
    #
    #     self.tableWidget.verticalHeader().setVisible(False)
    #     self.tableWidget.setFixedHeight(50)
    #
    #     # table selection change
    #     self.tableWidget.doubleClicked.connect(self.on_click)
    #
    # def totalTable(self):
    #
    #     layout = QVBoxLayout()
    #
    #     self.tableWidget = QTableWidget()
    #     self.tableWidget.setRowCount(1)
    #     self.tableWidget.setColumnCount(2)
    #
    #     self.tableWidget.setItem(0, 0, QTableWidgetItem("47"))
    #     self.tableWidget.setItem(0, 1, QTableWidgetItem("671.5"))
    #
    #     self.tableWidget.setVerticalHeaderLabels(['Net Total RM '])
    #     self.tableWidget.setHorizontalHeaderLabels(['Unit Price','Total'])
    #     self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
    #     self.tableWidget.setColumnWidth(1, 80)
    #
    #     self.tableWidget.setFixedHeight(65)
    #     self.tableWidget.setFixedWidth(260)
    #
    #     # table selection change
    #     self.tableWidget.doubleClicked.connect(self.on_click)
    #
    # @pyqtSlot()
    # def on_click(self):
    #     print("\n")
    #     for currentQTableWidgetItem in self.tableWidget.selectedItems():
    #         print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())



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