# coding:utf-8
# 卿 博客:https://www.cnblogs.com/-qing-/
from bs4 import BeautifulSoup
import requests,re
session = "_fofapro_ars_session=dd3506a3d9820952c612303aac0ce2dc"
header = {
    "Accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "X-CSRF-Token":"DpraMUR6PuefxdVpDmbZmgW9572Oz4CKSkqLa4u+astRxa+NSW5t0gfjlRB8cESuUrBvrD+zkGA9GFcfEYAVZA==",
    "X-Requested-With":"XMLHttpRequest",
    "Cookie":session,
}
def file_put(str):
    with open("ip.txt","a") as f:
        f.write(str)

def spider_ip(url):
    html_doc = requests.get(url = url,headers = header).content
    soup = BeautifulSoup(html_doc)
    for link in soup.find_all('a'):
        if "http" in link.get('href') :
            if "http" in link.get('href') :
                ip = link.get('href')
                result = re.findall(r"\d+\.\d+\.\d+.\d+",ip,re.I)[0]
                print(result)
                file_put(ip+"\n")

for i in range(1,5):
    spider_ip("https://fofa.so/result?full=true&page="+ str(i) +"&qbase64=")c2VleW9u