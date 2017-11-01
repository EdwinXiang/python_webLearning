#coding:utf-8
import time
import threading

def saySorry():
	print("亲爱的，我错了，我可以亲亲你吗")
	time.sleep(1)

# 单线程执行
# if __name__ == '__main__':
# 	for i in range(5):
# 		saySorry()

# 多线程执行
if __name__ == '__main__':
	for i in range(5):
		t = threading.Thread(target=saySorry)
		t.start()