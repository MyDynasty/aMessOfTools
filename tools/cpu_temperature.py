#coding=utf-8

import requests,time,threading
from multiprocessing.dummy import Pool as ThreadPool

share_id = []
start_time = time.time()
for i in range(1,1000000):
    n = "%06d" % i
    share_id.append(n)
share_id_T = []

def get_share_id(id):
    if not 'Please check symbol' in requests.get('http://www.aigaogao.com/tools/history.html?s='+id).text:
        share_id_T.append(id)
        print(id)
if __name__ == '__main__':
    pool = ThreadPool(20)
    pool.map(get_share_id, share_id)
    pool.close()
    print(time.time()-start_time)
    with open('share_id','w') as f:
        f.write(share_id_T)