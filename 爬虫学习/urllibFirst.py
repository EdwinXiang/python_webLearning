# !/usr/bin/env python
#coding:utf-8
import urllib2

# url 作为request()方法的参数，构造并返回一个request对象
request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen('http://www.baidu.com')
# 将request对象作为urlopen()方法的参数，发送给服务器并接收响应
respone = urllib2.urlopen(request)
html = respone.read()
print html