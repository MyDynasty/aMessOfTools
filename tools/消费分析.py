import pandas as pd
import psycopg2
import re

def insert_wechat(csv_path):
    csv_data = pd.read_csv(csv_path)
    csv_data = csv_data.values.tolist()
    conn = psycopg2.connect(database="analysis", user="iceqboo", password="62350000", host="106.54.96.164", port="5432")
    cur = conn.cursor()

    #cur.execute('select * from pg_database')
    # print(cur.fetchall())

    for i in csv_data[16:]:
        sql = "INSERT INTO public.wechat VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
        i[0], i[1], i[2], i[3], i[4], i[5][1:], i[6], i[7], i[8], i[9], i[10])
        cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()

def insert_alipay(scv_path):
    csv_data = pd.read_csv(scv_path, encoding='gb18030')
    csv_data = csv_data.values.tolist()

    conn = psycopg2.connect(database="analysis", user="iceqboo", password="62350000", host="106.54.96.164", port="5432")
    cur = conn.cursor()

    # cur.execute('select * from pg_database')
    # print(cur.fetchall())

    for i in csv_data[1:]:
        for j in range(len(i)):
            if (re.match(r'\t$', i[j]) or re.match(r'^[ ]+\t$', i[j]) or re.match(r'^[ ]+$', i[j])):
                i[j] = 'null'
            elif (re.match(r'[A-Z!-@a-z0-9\u4E00-\u9FA5_]+[ ]+$', i[j]) or re.match(r'[A-Z!-@a-z0-9\u4E00-\u9FA5_]+[ ]*\t$', i[j])):
                i[j] = re.sub(r'\t', '', i[j])
                i[j] = '\'' + re.sub(r'[ ]+', '', i[j]) + '\''
            else:
                i[j] = '\'' + i[j] + '\''
        print(i)
        sql = "INSERT INTO public.alipay VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % (
            i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15])
        cur.execute(sql)

        conn.commit()
    cur.close()
    conn.close()

insert_alipay('C:\\Users\\iceqb\\Desktop\\alipay_record_20191111_1019_1.csv')


# a = 'abcsdf'
# b = 'asdfdf      '
# c = 'adsfasdf     \t'
# d = '         '
# e = '          \t'
# f = '\t'
#
#
# re.match(r'^[A-Za-z0-9\u4E00-\u9FA5]+$', a)      #a = 'abcsdf'
# re.match(r'[A-Za-z0-9\u4E00-\u9FA5]+[ ]+$', a)   #b = 'asdfdf      '
# re.match(r'[A-Za-z0-9\u4E00-\u9FA5]+[ ]+\t$', a) #c = 'adsfasdf     \t'
# re.match(r'^[ ]+$', a)              #d = '         ' 全是空格
# re.match(r'^[ ]+\t$', a)            #e = '          \t'
# re.match(r'\t$', a)                 #f = '\t'
#
#re.sub(r'\t','',c)
#re.sub(r'[ ]+','',b)
#
# if(re.match(r'\t$', a) || re.match(r'^[ ]+\t$', a) || re.match(r'^[ ]+$', a)):
#     a = 'null'