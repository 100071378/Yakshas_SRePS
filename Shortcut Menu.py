import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Shortcut(QMainWindow):
    def __init__(self, parent=None):
        super(Shortcut, self).__init__(parent)

        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("save")
        file.addAction("quit")

        edit = bar.addMenu('Edit')
        search = bar.addMenu('Search')
        tool = bar.addMenu('Tools')
        help= bar.addMenu('Help')

        exitButton = QAction(QIcon('exit.png'), 'Exitter', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exits this shit')
        exitButton.triggered.connect(self.close)
        file.addAction(exitButton)

        self.items = QDockWidget("List of Shortcuts", self)
        self.listWidget = QListWidget()
        self.listWidget.addItem("Ctrl+A (Add Sales Record)")
        self.listWidget.addItem("")
        self.listWidget.addItem("Ctrl+D (Add Delete Record)")
        self.listWidget.addItem("")
        self.listWidget.addItem("Ctrl+E (Add Edit Record)")

        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)
        self.setWindowTitle("Shortcut Window")


def main():
    app = QApplication(sys.argv)
    ex = Shortcut()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()