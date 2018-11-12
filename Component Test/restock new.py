import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# class ReStock(QDialog):
#
#     def __init__(self):
#         super(ReStock, self).__init__()
#         self.createFormGroupBox()
class Dialog(QDialog):


    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.CompanygroupBox)

        self.createTableHeader()
        mainLayout.addWidget(self.tableWidget)

        self.createTable()
        mainLayout.addWidget(self.tableWidget)

        # self.totalTable()
        # mainLayout.addWidget(self.tableWidget)

        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Re-Stock Recommendation")

    def createFormGroupBox(self):
        self.CompanygroupBox = QGroupBox("Company Details")
        lay = QFormLayout()
        self.CompanygroupBox.setGeometry(QRect(20, 30, 421, 121))
        self.CompanygroupBox.setObjectName("CompanygroupBox")

        self.companylabel = QLabel(self.CompanygroupBox)
        self.companylabel.setGeometry(QRect(20, 30, 71, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.companylabel.setFont(font)
        self.companylabel.setObjectName("companylabel")
        self.companylabel.setText("Company :")
        self.CompanyfontComboBox = QComboBox(self.CompanygroupBox)
        self.CompanyfontComboBox.setGeometry(QRect(100, 30, 231, 22))
        self.CompanyfontComboBox.setObjectName("CompanyfontComboBox")
        lay.addRow(self.companylabel, self.CompanyfontComboBox)

        self.companylabel_2 = QLabel(self.CompanygroupBox)
        self.companylabel_2.setGeometry(QRect(20, 70, 71, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        lay.addRow(self.companylabel)
        self.companylabel_2.setFont(font)
        self.companylabel_2.setObjectName("companylabel_2")
        self.companylabel_2.setText("Category : ")
        self.comboBox = QComboBox(self.CompanygroupBox)
        self.comboBox.setGeometry(QRect(100, 70, 151, 22))
        self.comboBox.setObjectName("comboBox")
        lay.addRow(self.companylabel_2, self.comboBox)

        self.companylabel_3 = QLabel(self)
        self.companylabel_3.setGeometry(QRect(460, 40, 71, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.companylabel_3.setFont(font)
        self.companylabel_3.setObjectName("companylabel_3")
        self.companylabel_3.setText("Order ID :")
        self.spinBox = QSpinBox(self)
        self.spinBox.setGeometry(QRect(540, 40, 42, 22))
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        lay.addRow(self.companylabel_3, self.spinBox)

        self.companylabel_4 = QLabel(self)
        self.companylabel_4.setGeometry(QRect(460, 90, 71, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.companylabel_4.setFont(font)
        self.companylabel_4.setObjectName("companylabel_4")
        self.companylabel_4.setText("Date :")
        self.dateEdit = QDateEdit(self)
        self.dateEdit.setGeometry(QRect(510, 90, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2018, 12, 11))
        self.dateEdit.setObjectName("dateEdit")
        lay.addRow(self.companylabel_4, self.dateEdit)

        self.CompanygroupBox.setLayout(lay)


    def createTable(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(5)
        # self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,1)"))
        # self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        # self.tableWidget.setItem(1, 2, QTableWidgetItem("Cell (2,1)"))
        # self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        # self.tableWidget.setItem(2, 2, QTableWidgetItem("Cell (3,1)"))
        # self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        # self.tableWidget.setItem(3, 2, QTableWidgetItem("Cell (4,1)"))
        # self.tableWidget.setItem(4, 3, QTableWidgetItem("Cell (4,2)"))

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

        col_header = ['Cash','Charge', 'C.O.D', 'PAID OUT', 'Ship VIA', 'TERMS']
        self.tableWidget.setHorizontalHeaderLabels(col_header)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setFixedHeight(50)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())






if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())