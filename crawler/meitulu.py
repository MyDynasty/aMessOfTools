# coding=utf-8

import requests
from lxml import etree
import time,os,sys,re
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')




def get_img(url):
    '''
    下载页面下所有图片
    '''
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
    #print(len(tree))
    #print(page_num)

    if not os.path.exists(img_title):
        os.mkdir(img_title)
        print("已创建目录")
    else:
        print("目录已存在!")

    for i in range(1, page_num * 4 + 1):
        tmpurl = img_url.replace('1.jpg', str(i) + '.jpg')
        try:
            img_data = requests.get(tmpurl, headers=headers).content
        except :
            print("error url: " + tmpurl)
        with open(os.getcwd() + '\\' + img_title.strip() + '\\' + str(i) + '.jpg', 'wb') as f:
            f.write(img_data)
        print(str(i)+'.jpg'+'已保存\r')

    print('FINISHED!')

def paku(url):
    '''
    根据类型或人爬取页面
    '''
    url_text = requests.get(url).content.decode()
    tree = etree.HTML(url_text)
    tmp = tree.xpath('.//div[@class="boxs"]/ul/li')
    urls = []
    for i in tmp:
        urls.append(i[0].attrib['href'])
    print(urls)
    return urls

def creat_index():
    '''
    创建网页目录
    '''
    from natsort import natsorted
    a = os.getcwd()
    b = os.listdir()
    for i in b:
        list_jpg = os.listdir(a + '\\' + i)
        with open(a + '\\' + i + '\\index.html', 'w') as f:
            list_jpg = natsorted(list_jpg)
            for file_name in list_jpg:
                f.write("<img src=\"" + file_name + "\" style=\"width: 100%;\">\r\n")

if __name__ == '__main__':

    # while True:
    #     print('''请输入网址，如：https://www.meitulu.com/item/16777.html\r''')
    #     url = input("网址：").replace(' ','')
    #     try:
    #         get_img(url)
    #         # break
    #     except:
    #         print('''网址：''')

    #get_img('https://www.meitulu.com/item/16581.html')

    tmp = paku('https://www.meitulu.com/t/sugar-xiaotianxincc/3.html')
    for i in tmp:
        get_img(i)