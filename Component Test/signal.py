import sys
from PyQt5 import QtWidgets

class Dialog(QtWidgets.QDialog):

    def slot_method(self):
        print('this is slot method')

    def __init__(self):
        super(Dialog, self).__init__()

        button = QtWidgets.QPushButton('CLICK HERE!', self)
        button.clicked.connect(self.slot_method)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle('shit me')




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())