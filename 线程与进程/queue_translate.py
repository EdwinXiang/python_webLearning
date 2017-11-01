#coding:utf-8
from multiprocessing import Manager,Pool
import os,time
import random

def reader(q):
	print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
	for i in range(q.qsize()):
		print("reader从queue中获取到的消息:%s"%q.get(True))


def writer(q):
	print("writer启动(%s),父进程(%s)"%(os.getpid(),os.getppid()))
	for i in range("zengmengting"):
		q.put(i)


if __name__ == '__main__':
	print("%s start"%os.getpid())
	q = Manager().Queue()
	po = Pool()
	po.apply(writer,(q,))
	po.apply(reader,(q,))
	po.close()
	po.join()
	print("%s end"%os.getpid())