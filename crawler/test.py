

import writetocsv
import csv
import socket
import time
from lxml import etree

start = time.time()
with open('html.txt','r') as f:
    response = f.read()
#print(response)
print("spend time is %s" %(time.time()-start))

data = []
tmp = []
tree = etree.HTML(response)
for i in range(1,31):
    for j in range(2,10):
        path = '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']/text()'
        ranks = tree.xpath(path)
        tmp.append(ranks[0].replace('\n','').replace('\t',''))
    tmp = tuple(tmp)
    data.append(tmp)
    tmp = []

print(data)

start = time.time()
with open('test.csv','a',newline='') as e:
    write =csv.writer(e)
    for i in data:
        write.writerow(i)
print("spend time is %s" %(time.time() - start))