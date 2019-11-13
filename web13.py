# coding=utf-8
import base64
import requests

r = requests.session()
r1 = r.get('http://123.206.31.85:10013/index.php')
password = r1.headers['Password']
tmp = base64.b64decode(password)
print(tmp)
data = {'password': tmp[5:-1].decode('utf8')}
print(tmp[5:-1].decode('utf8'))
r2 = r.post('http://123.206.31.85:10013/index.php',data=data)

print(r2.content)
