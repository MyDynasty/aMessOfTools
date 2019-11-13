# coding=utf-8

import requests,socket
from lxml import etree

def get_share_price_xpath(id):
    url = 'http://www.aigaogao.com/tools/history.html?s=' + id
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
               'Connection': 'close',
               'Pragma': 'no-cache',
               'Cache-Control': 'no-cache',
               'Upgrade-Insecure-Requests': '1'

    }
    print(type(id))
    r = requests.get(url,headers = headers).text.replace(u'\xa9', u'')
    print(type(r))
    tree = etree.HTML(r)
    return tree

def output_vsc(tree):
    tmp = tree.xpath('//*[@id="ctl16_contentdiv"]/table/tr')
    data = str()
    for i in tmp[0]:
        data += i.text + ','

    for i in tmp[1:-1]:
        data += '\n' +i[0][0].text + ','
        data += i[1].text + ','
        data += i[2].text + ','
        data += i[3].text + ','
        data += i[4].text + ','
        data += i[5].text.replace(',', '') + ','
        data += i[6].text.replace(',', '') + ','
        data += i[7].text + ','
        data += i[8][0].text + ','
        try:
            data += i[9].text + ','
        except:
            data += ','
        data += i[10][0].text + ','
        data += i[11].text + ','
        data += i[12][0].text + ','

    with open('avc.csv','w') as f:
        f.write(data)


def build_share_id():
    share_id = []
    for i in range(1,1000000):
        n = "%06d" % i
        share_id.append(n)



if __name__ == '__main__':
    get_stock_price('002175')



