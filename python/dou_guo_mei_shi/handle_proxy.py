#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 2:40
# @Author  : Aries
# @Site    : 
# @File    : handle_proxy.py
# @Software: PyCharm


#60.17.177.187 代理出来的ip
import  requests
url = 'http://ip.hahado.cn/ip'
proxy = {'http':'http://H79623F667Q3936C:84F1527F3EE09817@http-cla.abuyun.com:9030'}
response = requests.get(url=url,proxies=proxy)
print(response.text)