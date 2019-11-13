# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import test

if __name__=='__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())