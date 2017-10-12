#coding:utf-8
import random

# 定义一个列表来存储3个办公室
offices = [[],[],[]]
# 定义一个列表用来存储8位老是的名字
names = ['a','b','c','d','e','f','g','h']

i = 0
for name in names:
	index = random.randint(0,2)
	offices[index].append(name)

i = 1
for tempName in offices:
	print('offices %d de renshu:%d' % (i,len(tempName)))
	i += 1

	for name in tempName:
		print("%s" % name,end = '')
		print("\n")
		print("-"*20)
		