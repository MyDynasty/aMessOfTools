# -*- coding: utf-8 -*-

import re

text = ''
page = 0
with open("C:\\Users\\iceqb\\Desktop\\303.txt", 'r', encoding='utf-8') as f:
    for tmp in f:
        page = page + 1
        print(page)
        if ('章' in tmp) and ('0' in tmp):
            text += '\n' + tmp + '  '
        else:
            text += tmp.replace(' ', '').replace('\n', '').replace('“', '').replace('”', '').replace('-', '')


with open("C:\\Users\\iceqb\\Desktop\\404.txt", 'wb') as p:
    p.write(text.encode('utf8'))