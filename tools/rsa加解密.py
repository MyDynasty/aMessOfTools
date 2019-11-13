import math
import random

#生成素数数组
def prime_array():
    arraya = []
    for i in range(2,100): #生成前100中的素数，从2开始因为2是最小的素数
        x = prime(i,2)    #i为素数是返回True，则将x加入arraya数组中;2为测试值
        if x:
            arraya.append(i)
    return arraya

#判断是否为素数
def prime(n, test_divisor):
    if math.sqrt(n) < test_divisor:
        return True   #为素数时返回True
    if n % test_divisor == 0:
        return False  #不为素数时返回Fasle
    else:
        return prime(n, test_divisor+1)

#找出与（p-1）*(q-1)互质的数e
def co_prime(s):
    while True:
        e = random.choice(range(100))
        x = gcd(e,s)
        if x==1: #如果最大公约数为1，则退出循环返回e
            break
    return e

#求两个数的最大公约数
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

#根据e*d mod s = 1,找出d
def find_d(e,s):
    for d in range(100000000): #随机太难找，就按顺序找到d,range里的数字随意
        x = (e*d) % s
        if x==1:
            return d

#生成公钥和私钥
def main():
    a= prime_array()        #生成素数数组
    print("前100个素数:",a)
    p = random.choice(a)    #随机选择素数
    q = random.choice(a)
    print("随机生成两个素数p和q. p=",p," q=",q)
    n = p * q
    s = (p-1)*(q-1)
    #print("The p is ", p)
    #print("The q is ", q)
    #print("The n(p*q) is ",n)
    e = co_prime(s)         #找出与（p-1）*(q-1)互质的数e
    print("根据e和(p-1)*(q-1))互质得到: e=", e)
    d = find_d(e,s)
    print("根据(e*d) 模 ((p-1)*(q-1)) 等于 1 得到 d=", d)
    print("公钥:   n=",n,"  e=",e)
    print("私钥:   n=",n,"  d=",d)
    pbvk=(n,e,d)
    return pbvk

#生成public key公钥或private key私钥
#zx==0 公钥 zx==1 私钥
#a为元组(n,e,d)
def generate_pbk_pvk(a,zx):
    pbk = (a[0],a[1]) #public key公钥 元组类型，不能被修改
    pvk = (a[0],a[2]) #private key私钥
    #print("公钥:   n=",pbk[0],"  e=",pbk[1])
    #print("私钥:   n=",pvk[0],"  d=",pvk[1])
    if zx==0:
        return pbk
    if zx==1:
        return pvk

#加密
def encryption(mw, ned):
    # 密文B = 明文A的e次方 模 n， ned为公钥
    #mw就是明文A，ned【1】是e， ned【0】是n
    B = pow(mw,ned[1]) % ned[0]
    return B

#解密
def decode(mw, ned):
    # 明文C = 密文B的d次方 模 n， ned为私钥匙
    #mw就是密文B， ned【1】是e，ned【1】是d
    C = pow(mw,ned[1]) % ned[0]
    return C

if __name__=='__main__':
    n = 0xCE522FBBA31B08CEA95A54D9AC09BEC855CC927955FE1E6197EFFD693AA8F667F67C074B0390C66A0B8C11ABD11849CC570255FF8F982B236E34031711930AD4398D4E68FD279D4D0C7C7AC813BF5FF09AC58DDD35AA25F8D6BACD0B1A62261A81E7FB3F32D3C5C30802FA1EF78B5897CE65CDCD7EC6948FD86DC5ACD392C36B
    e = 0x010001
    d = 0x9AA40D34E566A0EE4D0EF0A40A076FE0B63653DEEFEE3D15470D50F1EB4EB3096F3CBD36A36082E6FEEAA86010A3D4C47CBEBA78874735A623B6864E6714C03AC2097F21CD6876BE31065FAA3E14194527E69CC37B6E535729FCFF8354D1BAFDA69845A0D9D3925019B0749B6B7B99D9D87E322E2F344B28130AF21BF7CE0C21
    pbvk = (n,e,d)
    pbk = generate_pbk_pvk(pbvk, 0) #公钥  if 0 return pbk if 1 return pvk
    #A = int(input("请输入明文: "))
    #print("加密中....")
    #B = encryption(A,pbk) #加密
    #print("生成的密文是: ", B)
    B = 29292378347128013190443474379188941158098023205802761774438019901525344990455045672895914920330818403708505560118235725959276565411191769689751391257043336700387783574633974398568843305193087795483042278466554619464690821717320592477304379124079059531958922420316205962660361070097828384029619923396330056729
    pvk = generate_pbk_pvk(pbvk, 1)  #私钥
    #print(pvk)
    print("解密中....")
    C = decode(B,pvk)     #解密
    print("解密后的明文是: ", C)
    if A==C:
        print("加密前的明文和解密后的明文一样，成功!!!")