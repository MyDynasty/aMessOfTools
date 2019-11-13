# coding=utf-8

import base64
import hashlib

str = "fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA="

str1 = base64.b64decode(str)
print(str1)

str2 = []
for i in range(len(str1)):
    str2.append(ord(chr(str1[i])))
print(str2)