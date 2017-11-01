#coding:utf-8
import threading
import time

# 线程执行代码的封装
class MyThread(threading.Thread):
	"""自定义线程"""
	def run(self):
		for i in range(3):
			time.sleep(1)
			msg = "I'm" + self.name + ' @ ' + str(i) # name 保属性中保存的事当前线程的名字
			print(msg)

		
if __name__ == '__main__':
	t = MyThread()
	t.start()