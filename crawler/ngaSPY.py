# coding=utf-8

import requests
from lxml import etree
import os,re


url = 'https://bbs.nga.cn/read.php?tid=16321887'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Connection':'keep-alive',
    'Cookie': 'taihe=61bdf74ddd32a6ce9a15a7d1a9f64223; ngaPassportUid=10436274; ngaPassportUrlencodedUname=IceQboo; ngaPassportCid=cef3d0392f498171a7e71000ecd628c8336a9f88; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A0%2C1%3A1555642208%7D%7D; ngacn0comUserInfo=IceQboo%09IceQboo%0939%0939%09%0910%0913011%094%090%090%0971_30%2C19_75%2C61_1; ngacn0comUserInfoCheck=2fbaff612991ffacf3afa2efea0dd86f; ngacn0comInfoCheckTime=1549531132; Hm_lvt_5adc78329e14807f050ce131992ae69b=1549254074,1549520560,1549531135,1549849846; lastvisit=1549850126; lastpath=/read.php?tid=16282569&_ff=-7; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1549850130'
}

# 获取图片相对地址的正则
img_link_pattern = r',url:\'(.*?)\',name:'
# 获取第三方图片地址的正则
img_link_with_third_site_pattern = r'\[img\](.*?)\[/img\]'
# 获取图片地址和名称的正则
img_link_and_name_pattern = r',url:\'(.*?)\',name:\'(.*?)\''
# 获取帖子名称的正则，用作文件夹名字
post_title_pattern = r'<title>(.*?)</title>'
# 获取帖子总页数正则
post_page_num_pattern = r',1:([0-9]*?),'
# 图片域名地址
img_link_prefix = 'http://img.nga.cn/attachments/'



data = requests.get(url,headers=headers).content.decode('gbk')

#获取总页数
pagenum = int(re.findall(re.compile(post_page_num_pattern),data)[0])
#获取图片url
imglist = re.findall(re.compile(img_link_with_third_site_pattern),data)
#获取帖子名称
title = re.findall(re.compile(post_title_pattern),data)[0]

print(os.getcwd())
if not os.path.exists(title):
    os.mkdir(title)
    print("正在创建目录")
else:
    print("目录已存在!")

for i in range(len(imglist)):
    imglist[i] = imglist[i].replace('./', img_link_prefix)
    print(imglist[i])

for num in range(2,pagenum + 1):
    tmpurl = url + '&page=' + str(num)
    print(tmpurl)
    data = requests.get(tmpurl, headers=headers).content.decode('gb18030')
    tmpimglist = re.findall(re.compile(img_link_with_third_site_pattern), data)
    for i in range(len(tmpimglist)):
        tmpimglist[i] = tmpimglist[i].replace('./', img_link_prefix)
        # print(tmpimglist[i])
        imglist.append(tmpimglist[i])

for photourl in imglist:
    photoname = photourl[44:]
    try:
        with open(os.getcwd() + '\\' + title + '\\' + photoname, 'wb') as f:
            f.write(requests.get(photourl, headers=headers).content)
    except:
        print('无法下载图片：' + photourl)



    with open('list','a') as p:
        p.write(photourl + '\r\n')

# for ii in imglist:
#     with open('listurl', 'a') as ww:
#         ww.write(ii + '\r')

#print(type(pagenum))  44

# print(len(imglist))



