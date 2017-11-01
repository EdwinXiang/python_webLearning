#coding:utf-8
from multiprocessing import Process,Queue
import os,time,random

#写数据进程执行的代码
def write(q):
	for value in ['a','b','c','d']:
		print 'put %s to queue...' % value
		q.put(value)
		time.sleep(random.random())


# 读取数据
def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print "get %s from queue."%value
			time.sleep(random.random())
		else:
			break

if __name__ == '__main__':
	# 父进程创建queue。饼传给各个子进程
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	# 启动子进程pw，写入
	pw.start()
	# 等待pw结束
	pw.join()
	# 启动子进程pr，读取
	pr.start()
	pr.join()
	print ''
	print "所有的数据都写入并且读完"

