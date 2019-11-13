# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urlencode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout.addWidget(self.lineEdit_9)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.lineEdit.setText(_translate("MainWindow", "aa"))
        self.lineEdit.setPlaceholderText('请输入需要转换的字符！！！')

