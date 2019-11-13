import requests
from lxml import etree

def paku(url):
    url_text = requests.get(url).content.decode()
    tree = etree.HTML(url_text)
    tmp = tree.xpath('.//div[@class="boxs"]/ul/li')
    urls = []
    for i in tmp:
        urls.append(i[0].attrib['href'])
    print(urls)
    return urls

paku("https://www.meitulu.com/t/1385/")