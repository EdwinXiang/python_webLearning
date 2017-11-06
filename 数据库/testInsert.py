#coding:utf-8

from redis_app import *

sql = 'insert into student(sname,gender) values(%s,%s)'
sname = raw_input("请输入用户名:")
gender = raw_input("请输入性别，1为男，2为女")
params=[sname,bool(gender)]

MysqlHelper = MysqlHelper('localhost',3306,'stu','root','123')
count = MysqlHelper.insert(sql,params)

if count == 1:
	print('ok')

else:
	print('error')


