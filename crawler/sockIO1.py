# coding:utf-8
import time
import socket
import sys
import threading
import ssl


def doRequest():
    response = bytes()
    sock = socket.socket()
    sock.connect(('119.75.217.26', 443))
    sock.send("GET /s?wd=c+socket%E7%BC%96%E7%A8%8B&rsv_spt=1&rsv_iqid=0xab2e7bff0000ee06&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&rqlang=&tn=baiduhome_pg&ch=&rsv_enter=1&prefixsug=c%2520socket&rsp=0&inputT=158378 HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nReferer: https://www.baidu.com/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\nCookie: BDUSS=kFDSlVPWEVxOUhNS0NTYXFpeWd5TGhWbGFVWWIwOEFYRmRIMlJyQWw4YjE4a0ZjQVFBQUFBJCQAAAAAAAAAAAEAAAAKodAby665s7XEc2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPVlGlz1ZRpcc; BIDUPSID=67970264B3B9DEE4ED332360E9CBC80B; PSTM=1545234309; BD_UPN=12314753; BAIDUID=E7EB59B954C6E3E2E6E26E9F1C2304F8:FG=1; ISSW=1; ISSW=1; H_PS_PSSID=1421_21110_28131_26350_28267; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=1; BDSVRTM=0; sug=3; sugstore=0; bdime=0; H_PS_645EC=6a5abUHHmp%2Fzoatl413pvd2qp7XE003Cx%2Fyxdzgf5TPZy6dcIn9vOxN%2B8h55pZqJTdhQ; ORIGIN=2\r\n\r\n".encode("utf-8"))
    # response = sock.recv(1024)
    while True:
        buf = sock.recv(4096)
        response += buf
        if not len(buf):
            break
    print(response)
    return response


# def main():
if __name__ == "__main__":
    start = time.time()
    for i in range(1):
        doRequest()
    print("spend time is %s" % (time.time() - start))


