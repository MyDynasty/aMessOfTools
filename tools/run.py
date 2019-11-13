import sys,time,base64,binascii
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5 import QtCore,QtGui
from urlencode import Ui_MainWindow

class mwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mwindow, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.msg)


    def msg(self,text):
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




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    w.show()
    sys.exit(app.exec_())
