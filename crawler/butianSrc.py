# coding: utf-8

# coding=utf-8

import requests
from lxml import etree
import time,os,sys,re
import json


global uid
uid = []

def get_img():
    url = 'https://www.butian.net/Reward/pub'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'https://www.butian.net/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'X - Requested - With': 'XMLHttpRequest',
        'Cookie' : '__guid=66782632.463272934168084350.1557221184776.4592; PHPSESSID=guiv44gl91cjtcsvoj9onsrmj1; __DC_sid=66782632.3247184304364543500.1558355214085.679; btlc_ab7a660c7e054d9e446e06f4571ebe41=881deeca35af8841386442b681cddc26c94077eb01056f70b9d13ad832f316ba; __DC_monitor_count=25; __DC_gid=66782632.715623539.1557221184807.1558357496184.98; __q__=1558357648540'
    }

    global uid
    for j in range(1,175):
        # data = {'s': '1', 'p': '1', 'token': ''}
        r = requests.post(url, headers=headers, data={'s': '1', 'p': j, 'token': ''}).text
        #print(r)

        tmp = json.loads(r)
        for i in tmp['data']['list']:
            rr = requests.get(url = 'https://www.butian.net/Loo/submit?cid=' + i['company_id'], headers=headers).text
            tree = etree.HTML(rr)
            aim_url = tree.xpath('//*[@id="tabs"]/form/div[1]/ul/li[3]/input')[0].attrib['value']
            with open('butian_url', 'a') as f:
                f.write(aim_url + '\r')



if __name__ == '__main__':

    get_img()