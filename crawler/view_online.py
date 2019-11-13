# coding=utf-8

import requests
from lxml import etree
import time,os,sys,re
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib import parse



def get_img(url):
    # url = 'https://www.meitulu.com/item/2005.html'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.meitulu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    img_xpath_title = '/html/body/div[2]/div[1]/h1'
    img_xpath_url = '/html/body/div[4]/center/img'
    img_xpath_page = '//*[@id="pages"]/a'

    r = requests.get(url, headers=headers).content.decode('utf8')

    tree = etree.HTML(r)

    img_title = tree.xpath(img_xpath_title)[0].text.replace('/','').replace('\\','').replace(':','').replace('"','').replace('<','').replace('>','').replace('|','').replace('*','')
    img_url = tree.xpath(img_xpath_url)[0].attrib['src']
    page_num = int(tree.xpath(img_xpath_page)[-2].text)
    print(len(tree))
    print(page_num)

    if not os.path.exists(img_title):
        os.mkdir(img_title)
        print("已创建目录")
    else:
        print("目录已存在!")

    urllist = []
    for i in range(1, page_num * 4 + 1):
        tmpurl = img_url.replace('1.jpg', str(i) + '.jpg')
        urllist.append(tmpurl)

    print(urllist)
    print('FINISHED!')
    return urllist


data = {'result':'this is test'}

host = ('localhost',12345)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        urls = get_img(parsed_path.query)
        message = ''
        for i in urls:
            message += "<img src=\"" + i + "\">"
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(length))
        print(post_data)



if __name__ == '__main__':

    # while True:
    #     print('''请输入网址，如：https://www.meitulu.com/item/16777.html\r''')
    #     url = input("网址：").replace(' ','')
    #     try:
    #         get_img(url)
    #         # break
    #     except:
    #         print('''网址：''')


    server = HTTPServer(host, Resquest)
    print("Starting Server....")
    server.serve_forever()