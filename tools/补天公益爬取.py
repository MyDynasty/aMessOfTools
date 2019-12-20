# -*- coding: UTF-8 -*-

import requests
import time,re

#公益src页数
pageNum = 179              #176
r = requests.post("https://www.butian.net/Reward/pub",data={'s':'1','p':'1','token':''})
r.json()


data = list()



def pubWelfareSrcCrawlName():
    '''
    爬取所有公益src名称与ID

    '''
    global data
    for page in range(pageNum):
        try:
            r = requests.post("https://www.butian.net/Reward/pub", data={'s': '1', 'p': page + 1, 'token': ''}).json()
            data = data + r['data']['list']
            print('SUCCESS : ' + str(page + 1))
        except:
            print('ERROR : ' + str(page + 1))

def organizeData():
    '''
    提取公益src保存至文件
    '''
    global data
    for i in data:
        with open('data2.txt','a') as f:
            try:
                srcurl = requests.get("https://www.butian.net/Loo/submit?cid=" + i['company_id'], cookies={
                    'btlc_ba52447ea424004a7da412b344e5e41a': 'bd02e9305511a86e3ae417f36e945ba9597254c78123b46abb8fe179ba9dd3c4'}).text
                curl = re.findall('placeholder="请输入厂商域名" value=\"(.*)\"', srcurl)
                f.write(i['company_id'] + '\t' + i['company_name'] + '\t' + str(curl) + '\n')
                print('SUCCESS ID : ' + i['company_id'])
            except Exception as e:
                print(e.args)
                print("ERROR ID : " + i['company_id'])




if __name__ == '__main__':
    pubWelfareSrcCrawlName()
    organizeData()
    print(data)