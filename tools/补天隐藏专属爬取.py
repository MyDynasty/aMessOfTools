# -*- coding: UTF-8 -*-

import requests
import time,re
from lxml import etree

#公益src页数
startpage = 34
endpage   = 179              #176
r = requests.post("https://www.butian.net/Reward/pub",data={'s':'1','p':'1','token':''})
r.json()


data = list()



def pubWelfareSrcCrawlName():
    """
    爬取所有公益src名称与ID

    """
    global data
    for page in range(startpage, endpage + 1):
        time.sleep(0.1)
        try:
            r = requests.post("https://www.butian.net/Reward/pub", data={'s': '1', 'p': page, 'token': ''}).json()
            data = data + r['data']['list']
            print('SUCCESS : ' + str(page))
            for i in r['data']['list']:
                with open('data2.txt', 'a', encoding='gb18030', errors='ignore') as f:
                    try:
                        srcurl = requests.get("https://www.butian.net/Company/" + i['company_id'], cookies={
    "__DC_gid":"66782632.715623539.1557221184807.1563682283283.526",
    "__guid":"66782632.463272934168084350.1557221184776.4592",
    "btlc_ba52447ea424004a7da412b344e5e41a":"bd02e9305511a86e3ae417f36e945ba9597254c78123b46abb8fe179ba9dd3c4",
    "PHPSESSID":"co8scldrr4trse2ggslhlii6b1",
    "__q__":"1576805232532"
}
).text
                        # curl = re.findall('<dt>公司简介</dt>(.*)</dl>', srcurl)
                        tree = etree.HTML(srcurl)
                        tmp = str(tree.xpath('/html/body/div[2]/div/div[3]/dl[1]/text()')).replace('\\t', '').replace(
                            '\\r', '').replace('\\n', '').replace("['', '", '').replace("']", '')
                        f.write(i['company_id'] + '\t' + i['company_name'] + '\t' + str(tmp) + '\n')
                        print('SUCCESS ID : ' + i['company_id'])
                    except Exception as e:
                        print(e.args)
                        print("ERROR ID : " + i['company_id'])
                        print('ERROR : ' + str(page))
                        return 0
        except:
            print('ERROR : ' + str(page))
            return 0



if __name__ == '__main__':
    pubWelfareSrcCrawlName()
    #organizeData()
    #print(data)