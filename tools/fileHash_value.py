# coding=utf-8

import hashlib
import sys

def match(file_path,Bytes=1024):
    md5_1 = hashlib.md5()
    with open(file_path,'rb') as f:
        while 1:
            data = f.read(Bytes)
            if data:
                md5_1.update(data)
            else:
                break
    ret = md5_1.hexdigest()
    return ret
def get_md5(data):
    md5_1 = hashlib.md5()
    md5_1.update(data.encode('utf8'))
    return md5_1.hexdigest()


if __name__ == '__main__':

    try:
        file_path = sys.argv[1]
    except:
        file_path = input('请输入文件路径：')
    print(match(file_path))