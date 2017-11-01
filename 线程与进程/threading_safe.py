#coding:utf-8
# 使用互斥锁来实现线程同步
from threading import Thread,Lock
import time

g_num = 0
def test1():
	global g_num
	for i in range(1000):
		# true表示堵塞  即如果这个锁在上锁之前已经被锁上了，那么这个线程会在这里一直等待到解锁为止
		# false 表示非堵塞 即不管本次调用能够成功上锁，都不会卡在这，而是继续执行下面的代码
		matexFlag = mutex.acquire(True)
		if matexFlag:
			g_num += 1
			mutex.release()

	print("---test1---g_num=%d"%g_num)


def test2():
	global g_num
	for i in range(1000):
		mutexFlag = mutex.acquire(True)
		if mutexFlag:
			g_num += 1
			mutex.release()

	print("---test2---g_num=%d"%g_num)

#创建一个互斥锁
#这个默认是为上锁的状态

mutex = Lock()

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)