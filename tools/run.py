import sys,time,base64,binascii,re
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
#from urlencode import Ui_MainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1359, 881)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 651, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 621, 411))
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
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 271, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 170, 271, 131))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "请输入需要转换的字符！！！"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))


class mwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mwindow, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.msg)
        # self.textEdit.textChanged.connect(self.msg1)
        self.textEdit.textChanged.connect(self.msg1)


    def msg(self):
        data = self.lineEdit.text()


        tmp = base64.b64encode(data.encode('utf-8'))
        self.lineEdit_2.setText(tmp.decode('utf8'))
        self.lineEdit_6.setText(data.encode('utf-8').decode('unicode_escape'))

        try:
            tmp = base64.b64decode(data)
            self.lineEdit_3.setText(tmp.decode('utf8'))
        except:
            self.lineEdit_3.setText('')

        if data[:2] == '0x':
            try:
                tmp = binascii.a2b_hex(data[2:].encode('utf8')).decode('utf8')
                self.lineEdit_4.setText(tmp)
            except:
                pass

            self.lineEdit_5.setText('')
        elif data != '':
            tmp = '0x' + binascii.b2a_hex(data.encode('utf8')).decode('utf8')
            self.lineEdit_5.setText(tmp)
            self.lineEdit_4.setText('')
        else:
            self.lineEdit_4.setText('')
            self.lineEdit_5.setText('')

        QApplication.processEvents()

    def msg1(self):
        data = self.textEdit.toPlainText()

        try:
            ip_list = re.findall(
                r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", data)
            new_numbers = []
            for x in ip_list:
                if x not in new_numbers:
                    new_numbers.append(x)
            new_numbers.sort()
            j = ''
            for i in new_numbers:
                j = j + i + '\n'
            self.textEdit_2.setText(j)
        except :
            pass

        QApplication.processEvents()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    w.show()
    sys.exit(app.exec_())
