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
        mainLayout.addWidget(self.CompanygroupBox_2)

        # self.createTableHeader()
        # mainLayout.addWidget(self.tableWidget)
        #
        # self.createTable()
        # mainLayout.addWidget(self.tableWidget)

        # self.totalTable()
        # mainLayout.addWidget(self.tableWidget)

        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Re-Stock Recommendation")
        self.resize(655, 520)


    def createFormGroupBox(self):

        # self.centralwidget = QtWidgets.QWidget()
        # self.centralwidget.setObjectName("centralwidget")
        # self.restocktab = QtWidgets.QTabWidget(self.centralwidget)
        # self.restocktab.setGeometry(QtCore.QRect(10, 10, 627, 481))
        # self.restocktab.setObjectName("restocktab")
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
        # self.buttonBox = QtWidgets.QDialogButtonBox(self.CompanygroupBox_2)
        # self.buttonBox.setGeometry(QtCore.QRect(430, 410, 161, 23))
        # self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        # self.buttonBox.setObjectName("buttonBox")
        # self.verticalLayout.addWidget(self.CompanygroupBox_2)
        # self.restocktab.addTab(self.verticalTabWidgetPage1, "")





    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())






if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())