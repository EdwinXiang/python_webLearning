#coding:utf-8
import re

# ret = re.match(r"<(\w*)><(\w*)>.*</2></1>","<html><h1>www.itcast.com</h1></html>")
# print(ret.group())
ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.itcast.cn</h1></html>")
print(ret.group())