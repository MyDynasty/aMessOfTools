# coding: utf-8
import csv
import socket
import time
from lxml import etree



response = b''
sock = socket.socket()
sock.connect(("45.76.86.64", 80))
sock.send("PUT /input.txt\r\n".encode("utf-8"))
sock.send("Host: 45.76.86.64\r\n".encode("utf-8"))
sock.send("Content-Length: 6\r\n\r\n123456".encode("utf-8"))
buf = sock.recv(4096)
while buf:
    response += buf
    buf = sock.recv(4096)
print(response)
response += buf
print(response)
