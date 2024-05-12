from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType

ui, _ = loadUiType('schoolmanagement.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menubar.setVisible(False)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    window.setFixedHeight(639)
    window.setFixedWidth(800)
    app.exec_()


if __name__ == '__main__':
    main()
