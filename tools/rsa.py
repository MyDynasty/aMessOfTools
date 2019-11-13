#!/usr/bin/env python
#coding -*- utf:8 -*-

def one(c,d,n):
    '''
    :param c:  int
    :param d:  int
    :param n:  int
    :return:
    '''

    return bytearray.fromhex(hex(pow(c,d,n))[2:])

def two(n,e,p,q,c):
    '''
    :param n: int
    :param e: int
    :param p: int
    :param q: int
    :param c: b'\x0f\x04\xb3\xb6~\xf20\xf8\x0b\xb5\x18\xd2m\xed8\xaf\x84\xb6\xc8\xd8{\xa8\x0c\t\xeb\xf1\xd8e\x120\x82\xfa'
    :return:
    '''

    import gmpy2
    import rsa
    d = int(gmpy2.invert(e, (p - 1) * (q - 1)))
    privatekey = rsa.PrivateKey(n, e, d, p, q)
    return  rsa.decrypt(f.read(), privatekey).decode()

if __name__ == '__main__':
    n = 98432079271513130981267919056149161631892822707167177858831841699521774310891
    e = 65537
    p = 302825536744096741518546212761194311477
    q = 325045504186436346209877301320131277983
    with open('C:\\Users\\iceqb\\Downloads\\fujian\\encrypted.message3','rb') as f:
        c = f.read()
    print(c)
    two(n,e,p,q,c)