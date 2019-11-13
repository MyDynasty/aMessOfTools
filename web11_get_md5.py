# coding=utf-8

import socket
import hashlib

def get_md5():
    response = bytes()
    sock = socket.socket()
    sock.connect(('123.206.31.85', 3030))
    sock.send("GET /shell.php HTTP/1.1\r\nHost: 123.206.31.85:3030\r\nCookie: PHPSESSID=ikqrjigfvsmdtt19ee3fm99370b714g3\r\n\r\n".encode('utf-8'))
    response = sock.recv(461)
    return response

if __name__ == "__main__":
    md55 = ''
    for i in range(1):
        md55 = get_md5()[414:420].decode('utf8') + '\n'
        print(i)
        with open('web11_get_md5', 'a') as f:
            f.write(md55)

sum = []
j = 0
f = open("gen_md5.txt","a")
for i in xrange(1000000000):
    tmp = (hashlib.md5(str(i)).hexdigest(),i)
    sum.append(tmp)
    j = j+1
    if(j==10000000):
        for i in sum:
            f.write("{0} {1}".format(i,"\n"))
        j=0
        sum =[]
f.close()