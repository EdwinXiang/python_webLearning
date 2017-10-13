#coding:utf-8
from multiprocessing import Process
import time
import os

# 两个子进程将会调用的两个方法
def worker_1(interval):
	print("worker_1,父进程(%s),当前进程(%s)"%(os.getppid(),os.getpid()))
	t_start = time.time()
	time.sleep(interval) #程序将会被挂起interval秒
	t_end = time.time()
	print("worker_1,执行时间'%0.2f'秒"%(t_end - t_start))


def worker_2(interval):
	print("worker_2,父进程(%s),当前进程(%s)"%(os.getppid(),os.getpid()))
	t_start = time.time()
	time.sleep(interval)
	t_end = time.time()
	print("worker_1,执行时间'%0.2f'秒"%(t_end - t_start))

#输出当前程序的ID
print("进程id:%s"%os.getpgid())
# 创建两个进程
p1 = Process(target = worker_1,args=(2,))
p2 = Process(target = worker_2,name = "dongo"args=(1,))

p1.start()
p2.start()

# 同时父进程任然往下执行 如何p2进程还在执行，将会返回true
print("p2.is_alive=%s"%p2.is_alive())

# 输出p1和p2进程的别名和pid
print("p1.name=%s"%p1.name)
print("p1.pid=%s"%p1.pid)

print("p2.name=%s"%p2.name)
print("p2.pid=%s"%p2.pid)

p1.join()
print("p1.is_Alive=%s"%p1.is_alive())
