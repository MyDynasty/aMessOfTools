# coding: utf-8

import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from PyQt5.QtWidgets import QDialog,QApplication,QVBoxLayout,QPushButton,QFileDialog,QLabel
from PyQt5.QtGui import QPalette,QIcon,QFont
from PyQt5.QtCore import Qt

class MyWindow(QDialog):
    def __init__(self,parent=None):
        super(MyWindow, self).__init__(parent)
        layout=QVBoxLayout()

        font = QFont()
        font.setFamily('微软雅黑')

        self.label1 = QLabel(self)
        self.label1.setText("----------解密文件-----------")
        self.label1.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label1)
        layout.addStretch()

        self.myButton = QPushButton('选择私钥')
        self.myButton.clicked.connect(self.msg)
        layout.addWidget(self.myButton)

        self.myButton2 = QPushButton('选择文件')
        self.myButton2.clicked.connect(self.msg2)
        layout.addWidget(self.myButton2)

        self.myButton3 = QPushButton('点击解密')
        self.myButton3.clicked.connect(self.msg3)
        layout.addWidget(self.myButton3)

        self.label2 = QLabel(self)
        self.label2.setText('----------加密文件-----------')
        self.label2.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label2)
        layout.addStretch()

        self.myButton4 = QPushButton('选择文件并加密')
        self.myButton4.clicked.connect(self.msg4)
        layout.addWidget(self.myButton4)

        self.label3 = QLabel(self)
        self.label3.setText('power by iceqboo')
        self.label3.setAlignment(Qt.AlignRight)
        self.label3.setTextInteractionFlags(Qt.TextSelectableByMouse)
        layout.addWidget(self.label3)
        layout.addStretch()

        self.setWindowTitle('decrypt')
        # self.setFixedSize(200,300)
        self.setLayout(layout)
        self.setMinimumWidth(250)
        self.setWindowIcon(QIcon('easy.ico'))

    def msg(self):
        global rsa_private_key,data
        rsa_priv_file, filetype = QFileDialog.getOpenFileName(self,
                                                          "选择私钥",
                                                          "./",
                                                          "Text Files (*.pem)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(rsa_priv_file)
        try:
            with open(rsa_priv_file,'rb') as f:
                rsa_private_key = f.read()
        except:
            pass

    def msg2(self):
        global rsa_private_key,data
        try:
            xlsx_file, filetype = QFileDialog.getOpenFileName(self,
                                                              "选取文件",
                                                              "./",
                                                              "Text Files (*.xlsx)")  # 设置文件扩展名过滤,注意用双分号间隔
            print(xlsx_file)
            with open(xlsx_file, 'rb') as f:
                data = f.read()
        except:
            pass

    def msg3(self):
        global rsa_private_key,data
        try:
            tmp = self.rsa_long_decrypt(rsa_private_key, data, length=128)
            with open('new.xlsx', 'wb') as f:
                f.write(tmp)
            print("it's ok!")
        except:
            pass

    def msg4(self):
        try:
            xlsx_file, filetype = QFileDialog.getOpenFileName(self,
                                                              "选取文件",
                                                              "./",
                                                              "Text Files (*.xlsx)")  # 设置文件扩展名过滤,注意用双分号间隔
            print(xlsx_file)
            with open(xlsx_file, 'rb') as f:
                message = f.read()

            random_generator = Random.new().read
            rsa = RSA.generate(1024, random_generator)

            rsa_private_key = rsa.exportKey()
            rsa_public_key = rsa.publickey().exportKey()
            print(rsa_private_key)
            print(rsa_public_key)
            with open('miyao.pem', 'wb') as p:
                p.write(rsa_private_key)

            data = self.rsa_long_encrypt(rsa_public_key, message, length=100)
            with open('jimi.xlsx', 'wb') as p:
                p.write(data)
            print("it's ok!")
        except:
            pass


    def rsa_long_encrypt(self,pub_key_str, msg, length=100):
        """
        单次加密串的长度最大为 (key_size/8)-11
        1024bit的证书用100， 2048bit的证书用 200
        """
        pubobj = RSA.importKey(pub_key_str)
        pubobj = Cipher_pkcs1_v1_5.new(pubobj)
        res = []
        for i in range(0, len(msg), length):
            res.append(pubobj.encrypt(msg[i:i + length]))
        return b"".join(res)

    def rsa_long_decrypt(self,priv_key_str, msg, length=128):
        """
        1024bit的证书用128，2048bit证书用256位
        """
        privobj = RSA.importKey(priv_key_str)
        privobj = Cipher_pkcs1_v1_5.new(privobj)
        res = []
        for i in range(0, len(msg), length):
            res.append(privobj.decrypt(msg[i:i + length], 'xyz'))
        return b"".join(res)


if __name__ == "__main__":
    import sys

    rsa_private_key= bytes
    data = bytes
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())