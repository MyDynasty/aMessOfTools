from multiprocessing.dummy import Pool as ThreadPool

import requests
import time

listok = []
listerror = []
timeout = 1     #设置超时时间
thread = 100    #设置线程数!!!!!!!!!!!!!!!!!!!!!!!

def verifi(ip,port):
    if port!='443':
        r = requests.get('http://' + ip+':'+port , timeout=timeout)
    else:
        r = requests.get('https://' + ip + ':' + port ,timeout=timeout)

    return r.ok


def main(i):
    global tmp
    a = i.replace('\r', '').replace('\n', '')
    b = a.split()
    print("第" + str(tmp) + "个")
    tmp += 1
    try:
        if verifi(b[0], b[1]):
            listok.append(b[0] + ':' + b[1])
    except:
        listerror.append(b[0] + ':' + b[1])




if __name__ == '__main__':
    start = time.time()
    tmp = 1
    ip_port = []
    with open('iplist.txt','r') as f:
        for i in f:
            ip_port.append(i)

    pool = ThreadPool(thread)
    pool.map(main, ip_port)
    pool.close()

    print('ok: \n')
    for i in listok:
        print(i)
    print('\nerror: \n')
    for i in listerror:
        print(i)

    print("spend time is %s" % (time.time() - start))