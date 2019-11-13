# coding: utf-8
#https://www.jianshu.com/p/8cd8f60df8bf
import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA

#message = b"this is test"
with open("安可算分.xlsx",'rb') as f:
    message = f.read()

random_generator = Random.new().read
rsa = RSA.generate(1024,random_generator)

rsa_private_key = rsa.exportKey()
rsa_public_key = rsa.publickey().exportKey()
print(rsa_private_key)
print(rsa_public_key)
with open('miyao.pem','wb') as p:
    p.write(rsa_private_key)


# rsakey = RSA.importKey(rsa_public_key)
# cipher = Cipher_pkcs1_v1_5.new(rsakey)
# cipher_text = cipher.encrypt(message)
# print(type(cipher_text))
# with open('jimihou.xlsx','rb') as w:
#     w.write(cipher_text)
#
# rsakey = RSA.importKey(rsa_private_key)
# cipher = Cipher_pkcs1_v1_5.new(rsakey)
# random_generator = Random.new().read
# text = cipher.decrypt(cipher_text,None)
# print(type(text))


def rsa_long_encrypt(pub_key_str, msg, length=100):
    """
    单次加密串的长度最大为 (key_size/8)-11
    1024bit的证书用100， 2048bit的证书用 200
    """
    pubobj = RSA.importKey(pub_key_str)
    pubobj = Cipher_pkcs1_v1_5.new(pubobj)
    res = []
    for i in range(0, len(msg), length):
        res.append(pubobj.encrypt(msg[i:i+length]))
    return b"".join(res)

def rsa_long_decrypt(priv_key_str, msg, length=128):
    """
    1024bit的证书用128，2048bit证书用256位
    """
    privobj = RSA.importKey(priv_key_str)
    privobj = Cipher_pkcs1_v1_5.new(privobj)
    res = []
    for i in range(0, len(msg), length):
        res.append(privobj.decrypt(msg[i:i+length], 'xyz'))
    return b"".join(res)

data = rsa_long_encrypt(rsa_public_key, message, length=100)
with open('jimi.xlsx','wb') as p:
    p.write(data)

with open('jimi.xlsx','rb') as w:
    data = w.read()

with open('miyao.pem','rb') as q:
    priv_key_str = q.read()

data = rsa_long_decrypt(priv_key_str, data, length=128)
with open('new.xlsx','wb') as r:
    r.write(data)