#coding:utf-8
from socket import *
from multiprocessing import *
from time import sleep
from threading import Thread

# 处理客户的的请求并未其服务
def dealWithClient(newSocket,destAddr):
	while True:
		recvData = newSocket.recv(1024)
		if len(recvData) > 0:
			print("recv[%S]:%s"%(str(destAddr),recvData))
		else:
			print("[%s]客户端已经关闭"%str(destAddr))
			break
	newSocket.close()


def main():
	
	serSocket = socket(AF_INET,SOCK_STREAM)
	serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	localAddr =('',7788)
	serSocket.bind(localAddr)
	serSocket.listen(5)

	try:
		while True:
			print("---主进程，等待新客户端的到来---")
			newSocket,destAddr = serSocket.accept()

			print("---主进程,接下来创建一个新的进程负责数据处理[%s]---"%str(destAddr))
			# 创建多进程
			# client = Process(target=dealWithClient,args=(newSocket,destAddr))
			# 创建多线程
			client = Thread(target=dealWithClient,args=(newSocket,destAddr))
			client.start()

			# 因为已经向子进程中copy了一份，并且父进程中这个套接字页没有用处了
			# 所以关闭
			newSocket.close()
	finally:
		# 当为所有的客户端服务完之后再进行关闭，表示不再接收新的客户端链接
		serSocket.close()

if __name__ == '__main__':
	main()