# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anke.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_Dialog(object):
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(765, 571)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 40, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 90, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "one"))
        self.pushButton_2.setText(_translate("Dialog", "two"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = Ui_Dialog()
    myshow.show()
    sys.exit(app.exec_())