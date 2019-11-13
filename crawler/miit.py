# coding: utf-8

import csv
import socket
import time
from lxml import etree

response = b''

sock = socket.socket()
sock.connect(("data.miit.gov.cn",80))
sock.send("GET /resultSearch?categoryTreeId=1064&pagenow=1 HTTP/1.1\r\n".encode("utf-8"))
sock.send("Host: data.miit.gov.cn\r\n".encode("utf-8"))
sock.send("Connection: keep-alive\r\n".encode("utf-8"))
sock.send("Upgrade-Insecure-Requests: 1\r\n".encode("utf-8"))
sock.send("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36\r\n".encode("utf-8"))
sock.send("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n".encode("utf-8"))
sock.send("Referer: http://data.miit.gov.cn/resultSearch?categoryTreeId=1064&pagenow=2\r\n".encode("utf-8"))
sock.send("Accept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n".encode("utf-8"))
sock.send("Cookie: Hm_lvt_af6f1f256bb28e610b1fc64e6b1a7613=1547437844,1547443779; Hm_lpvt_af6f1f256bb28e610b1fc64e6b1a7613=1547443810; JSESSIONID=83C8F249324F3D8D61803C14E21ECD25\r\n\r\n".encode("utf-8"))
starttime = time.time()
buf = sock.recv(4096)
while buf:
    response += buf
    buf = sock.recv(4096)
print("spend time is %s" %(time.time()-starttime))
print(response.decode("utf-8"))
# with open('html.txt','w') as f:
#     f.write(response.decode("utf-8"))
print("spend time is %s" %(time.time()-starttime))
response = response.decode("utf-8")

data = []
tmp = []
tree = etree.HTML(response)
for i in range(1,31):
    for j in range(2,10):
        path = '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']/text()'
        ranks = tree.xpath(path)
        tmp.append(ranks[0].replace('\n', '').replace('\t', ''))
    tmp = tuple(tmp)
    data.append(tmp)
    tmp = []












