#coding:utf-8
import hashlib
import datetime

KEY_VALUE = "itcast"

now = datetime.datetime.now()
m = hashlib.md5()
str = "%s%s" % (KEY_VALUE,now.strftime("%Y%m%d"))
print(str)
m.update(str.encode("utf-8"))
value = m.hexdigest()
print(value)