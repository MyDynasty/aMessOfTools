
import Crypto.Cipher.DES
import Crypto.Util.Padding
import base64

BLOCK_SIZE = 8
key = "cicioweb"
iv = "EjRWeAECAwQ="
content = "123456"
cipher = Crypto.Cipher.DES.new(key.encode("utf-8"), Crypto.Cipher.DES.MODE_CBC, base64.b64decode(iv))

def encrypt(data):
    global cipher
    miwen = b"=#=" + base64.encodebytes(cipher.encrypt(Crypto.Util.Padding.pad(data.encode("utf-8"), BLOCK_SIZE)))
    return miwen

def decrypt(data):
    global cipher
    return Crypto.Util.Padding.unpad(cipher.decrypt(base64.decodebytes(data.replace("=#=", "").encode("utf-8"))), BLOCK_SIZE)

if __name__ == '__main__':
    while True:
        aa = input("输入密码：")
        print(decrypt(aa))