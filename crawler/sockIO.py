#!/usr/bin/env python
# encoding: utf-8

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
urllist = []
re1 = 'abcmlyx'
re2 = '012346789'
url = 'http://d0b0501117c64a40b78b2f63757bf95a0cdfaa13fe70407c.changame.ichunqiu.com/js/'
pool = ThreadPool()
def url_list():
    for i in re1:
        for j in re1:
            for k in re2:
                for l in re2:
                    for m in re2:
                        urllist.append(url+i+j+'ctf'+k+l+m+'.js')
    return urllist

def url_open(url):
        try:
            result = urllib2.urlopen(url).read()
            if '404' not in result:
                print url+result
        except:
            pass


def main():
    urllist = url_list()
    pool.map(url_open, urllist)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
