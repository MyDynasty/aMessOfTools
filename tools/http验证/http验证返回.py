import requests

listok = []
listerror = []

def verifi(ip,port):
    if port!='443':
        r = requests.get('http://' + ip+':'+port)
    else:
        r = requests.get('https://' + ip + ':' + port)

    return r.ok

if __name__ == '__main__':
    with open('iplist.txt','r') as f:
        for i in f:
            a = i.replace('\r','').replace('\n','')
            b = a.split()
            try:
                if verifi(b[0],b[1]):
                    listok.append(b[0]+':'+b[1])
            except:
                listerror.append(b[0]+':'+b[1])

    print('ok: \n')
    for i in listok:
        print(i)
    print('\nerror: \n')
    for i in listerror:
        print(i)